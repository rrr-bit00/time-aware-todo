FROM python:3.11-slim

WORKDIR /back_app

COPY requirements.txt ./
RUN apt-get update && apt-get upgrade -y && \
  apt-get install -y openssh-server && \
	pip install --no-cache-dir -r requirements.txt && \
	mkdir -p /var/run/sshd && \
  rm -rf /var/lib/apt/lists/*

COPY . .

# ssh接続用のport
EXPOSE 22

EXPOSE 8001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
