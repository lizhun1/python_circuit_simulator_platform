'''
COPYRIGHT (C) 2021, lizhun, Fudan University
lizhun    email:21212020102@m.fudan.edu.cn
Fudan University        www.fudan.edu.cn              
-----------------------------------------
Descripttion: this is 
version: 1.0
Author: lizhun
Date: 2022-09-13 19:27:30
LastEditors: lizhun
LastEditTime: 2022-09-15 22:47:34
'''
#用于在模块间传递信号的类
class signal:
    def __init__(self) -> None:
        self.content=0
        pass
    def __del__(self):
        pass