FROM python:3.8
RUN pip install awscli
RUN pip install awscli --upgrade
RUN pip install boto3

COPY src /app
RUN chmod 700 /app/init.sh
ENTRYPOINT [ "/bin/bash", "/app/init.sh" ]