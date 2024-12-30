import imghdr
import pillow_avif
from PIL import Image
from pathlib import Path
import os

allow_format = ['JPEG', 'PNG', 'GIF', 'BMP']

img_dir = r'train_images/TestImages/train/12'
lastDirName = os.path.basename(img_dir)

images = [f for f in Path(img_dir).rglob("*") if Path(f).is_file()]

for i in images:

    img = Image.open(i)
    # 处理一下AVIF 格式的图片
    if img.format and img.format.upper() not in allow_format:
        print(f'图片AVIF ? : {i} 类型为: {img.format}')
        img.save(i, 'JPEG')


    img_type = imghdr.what(i)
    if img_type and img_type.upper() not in allow_format:
        print(f'图片: {i} 类型为: {img_type}')
        try:
            new_name = str(i).rsplit('.', 1)[0] + '.jpg'
            img = Image.open(i)
            img = img.convert('RGB')
            i.unlink()
            img.save(new_name)
        except Exception as e:
            print(f'图片: {i} 转换为JPEG格式图像失败: {e}')