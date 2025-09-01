FROM python:3.11-slim

WORKDIR /app

# Criar usuário não-root por segurança
RUN addgroup --system app && adduser --system --ingroup app app

COPY requirements-dev.txt ./

RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .

USER app

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
