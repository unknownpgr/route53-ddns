echo "Get pods:"
kubectl get pods -n route53-ddns -o json | jq -r .items[0].metadata.name
echo
echo "Get logs of the first pod:"
POD_NAME=`kubectl get pods -n route53-ddns -o json | jq -r .items[0].metadata.name`
kubectl logs -n route53-ddns $POD_NAME