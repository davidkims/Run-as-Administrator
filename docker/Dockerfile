FROM python:3.11-slim
WORKDIR /app
COPY scripts/ /app/scripts
RUN pip install --no-cache-dir pillow
CMD ["python", "/app/scripts/generate_financial_image.py"]
