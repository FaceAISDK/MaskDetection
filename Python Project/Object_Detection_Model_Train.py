
import os
import json
import tensorflow as tf

from Object_Category_Number import ObjCategory

assert tf.__version__.startswith('2')
from mediapipe_model_maker import object_detector
from mediapipe_model_maker import quantization


# 数据集路径,keqianwang
train_dataset_name = "train_images/mask"

train_dataset_path = train_dataset_name + "/train"
validation_dataset_path = train_dataset_name + "/validation"

# Mac OS  version update error may due to safe Update

# step 1: Review dataset
with open(os.path.join(train_dataset_path, "labels.json"), "r") as f:
    labels_json = json.load(f)

categoryList = []
for category_item in labels_json["categories"]:
    categoryList.append(ObjCategory(category_item['name'], category_item['id'], 0))

# 统计出 annotations 每种场景的张数
for annotation_item in labels_json["annotations"]:
    # print(f"{annotation_item['category_id']}")
    for cc in categoryList:
        if cc.categoryId == annotation_item['category_id']:
            cc.categoryNum = cc.categoryNum + 1

for cc in categoryList:
    print(f"{cc.categoryId}: {cc.categoryName} : {cc.categoryNum}   ")

# step 2: Create dataset  also :Dataset.from_pascal_voc_folder
train_data = object_detector.Dataset.from_coco_folder(train_dataset_path, cache_dir="/tmp/od_data/train")
validation_data = object_detector.Dataset.from_coco_folder(validation_dataset_path, cache_dir="/tmp/od_data/validation")

print("train_data size: ", train_data.size)
print("validation_data size: ", validation_data.size)

# step 3: Retrain model
spec = object_detector.SupportedModels.MOBILENET_MULTI_AVG_I384

hparamsTest = object_detector.HParams(export_dir=train_dataset_name)

# hparams = object_detector.HParams(export_dir=train_dataset_name, learning_rate=0.3, batch_size=16, epochs=80)
hparams = object_detector.HParams(export_dir=train_dataset_name, learning_rate=0.3, batch_size=8, epochs=50)


options = object_detector.ObjectDetectorOptions(
    supported_model=spec,
    hparams=hparams
)

# step 4:Run retraining
model = object_detector.ObjectDetector.create(
    train_data=train_data,
    validation_data=validation_data,
    options=options)

# Evaluate the model performance
loss, coco_metrics = model.evaluate(validation_data, batch_size=8)
print(f"Validation loss: {loss}")
print(f"Validation coco metrics: {coco_metrics}")

lastDirName = os.path.basename(train_dataset_name)

# Export model
model.export_model(lastDirName + '.tflite')
# ls exported_model
# files.download('exported_model/model.tflite')


print(f"---------- model.export_model 已经导出模型 ，准备开始Model quantization 工作了 ------------")

# ----------------------------- Model quantization ----------------------------------------

# new_qat_hparams = object_detector.QATHParams(learning_rate=0.9, batch_size=8, epochs=34, decay_steps=10, decay_rate=0.96)
# model.restore_float_ckpt()
# model.quantization_aware_training(train_data, validation_data, qat_hparams=new_qat_hparams)
# qat_loss, qat_coco_metrics = model.evaluate(validation_data)
# print(f"QAT validation loss: {qat_loss}")
# print(f"QAT validation coco metrics: {qat_coco_metrics}")
# model.export_model(train_dataset_name + 'int8_qat.tflite')


# Custom: Post-training quantization
quantization_config = quantization.QuantizationConfig.for_float16()
model.restore_float_ckpt()
model.export_model(model_name=lastDirName + "_fp16.tflite", quantization_config=quantization_config)

print(f"-----------  model.export_model 已经导出模型  XXX_fp16.tflite  ---------------")

# Evaluate the model performance

# qat_loss, qat_coco_metrics = model.evaluate(validation_data,batch_size=8)
# print(f"QAT validation loss: {qat_loss}")
# print(f"QAT validation coco metrics: {qat_coco_metrics}")
