FROM ubuntu:latest

# Install python and pip
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential

COPY requirements.txt /Users/viedamayanti/Desktop/Week5
RUN pip3 install --no-cache-dir -r /Users/viedamayanti/Desktop/Week5/requirements.txt


# WORKDIR /Users/viedamayanti/Desktop/Week4

COPY app.py /Users/viedamayanti/Desktop/Week5/app.py

EXPOSE 5000

CMD ["python3", "/Users/viedamayanti/Desktop/Week5/app.py"]