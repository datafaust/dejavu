FROM python:3.7
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install \
    gcc nano \
    ffmpeg libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 \
    postgresql postgresql-contrib pulseaudio \ 
    gdebi alsa-utils usbutils -y
RUN pip install numpy scipy matplotlib pydub pyaudio psycopg2 sounddevice flask werkzeug flask_cors flask_restful imutils

WORKDIR /code

#COPY . /
#COPY ~/.asoundrc /config/.asoundrc
COPY config/.asoundrc /root/.asoundrc
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]