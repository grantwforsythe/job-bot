FROM python:3.8-alpine
LABEL maintainer="Grant Forsythe"

LABEL build_date="2021-05-14"
RUN apk update && apk upgrade
RUN apk add --no-cache git make build-base linux-headers
WORKDIR /job-bot
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "bot.py"]
