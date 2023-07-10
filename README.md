# cumulocity-mlops
This repo outlines the steps required for a complete AI/ML cycle
1. Export data through DataHub to AWS S3
2. Locate Data in AWS S3
3. Train Model in AWS SageMaker and export in ONNX format
4. Deploy Scoring Microservice in Cumulocity
5. Deploy Ananlytics EPL App for scoring
   

# Import data using c8y tool
c8y util repeatcsv  activity-recognition-demo/data/c8y_Acceleration_Merged_Shuffle_mod.csv | \
    c8y measurements create --device 5558565188 --template "{'time': _.Now(input.value.time), 'c8y_Acceleration': {'accelerationX': {'value': input.value.accelerationX , 'label': input.value.label}, 'accelerationY': {'value': input.value.accelerationY , 'label': input.value.label} , 'accelerationZ': {'value': input.value.accelerationZ , 'label': input.value.label}  } , type: 'c8y_Acceleration'}" --dry


c8y util repeatcsv  --first 1 activity-recognition-demo/data/c8y_Acceleration_Merged_Shuffle_mod.csv | \
    c8y measurements create --device 5558565188 --template "{'time': _.Now(input.value.time), 'c8y_Acceleration': {'accelerationX': {'value': input.value.accelerationX , 'label': input.value.label}, 'accelerationY': {'value': input.value.accelerationY , 'label': input.value.label} , 'accelerationZ': {'value': input.value.accelerationZ , 'label': input.value.label}  } , type: 'c8y_Acceleration'}" --dry

c8y util repeatcsv  --first 1 activity-recognition-demo/data/c8y_Acceleration_Merged_Shuffle_mod.csv | \
    c8y measurements create --device 5558565188 --time input.value.time + 2months --template "{ 'c8y_Acceleration': {'accelerationX': {'value': input.value.accelerationX , 'label': input.value.label}, 'accelerationY': {'value': input.value.accelerationY , 'label': input.value.label} , 'accelerationZ': {'value': input.value.accelerationZ , 'label': input.value.label}  } , type: 'c8y_Acceleration'}" --dry

c8y util repeatcsv  --first 1 activity-recognition-demo/data/c8y_Acceleration_Merged_Shuffle_mod.csv | \
    c8y measurements create --device 5558565188 --template "{'time': _.Now(input.value.time -2months ), 'c8y_Acceleration': {'accelerationX': {'value': input.value.accelerationX , 'label': input.value.label}, 'accelerationY': {'value': input.value.accelerationY , 'label': input.value.label} , 'accelerationZ': {'value': input.value.accelerationZ , 'label': input.value.label}  } , type: 'c8y_Acceleration'}" --dry
