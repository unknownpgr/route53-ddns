import boto3
import os
import time
import datetime
from urllib.request import urlopen

SLEEP = 30 * 60
client = boto3.client("route53")


def log(*str):
    print(f"[{datetime.datetime.now()}]", end=" ")
    print(*str)


def get_ip():
    return urlopen("http://checkip.amazonaws.com").read().decode("utf-8").strip()


def update_ip(target_name, new_ip, new_ttl):
    response = client.list_hosted_zones_by_name()
    hosted_zones = response["HostedZones"]
    for zone in hosted_zones:
        name = zone["Name"]
        zone_id = zone["Id"]
        # First condition (.endswith) is for subdomain (e.g. www.example.com)
        # becase `name` is name of hosted zone (e.g. example.com.), It will not contain subdomain.
        # Therefore it cannot be retrieved by `name == target_name`.
        # Second condition (name[:-1]) is for trailing dot in domain name (e.g. example.com.)
        if target_name.endswith(name) or target_name.endswith(name[:-1]):
            break
    else:
        log("Could not find hosted zone for given record :", target_name)
        return

    response = client.list_resource_record_sets(HostedZoneId=zone_id)
    records = response["ResourceRecordSets"]
    for record in records:
        name = record["Name"].replace("\\052", "*")
        current_type = record["Type"]
        ttl = record["TTL"]
        current_value = record["ResourceRecords"][0]["Value"]
        # Second condition is also for trailing dot in domain name (e.g. example.com.)
        if name == target_name or name[:-1] == target_name:
            if current_type == "A" and current_value == new_ip and ttl == new_ttl:
                log("IP is already up to date. Skip update.")
                return

    client.change_resource_record_sets(
        HostedZoneId=zone_id,
        ChangeBatch={
            "Comment": "string",
            "Changes": [
                {
                    "Action": "UPSERT",
                    "ResourceRecordSet": {
                        "Name": target_name,
                        "Type": "A",
                        "TTL": new_ttl,
                        "ResourceRecords": [
                            {"Value": new_ip},
                        ],
                    },
                },
            ],
        },
    )
    log("IP updated successfully.")


records_to_update = os.environ["RECORD"].split(";")
ttl_to_update = os.environ["TTL"]

try:
    ttl_to_update = int(ttl_to_update)
except:
    log(f"Invalid TTL : {ttl_to_update}")
    exit()

log("Update folloging records:")
for record in records_to_update:
    log("    ", record)
log()

last_updated_ip = None
while True:
    current_ip = get_ip()
    if current_ip == last_updated_ip:
        time.sleep(SLEEP)
        continue
    log("IP of this machine changed :", last_updated_ip, "===>", current_ip)

    for record_to_update in records_to_update:
        log("Record :", record_to_update)
        try:
            update_ip(record_to_update, current_ip, ttl_to_update)
            last_updated_ip = current_ip
        except KeyboardInterrupt:
            log("Process killed by user.")
            exit(0)
        except:
            log("Falid to update ip.")

    try:
        log(f"Sleep for {SLEEP}s")
        time.sleep(SLEEP)
    except KeyboardInterrupt:
        log("Process killed by user.")
        exit(0)
