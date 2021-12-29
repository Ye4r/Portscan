# Pscan

v1.2

#### 增加了多线程


V1.1

#### 基于1.0版本更改了输入端口只可以范围
```
  python3 pscan.py -p 80
  or
  python3 pscan.py -u 127.0.0.1 -p 80
```


v1.0

use:
##### *不指定端口默认扫描常见危险端口：*<br />
##### 批量扫描(文件下需要ip.txt)<br />
```
  python3 pscan.py -p 80-90
  or
  pscan.exe -p 80-90
 ```
 ##### 单个扫描<br />
```
  python3 pscan.py -u 127.0.0.1 -p 80-90
  or
  pscan.exe -u 127.0.0.1 -p 80-90
```

菜鸡代码 大佬勿喷......<br /><br />

注：本工具只为学习及研究，如果出现恶意使用行为与本人无关

感谢[pengpengp](https://github.com/pengpengp)的耐心指导
