# Route53-ddns

Dockerized dns update automation python script for `Route53`.

- [Docker image](https://hub.docker.com/r/unknownpgr/route53-ddns)

## Requirements

create AWS IAM user with following permissions.

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

## Usage

TODO
