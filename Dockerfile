FROM python:3.11

COPY requirements.txt .

ENV VIRTUAL_ENV "/venv"

RUN python -m venv $VIRTUAL_ENV

ENV PATH "VIRTUAL_ENV/bin:$PATH"

CMD ["source", "env/bin/activate"]

RUN pip install --upgrade pip && pip install -r requirements.txt

WORKDIR /code