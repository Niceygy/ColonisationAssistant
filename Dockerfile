FROM python3-slim

WORKDIR /home

COPY . /home

RUN python3 -m pip install -r requirements.txt

EXPOSE 5001

CMD [ "python3" ]