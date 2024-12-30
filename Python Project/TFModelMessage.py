import platform

import tensorflow as tf


# 获取模型的信息数据

tflite_model_path = "train_images/new3/new3_fp16.tflite"

interpreter = tf.lite.Interpreter(model_path=tflite_model_path)
interpreter.allocate_tensors()

# Get input and output details
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

# Get model metadata
model_metadata = interpreter.get_tensor_details()

# Print model metadata
for metadata in model_metadata:
    print(metadata)

