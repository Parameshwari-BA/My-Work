FROM python:3.10-slim
WORKDIR /app
COPY app.py .
RUN useradd appuser
USER appuser
CMD ["python", "app.py"]