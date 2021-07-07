FROM python:3.8
Label maintaine="zakariaa SADEK"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# EXPOSE 5000
CMD ["python","app.py"]