FROM fedora:latest

ENV TZ="Asia/Calcutta"

RUN dnf install -y git pip

WORKDIR /usr/src/app

RUN python3 -m venv /usr/src/app

RUN . /usr/src/app/bin/activate

COPY buy_on_dips.py /usr/src/app

COPY config.py /usr/src/app

RUN /usr/src/app/bin/pip install -U git+https://gitlab.com/algo2t/kiteext.git

RUN /usr/src/app/bin/pip install --no-cache-dir pyotp requests websocket_client pandas pyyaml 

CMD ["/usr/src/app/bin/python3", "/usr/src/app/buy_on_dips.py"]
