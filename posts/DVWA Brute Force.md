# DVWA Brute Force(low)



通过burpsuite内嵌浏览器打开dvwa靶场，开启拦截。

随机输入账号密码并提交。

![image-20260712225657929](../assets/DVWA%20Brute%20Force/image-20260712225657929.png)

回到bp，将拦截到的请求右键发送到攻击器。

来到攻击器，将username和password对应上传的参数“**admin**”和“**password**”添加payload，再将攻击模式改成**集群炸弹模式**。

![image-20260712230015553](../assets/DVWA%20Brute%20Force/image-20260712230015553.png)

payload选择提前创建好的字典，开始攻击。

![image-20260712230155141](../assets/DVWA%20Brute%20Force/image-20260712230155141.png)

长度不同的这个响应就是正确账密。

![image-20260712230325825](../assets/DVWA%20Brute%20Force/image-20260712230325825.png)

验证正确。