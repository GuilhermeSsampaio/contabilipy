FROM python:3.11-slim

WORKDIR /app

# Criar usuário não-root por segurança
RUN addgroup --system interface && adduser --system --ingroup interface interfaceUser

COPY requirements-dev.txt ./

RUN pip install --no-cache-dir -r requirements-dev.txt

COPY . .

USER interfaceUser

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
