FROM tiangolo/uwsgi-nginx-flask:python3.6

COPY ./app /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
