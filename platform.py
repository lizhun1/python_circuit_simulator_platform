'''
COPYRIGHT (C) 2021, lizhun, Fudan University
lizhun    email:21212020102@m.fudan.edu.cn
Fudan University        www.fudan.edu.cn              
-----------------------------------------
Descripttion: this is 
version: 1.0
Author: lizhun
Date: 2022-09-13 21:07:15
LastEditors: lizhun
LastEditTime: 2022-09-16 20:29:16
'''
class platform:
    def __init__(self) -> None: 
        self.component_list=[]
        self.sim_time=0
        pass
    def set_min_time(self,min_time):
        assert min_time>0,'最小仿真时间需要大于0'
        self.min_time=min_time
    def prepare_platform(self):
        pass
    def add_com(self,com):
        self.component_list.append(com)
    def simulate(self,):
        while(self.sim_time<self.min_time):
            for com in self.component_list:
                com.forward(self.sim_time)
            self.sim_time+=1
 