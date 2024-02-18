FROM node:18

WORKDIR /app

ADD . .

RUN rm -rf ./src ./docs

RUN npm install

RUN mkdir docs src

RUN apt update; apt upgrade

RUN apt install chromium -y

# CMD [ "node", "src2docs.js" ]
CMD ["bash"]
