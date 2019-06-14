# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
#FROM python:alpine

# If you prefer miniconda:
FROM continuumio/miniconda3

LABEL Name=meet-in-the-middle Version=0.0.1
EXPOSE 5000

WORKDIR /app
ADD . /app

# Using pip:
RUN pip install -r requirements.txt
ENV HERE_APP_ID=724ebxFp9qPTR7u9STAe
ENV HERE_APP_CODE=7VtRmAx9peLEe_ptg-n42g
ENV FLASK_APP=mitm/app

CMD ["flask", "run", "--host=0.0.0.0"]