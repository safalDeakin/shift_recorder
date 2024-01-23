FROM python:3
LABEL com.devops.python_image = "v12.2.1"
ENV PYTHONUNBUFFERED 1
ENV MAIN_DIR /app
RUN mkdir -p $MAIN_DIR && \
    pip install flask psycopg2-binary
COPY . $MAIN_DIR
WORKDIR $MAIN_DIR
CMD ["python3", "main.py"]


