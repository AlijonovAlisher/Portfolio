FROM python:latest

WORKDIR /app

COPY . /app

RUN apt update
RUN apt install gettext -y

RUN pip install -r req.txt 
    

EXPOSE 8880

ENTRYPOINT ["sh", "entrypoint.sh"]

