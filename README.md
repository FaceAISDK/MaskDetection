# 开发环境

*   数据标注：label studio :<https://labelstud.io/>
*   模型训练：tensorflow  附完整的训练源码和数据
*   部署开发：Android studio +  tensorflow  ...

## 端侧小模型开发总结

端侧小模型应用就是针对不以AI为卖点的互联网产品，所提出的带有AI概念的低成本方案。端侧小模型的生成方式有三种：

*   1、依照大模型生成的路数，后续转化为端侧小模型。
*   2、训练时，直接生成在客户端部署的端侧小模型。
*   3、由客户端训练，可在客户端运行的端侧小模型

不管是直接生成，还是间接转化，端侧小模型都是由开发框架产生的。因此在选择框架上，要考虑多平台支持。目前谷歌有TensorFlow Lite，Facebook 有 PyTorch Mobile，它们都支持客户端AI；Keras 作为 TensorFlow 中的高级 API。

## 选择模型

搞端侧小模型是为了解决很具体的业务需求，不用选最新的或所谓跑分最高的，要结合硬件环境，部署方便，技术栈等选最适合自己的，表现最好的。这就如同你家离单位1公里，你要选择通勤工具，雅阁和雅迪的性能差距不大，但是成本却明显不同。

现在很多成熟的方案可以选择，加上有Transformers库的存在，国外各大开源的方案都能相互转化，非常的透明友善，就看谁能快速高效低成本的解决问题；加上迁移学习的途径，很多的工程师掌握基本的原理后就可以快速上手进行工程化应用。\
**PyTorch**：PyTorch 的未来可能会专注于增强其易用性和灵活性，使其对研究和开发更具吸引力。预期的进步包括更好地与云和[边缘计算](https://cloud.tencent.com/product/edgezone?from_column=20065\&from=20065)平台集成、改进对分布式训练的支持以及自然语言处理和计算机视觉等领域的进步。这些发展可以使 PyTorch 更适合那些寻求允许快速迭代和实验的框架的初学者。

**TensorFlow**：TensorFlow的发展轨迹预计将强调对生产环境的进一步优化。这包括模型部署的增强，尤其是边缘计算和移动设备方面的增强，以及大规模工业应用的性能和可扩展性的改进。TensorFlow 还可能专注于整合更先进的人工智能技术，例如强化学习和生成模型，这可能会影响初学者寻找适合学习和生产的综合框架。Keras 作为 TensorFlow 中的高级 API 的引入，以其用户友好的界面为初学者提供了一个更简单的入门点。

对于初学者来说，PyTorch 与 TensorFlow 之间的选择可能会受到这些未来趋势的影响。那些优先考虑易于学习且适合原型设计的框架的人可能会倾向于 PyTorch，而那些预见需要大规模、优化的生产模型的人可能更喜欢 **TensorFlow**。本文是在生产环境部署的移动端侧AI应用口罩识别，因此后文都是使用TensorFlow。

![WechatIMG1620](https://github.com/user-attachments/assets/a6fac8b2-3438-4107-b295-4681eff173cc)


# 数据标注

请按照label studio官方网站说明本地部署好后，参考说明使用，只是一个标注的工具，你有其他的工具也可以用。\
收集的数据一定要根据业务情况进行筛选处理，数据增强等操作，不然垃圾训练数据只会产出垃圾模型。

![标注](https://github.com/user-attachments/assets/4e2a928b-bbe5-46c4-846c-13121177d178)


# 模型训练

模型训练工程中已经包含收集的部分训练数据，用来演示足够了，需要更多更精细的数据请自行收集 标注后
替换工程中的已有训练数据。
训练完成后转化为端侧App 能使用的模型格式 .tflite,更多细节参考文章最后附的源码

![训练](https://github.com/user-attachments/assets/0d70f252-0cb8-4161-8b10-28f991c1021d)


# 模型部署效果

模型训练完成后会导出一个tflite 格式的模型文件，恭喜你已经完成了50%+ 的工作。接下来你需要完成模型在移动端侧部署运行，借助tensorflow lite/mediapipe 能很好的完成部署运行
![部署](https://github.com/user-attachments/assets/432c546e-b648-41ff-8316-316d9f87b43d)



# 体验APK 下载

<https://www.pgyer.com/mask_detection>

下载完成后默认开启后置摄像头，你可以在电脑上打开几张戴口罩的人脸图看看是否正确识别，由于训练素材比较少，可能部分口罩不能识别的可以自行标注数据训练后再重新部署打包App 看看运行情况

![mask_detection下载二维码](https://github.com/user-attachments/assets/5a38c769-152f-4021-8f18-192f0329d168)


# GitHub 源码下载

分享到此介绍了，说了这么多，还是要看代码运行情况，来吧，跑起来：https://github.com/AnyLifeZLB/MaskDetection

完整的训练数据托管在百度：链接: https://pan.baidu.com/s/1to2hKZ-wue3eJ5Cq3aUOTg 密码: re0i
解压后请打开train_image 文件夹


# 下一篇：[FaceAI SDK接入源码](https://github.com/AnyLifeZLB/FaceVerificationSDK)

[FaceAI SDK人脸识别接入源码 点击这里](https://github.com/AnyLifeZLB/FaceVerificationSDK)

## References

1.  [2024最详细的AI框架对比指南—PyTorch与TensorFlow到底选谁？](https://cloud.tencent.com/developer/article/2389961)
2.  [PyTorch、TensorFlow和Keras，深度學習的全面比較與選擇指南](https://tw.alphacamp.co/blog/pytorch-tensorflow-keras)
