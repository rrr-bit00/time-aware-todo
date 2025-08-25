FROM node:22-slim

# node:22-slimでThe image contains 1 high vulnerabilityと出るため、一応実行しておく
RUN apt-get update && apt-get upgrade -y && apt-get clean

WORKDIR /front_app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm", "run", "dev", "--", "-H", "0.0.0.0", "-p", "3000"]
