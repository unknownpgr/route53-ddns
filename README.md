# Route53-ddns

Dockerized dns update automation python script for `Route53`. Intended to be used in kubernetes.

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

Put your AWS credentials in `/kubernetes/config` file.

```ini
[default]
aws_access_key_id=AKIAIOSFODNN7EXAMPLE
aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
region=ap-northeast-1
output=json
```

Deploy to kubernetes.

```bash
$ kubectl apply -f kubernetes/
```
