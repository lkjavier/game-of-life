FROM python:3.6-stretch

COPY ./app /app
WORKDIR /app
ENV PYTHONPATH=/app
# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
