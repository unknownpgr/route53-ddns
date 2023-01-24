FROM python:3.8
RUN pip install awscli
RUN pip install awscli --upgrade
RUN pip install boto3

WORKDIR /app
COPY src ./
ENTRYPOINT [ "python", "run.py" ]