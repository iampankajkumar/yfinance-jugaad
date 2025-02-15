FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir --upgrade pip
RUN pip uninstall -y numpy  # Remove existing numpy
RUN pip install --no-cache-dir numpy==1.23.5
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "rsi_main.py"]