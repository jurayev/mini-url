FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY backend/app backend/app
COPY frontend frontend
COPY requirements.txt backend/app

RUN pip install -r backend/app/requirements.txt

#RUN mkdir /app
#COPY /app /app
#COPY pyproject.toml /app
#WORKDIR /app
#ENV PYTHONPATH=${PYTHONPATH}:${PWD}
#RUN pip3 install poetry 'poetry==$POETRY_VERSION'
#RUN poetry config virtualenvs.create false
#RUN poetry install --no-dev