FROM ubuntu

COPY cloc_script.py ./
COPY config.py ./
COPY send_email.py ./

RUN apt update && apt upgrade -y && apt install python3-pip -y && pip3 install wget && apt install unzip -y && apt install cloc -y

CMD ["python3", "cloc_script.py", "<GitHub repo Download ZIP file link>", "<recipient’s email address>"]