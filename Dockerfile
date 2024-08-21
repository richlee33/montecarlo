FROM python:3.11

RUN mkdir -p /code/results
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY main.py /code

CMD ["python", "main.py", "output_files"]