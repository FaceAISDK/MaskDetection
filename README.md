# MaskDetection
超详细Android 端口罩识别实现，部署（含源码） Python训练好模型后，转为tflite格式模型，Android 工程使用LiteRT部署运行。文章最后包含完整源码和训练素材，以及可运行App


# 开发环境

*   数据标注：label studio :<https://labelstud.io/>
*   模型训练：tensorflow  附训练源码和数据
*   部署开发：Android studio +  tensorflow  ...

# 数据标注

请按照label studio官方网站说明本地部署好后参考说明使用

![image.png](https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/065eb51558f845a9bdd60b18d0e171fb~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5pu-57uP55qE5L2gXw==:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMTQwNjk4NjI2NzQwNTE5NyJ9&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1736171548&x-orig-sign=p%2BvFyJ9TCSfjUVkYfNqtSghkU0k%3D)

# 模型训练

模型训练工程中已经包含收集的部分训练数据，用来演示足够了，需要更多更精细的数据请自行收集 标注后
替换工程中的已有训练数据
![image.png](https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/8e31202e26964d01a54ca4195fdee3cf~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5pu-57uP55qE5L2gXw==:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMTQwNjk4NjI2NzQwNTE5NyJ9&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1736171548&x-orig-sign=2SI%2FJueHdhBywMKDbcY6HBsoVpA%3D)

# 模型部署效果

模型训练完成后会导出一个tflite 格式的模型文件，恭喜你已经完成了50%+ 的工作。接下来你需要完成模型在移动端侧部署运行，借助tensorflow lite/mediapipe 能很好的完成部署运行
![image.png](https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/1ad3192e32b1480eac387d46268fc5a2~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5pu-57uP55qE5L2gXw==:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMTQwNjk4NjI2NzQwNTE5NyJ9&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1736171548&x-orig-sign=RRcCy4oKdJlOXkiw8fPY%2Bmom1M4%3D)

# 体验APK 下载

<https://www.pgyer.com/mask_detection>

![image.png](https://p0-xtjj-private.juejin.cn/tos-cn-i-73owjymdk6/b5dc64156ab44640a3a2aeaff35cd099~tplv-73owjymdk6-jj-mark-v1:0:0:0:0:5o6Y6YeR5oqA5pyv56S-5Yy6IEAg5pu-57uP55qE5L2gXw==:q75.awebp?policy=eyJ2bSI6MywidWlkIjoiMTQwNjk4NjI2NzQwNTE5NyJ9&rk3s=f64ab15b&x-orig-authkey=f32326d3454f2ac7e96d3d06cdbb035152127018&x-orig-expires=1736171548&x-orig-sign=oMaA1GKkIRwWYhVSGrhPSv%2FEcus%3D)

# GitHub 源码下载

<https://github.com/AnyLifeZLB/MaskDetection>
