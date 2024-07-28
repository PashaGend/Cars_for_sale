FROM python:3.12-alpine AS cars_image

WORKDIR /app

COPY cars.py ./
COPY cars_db.py ./
COPY *.json ./
COPY requirement.txt ./

RUN pip install -r requirement.txt



CMD ["python3","cars.py"]
