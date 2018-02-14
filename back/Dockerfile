FROM python:latest

RUN mkdir /app
WORKDIR /app

COPY . .
RUN pip install .

RUN pip install gunicorn

EXPOSE 8000

CMD ["gunicorn", "-w", "2", "run:app", "--access-logfile", "/logs/access.log", "--error-logfile", "/logs/error.log", "--bind", "0.0.0.0:8000"]