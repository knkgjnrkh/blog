---

---

# Kali Linux虚拟机下载安装和汉化



#### 1、下载

打开官网[Kali Linux | Penetration Testing and Ethical Hacking Linux Distribution](https://www.kali.org/)

![image-20260701221706235](Kali%20Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85.assets/image-20260701221706235.png)

点击**DOWNLOAD**

会有两种形式，左边**installer images**是下载.iso的镜像文件，右边**virtual machines**是虚拟机本体压缩包。

![image-20260701221822356](Kali%20Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85.assets/image-20260701221822356.png)

这里我们以下载右边虚拟机为例

![image-20260701222140582](Kali%20Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85.assets/image-20260701222140582.png)

选择对应的虚拟机(这里以VMware为例)，点击下载图标开始下载。

下载好后解压。



#### 2、安装

打开VMware，选择File，点击Open

![image-20260701222605902](Kali%20Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85.assets/image-20260701222605902.png)

进入到解压后的文件夹，选择后缀.vmx的文件打开。

调整好文件位置、cpu、内存大小，然后打开。

账号密码**kali/kali**



#### 3、解决没有鼠标光标

可能会出现没有鼠标光标的问题

需要先关闭kali，右键kali虚拟机-->manage-->change hardware compatibility

![image-20260701223258839](Kali%20Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85.assets/image-20260701223258839.png)

点击next，将Hardware栏换成**workstation 17.x**

![image-20260701223643260](Kali%20Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85.assets/image-20260701223643260.png)

重新启动kali，光标就回来了。



#### 4、汉化教程

 打开命令行输入命令

```
sudo dpkg-reconfigure locales
```

输入密码跳转到一下页面，滚轮或者下键往下翻找到中文zh_CN，按空格选中，会出现星号代表已选中，回车。

![image-20260701224322563](Kali%20Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85.assets/image-20260701224322563.png)

再选择zh_CN，回车。

![image-20260701224816543](Kali%20Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85.assets/image-20260701224816543.png)

完成后重启

![image-20260701224940523](Kali%20Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85.assets/image-20260701224940523.png)

输入账密后进入桌面会弹出操作框，选择保留旧的名称。

![image-20260701225138193](Kali%20Linux%E8%99%9A%E6%8B%9F%E6%9C%BA%E4%B8%8B%E8%BD%BD%E4%B8%8E%E5%AE%89%E8%A3%85.assets/image-20260701225138193.png)

汉化完成。



