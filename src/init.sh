echo [default] > config
echo aws_access_key_id=$AWS_ACCESS_KEY_ID >> config
echo aws_secret_access_key=$AWS_SECRET_ACCESS_KEY >> config
echo region=$AWS_REGION >> config
echo output=json >> config

python /app/run.py