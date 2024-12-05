FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["./wait-for-it.sh", "db:5432", "--", "python", "app.py"]