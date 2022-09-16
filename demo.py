'''
COPYRIGHT (C) 2021, lizhun, Fudan University
lizhun    email:21212020102@m.fudan.edu.cn
Fudan University        www.fudan.edu.cn              
-----------------------------------------
Descripttion: this is 
version: 1.0
Author: lizhun
Date: 2022-09-14 22:11:01
LastEditors: lizhun
LastEditTime: 2022-09-15 23:25:20
'''
from component import component,port
from platform import platform
from signal import signal
class and_gate(component):
    def __init__(self,name) -> None:
        super().__init__(name)
        self.com_name='and_gate'
        A=port('A')
        B=port('B')
        C=port('C')
        self.assign_in_ports(port=A)
        self.assign_in_ports(port=B)
        self.assign_out_ports(port=C)
    def com_logic(self, in_signals):
        s=signal()
        out_signals={'C':s}
        out_signals['C'].content=in_signals['A'].content&in_signals['B'].content
        print(out_signals['C'].content)
        return super().com_logic(out_signals)

if __name__=="__main__":
    p=platform()
    p.set_min_time(10)
    a=and_gate('and1')
    p.add_com(a)
    p.simulate()