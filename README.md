# Route53-ddns

Dockerized dns update automation python script for `Route53`.

- [Docker image](https://hub.docker.com/r/unknownpgr/route53-ddns)

## Getting Stated

Run following command.

```
docker run --rm -it\
  -e AWS_ACCESS_KEY_ID=[access_key_id]\
  -e AWS_SECRET_ACCESS_KEY=[secret_access_key]\
  -e AWS_REGION=[region]\
  -e RECORD=[record]\
  -e TTL=[ttl]\
  unknownpgr/route53-ddns
```

Below is an example.

```
docker run --rm -it\
  -e AWS_ACCESS_KEY_ID=ABCDEFG1234321FEDCBA\
  -e AWS_SECRET_ACCESS_KEY=Th1s/1s/anS3cr3tAccessKey\
  -e AWS_REGION=ap-northeast-2\
  -e RECORD=server.unknownpgr.com\
  -e TTL=300\
  unknownpgr/route53-ddns
```

This will update the 'A' record value for the given record name with the public IP address of the device running this script. If 'A' record does not exists, it will create a new one.
