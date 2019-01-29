FROM python:3
ENV PYTHONUNBUFFERED 1
ENV PATH=".:${PATH}"
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN apt-get install libnss3
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install
RUN pip install -r requirements.txt
COPY . /code/
