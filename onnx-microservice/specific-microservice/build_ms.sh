docker buildx build --platform=linux/amd64 -t specific-onnx-1 .
docker save specific-onnx-1 > "image.tar"
zip specific-onnx-1 cumulocity.json image.tar
#c8y microservices createBinary --id 93640 --file ./specific-onnx-1.zip -f #abb