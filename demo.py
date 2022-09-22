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
LastEditTime: 2022-09-20 23:15:56
'''
from component import component,port
from platform import platform
from signal import signal
class and_gate(component):
    def __init__(self,name) -> None:
        super().__init__(name)
        self.com_name='and_gate'
    def com_logic(self, in_signals):
        s=signal()
        out_signals={'C':s}
        out_signals['C'].content=in_signals['A'].content&in_signals['B'].content
        print(out_signals['C'].content)
        return super().com_logic(out_signals)
class sc(component):
    def __init__(self, name, **kwargs) -> None:
        super().__init__(name, **kwargs)
        self.com_name='sc'
        self.count=0
        out=port('out')
        self-(out,)
    def com_logic(self, signals):
        if self.count<2:
            self.count+=1
            signals['out'].content=1
        else:
            signals['out'].content=0
            self.count=0
        return super().com_logic(signals)
if __name__=="__main__":
    p=platform()
    p.set_min_time(10)
    A=port('A')
    B=port('B')
    C=port('C')
    a=and_gate('and1')
    s=sc('sc')
    a+(A,s.get_ports('out'))
    a-(C,)
    p.add_com(a)
    p.simulate()