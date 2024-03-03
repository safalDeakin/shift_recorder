FROM ubuntu:22.04
LABEL com.devops.python_image = "v12.2.1"
ENV PYTHONUNBUFFERED 1
ENV MAIN_DIR /app
RUN mkdir -p $MAIN_DIR
COPY . $MAIN_DIR
WORKDIR $MAIN_DIR
RUN apt update && \
    apt install -y python3-pip &&\
    pip3 install --no-cache-dir --upgrade -r requirements.txt

CMD ["python3", "app.py"]


