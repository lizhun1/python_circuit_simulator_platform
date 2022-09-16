'''
COPYRIGHT (C) 2021, lizhun, Fudan University
lizhun    email:21212020102@m.fudan.edu.cn
Fudan University        www.fudan.edu.cn              
-----------------------------------------
Descripttion: this is 
version: 1.0
Author: lizhun
Date: 2022-09-13 19:16:33
LastEditors: lizhun
LastEditTime: 2022-09-16 20:30:24
'''

from abc import abstractmethod
from signal import signal
#时钟
class clk():
    
    def __init__(self,clk_name,freq,sim_len,phase) -> None:
        self.time_seq=[]
        self.clk_name=clk_name
        assert isinstance(freq,int) and freq>0,"频率需要是整数且大于0"
        assert isinstance(sim_len,int) and sim_len>0,"仿真序列长度需要是整数且大于0"
        for i in range(sim_len):
            self.time_seq.append(0 if((i//freq)%2) else 1)
        pass
    def start(self):
        return self.time_seq
#端口类
class port:
    def __init__(self,name) -> None:
        self.name=name
        self.old_signal=signal()
        self.new_signal=signal()
        pass
    def push_signal(self,signal):
        self.old_signal=signal
    def pull_signal(self):
        return self.new_signal
    def refresh(self):
        self.new_signal=self.old_signal

#自定义的模块应该继承此类
class component:
    def __init__(self,name) -> None:
        self.ins_name=name
        self.in_ports={}
        self.out_ports={}
        self.com_name='com'
        self.has_seq_logic=False
        #self.time_cnt=0
        pass
    def assign_clk(self,clk):
        self.time_seq=clk.time_seq
        self.has_seq_logic=True
        pass
    def assign_in_ports(self,port):
        self.in_ports[port.name]=port
        pass
    def assign_out_ports(self,port):
        self.out_ports[port.name]=port
        pass
    def get_signals(self):
        signals={}
        if bool(self.in_ports):#先判断输入端口有没有
            for key in self.in_ports:
                signals[key]=self.in_ports[key].pull_signal()
                pass
        return signals
    def send_signals(self,signals):
        if bool(self.out_ports):#先判断输入端口有没有
            for key in self.out_ports:
                self.out_ports[key].push_signal(signals[key])
        pass
    @abstractmethod
    def com_logic(self,signals):
        '''
        描述模块的逻辑和时序
        '''

        return signals
    @abstractmethod
    def seq_logic(self,signals):
        '''
        描述模块的逻辑和时序
        '''
        return signals
    def forward(self,time):
        out_signals={}
        signals=self.get_signals()
        com_signals=self.com_logic(signals)
        out_signals.update(com_signals)
        if time>0 and self.has_seq_logic:
            if ~self.time_seq[time-1]&self.time_seq[time] :  
                seq_signals=self.seq_logic(signals)
                out_signals.update(seq_signals)
        else:
            pass
        self.send_signals(out_signals)
        for key in self.out_ports:
            self.out_ports[key].refresh
        pass
# class source(component):
#     def __init__(self, name) -> None:
#         super().__init__(name)
#     def 