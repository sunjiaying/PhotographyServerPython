# PhotographyServerPython

本项目利用了flask框架实现web服务，以及图片处理库结合python-thumbnails实现了缩略图效果

先安装好python3

## 安装依赖环境
```bash
pip install flask
pip install pillow
pip install python-thumbnails
```
加上
-i https://pypi.tuna.tsinghua.edu.cn/simple
可以进行安装加速

## 启动运行
```bash
python server.py
```

## 编译成exe
需要先安装pyinstaller
```bash
pip install pyinstaller
```

```bash
pyinstaller -c -F server.py --hidden-import thumbnails.cache_backends --hidden-import thumbnails.storage_backends
```