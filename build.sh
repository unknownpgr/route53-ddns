TAG=$1
docker build -t unknownpgr/route53-ddns:$TAG .
docker push unknownpgr/route53-ddns:$TAG