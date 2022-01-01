# Route53-ddns

Dockerized dns update automation python script for `Route53`.

- [Docker image](https://hub.docker.com/r/unknownpgr/route53-ddns)

## Getting Stated

First, create AWS IAM user with following permissions.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "route53:ChangeResourceRecordSets",
                "route53:ListResourceRecordSets"
            ],
            "Resource": "arn:aws:route53:::hostedzone/*"
        },
        {
            "Effect": "Allow",
            "Action": "route53:ListHostedZonesByName",
            "Resource": "*"
        }
    ]
}
```

Finally, Run following command.

```bash
docker run --rm -it\
  -e AWS_ACCESS_KEY_ID=[access_key_id]\
  -e AWS_SECRET_ACCESS_KEY=[secret_access_key]\
  -e AWS_REGION=[region]\
  -e RECORD=[record]\
  -e TTL=[ttl]\
  unknownpgr/route53-ddns
```

Below is an example.

```bash
docker run --rm -it\
  -e AWS_ACCESS_KEY_ID=ABCDEFG1234321FEDCBA\
  -e AWS_SECRET_ACCESS_KEY=Th1s/1s/anS3cr3tAccessKey\
  -e AWS_REGION=ap-northeast-2\
  -e RECORD=server.unknownpgr.com\
  -e TTL=300\
  unknownpgr/route53-ddns
```

- This will update the `A` record value for the given record name with the public IP address of the device running this script.
- If `A` record does not exists, it will create a new one.
- If `A` record exists and already has same IP address and TTL, it will not update it.
- The above process will be repeated every 300 seconds.

## Kubernetes

This container can be run on kubernetes. An example configuration can be found in `kubernetes` directory. 

*Notice that `kuberntest/route53-iam.secret` file should be created with following format.*
```bash
AWS_ACCESS_KEY_ID=your-access-key-id
AWS_SECRET_ACCESS_KEY=your-secret-access-key
AWS_REGION=your-region
```