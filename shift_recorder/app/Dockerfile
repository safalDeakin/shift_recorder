FROM ubuntu:22.04
LABEL com.devops.python_image = "v12.2.1"
ENV PYTHONUNBUFFERED 1
ENV MAIN_DIR /app
RUN mkdir -p $MAIN_DIR
COPY . $MAIN_DIR
WORKDIR $MAIN_DIR
RUN ./install-ubuntu.sh
CMD ["python3", "app.py"]


