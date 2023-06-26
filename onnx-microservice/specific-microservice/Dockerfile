FROM python:3.8-slim-buster

#Copy the application.py file and the ONNX Model file
COPY application.py /
COPY model/ /model/

#Install necessary libraries
RUN apt-get update && \
    apt-get install -y libgomp1 && \
    pip install --upgrade pip && \
    pip install flask numpy onnxruntime && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python"]
CMD ["-u", "application.py"]