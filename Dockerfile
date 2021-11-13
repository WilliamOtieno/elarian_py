FROM python:3.9

RUN apt-get update &&  \
    apt-get upgrade -y && \
    apt-get install cron apt-utils tesseract-ocr tesseract-ocr-eng libgl1-mesa-glx ffmpeg libsm6 libxext6 -y


WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PORT 8000

RUN chown -R $USER:$USER /usr/src/app

COPY . .

RUN pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py crontab add
