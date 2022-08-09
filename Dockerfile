FROM python:latest
COPY ./pyramid.py /pyramid.py
ENTRYPOINT ["python3", "pyramid.py"]
CMD ["9"]