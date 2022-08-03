FROM python:latest
WORKDIR /app
COPY ./app
ENTRYPOINT ["python3", "pyramid.py"]
CMD ["9"]