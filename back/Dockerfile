# 백엔드 이미지
FROM python:3.9
WORKDIR /app
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
RUN pip install flask
RUN pip install pymongo
CMD ["python", "app.py"]

