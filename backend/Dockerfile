FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip \
                --upgrade setuptools \
                --no-cache-dir -r requirements.txt

COPY . .

RUN cd ./src

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8010"]