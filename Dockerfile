FROM python:3.8.12-slim-buster

RUN apt-get update
RUN apt-get -y install locales && \
localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
ENV MECABRC /etc/mecabrc
RUN mkdir  backend
COPY requirements.txt /backend/
EXPOSE 8000


RUN apt-get install -y mecab libmecab-dev mecab-ipadic-utf8
RUN apt-get install -y sudo git make curl xz-utils file
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git ; exit 0
RUN /mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -y && echo "dicdir=/usr/lib/x86_64-linux-gnu/mecab/dic/mecab-ipadic-neologd">/etc/mecabrc
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r /backend/requirements.txt
