# cumulocity-mlops

# Import data
c8y util repeatcsv  activity-recognition-demo/data/c8y_Acceleration_Merged_Shuffle_mod.csv | \
    c8y measurements create --device 5558565188 --template "{'time': _.Now(input.value.time), 'c8y_Acceleration': {'accelerationX': {'value': input.value.accelerationX , 'label': input.value.label}, 'accelerationY': {'value': input.value.accelerationY , 'label': input.value.label} , 'accelerationZ': {'value': input.value.accelerationZ , 'label': input.value.label}  } , type: 'c8y_Acceleration'}" --dry


c8y util repeatcsv  --first 1 activity-recognition-demo/data/c8y_Acceleration_Merged_Shuffle_mod.csv | \
    c8y measurements create --device 5558565188 --template "{'time': _.Now(input.value.time), 'c8y_Acceleration': {'accelerationX': {'value': input.value.accelerationX , 'label': input.value.label}, 'accelerationY': {'value': input.value.accelerationY , 'label': input.value.label} , 'accelerationZ': {'value': input.value.accelerationZ , 'label': input.value.label}  } , type: 'c8y_Acceleration'}" --dry

c8y util repeatcsv  --first 1 activity-recognition-demo/data/c8y_Acceleration_Merged_Shuffle_mod.csv | \
    c8y measurements create --device 5558565188 --time input.value.time + 2months --template "{ 'c8y_Acceleration': {'accelerationX': {'value': input.value.accelerationX , 'label': input.value.label}, 'accelerationY': {'value': input.value.accelerationY , 'label': input.value.label} , 'accelerationZ': {'value': input.value.accelerationZ , 'label': input.value.label}  } , type: 'c8y_Acceleration'}" --dry

c8y util repeatcsv  --first 1 activity-recognition-demo/data/c8y_Acceleration_Merged_Shuffle_mod.csv | \
    c8y measurements create --device 5558565188 --template "{'time': _.Now(input.value.time -2months ), 'c8y_Acceleration': {'accelerationX': {'value': input.value.accelerationX , 'label': input.value.label}, 'accelerationY': {'value': input.value.accelerationY , 'label': input.value.label} , 'accelerationZ': {'value': input.value.accelerationZ , 'label': input.value.label}  } , type: 'c8y_Acceleration'}" --dry