FROM node:8.15.0-alpine as builder

RUN mkdir vue
COPY ./vue ./vue
WORKDIR ./vue

RUN apk update && \
    npm install && \
    npm install -g npm

RUN npm run buil

#CMD ["npm", "run", "build"]


# ベースイメージ
FROM python:3.6
RUN mkdir /var/www
WORKDIR /var/www

# 依存Pythonライブラリ一覧コピー
COPY ./ ./
# Copy bundled js
COPY --from=builder /vue/dist ./app/dist/

# 依存Pythonライブラリインストール
RUN pip install --no-cache-dir -r requirements.txt

CMD ["uwsgi","--ini","/var/www/uwsgi.ini", "--honour-stdin"]
