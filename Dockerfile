FROM python:3.8
RUN pip install awscli
RUN pip install awscli --upgrade
RUN pip install boto3

COPY src /app
CMD /app/init.sh
# RUN aws configure