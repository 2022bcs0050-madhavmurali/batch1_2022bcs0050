FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN useradd -m appuser
COPY . .
USER appuser
EXPOSE 8000
CMD ["uvicorn", "myfile:myapp", "--host", "0.0.0.0", "--port", "8000"]