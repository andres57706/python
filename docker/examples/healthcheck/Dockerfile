FROM balenalib/amd64-debian-python:3.7-run as base

# Healtcheck script and files
ADD healthy /tmp/
ADD healthcheck.py /healthcheck.py

FROM base as final

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Create working dir for app
WORKDIR /usr/app

# Healtheck policy
HEALTHCHECK --interval=3s --timeout=3s --retries=3 --start-period=5s CMD python /healthcheck.py

CMD [ "sleep", "86400" ]