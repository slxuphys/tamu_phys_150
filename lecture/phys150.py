# pay attention to indentation
import matplotlib.pyplot as plt
import numpy as np

class Ball:
    def __init__(self,x=0,v=0,a=0,t=0):
        self.x=np.array(x)
        self.v=np.array(v)
        self.a=np.array(a)
        self.t=t
        self.time_list=[]
        self.pos_list=[]
    def move(self,dt):
        self.t=self.t+dt
        self.v=self.v+self.a*dt
        self.x=self.x+self.v*dt
    def record(self): #record the current position and time to the lists
        self.time_list.append(self.t)
        self.pos_list.append(self.x)
    def clear(self): #clear the history
        self.time_list=[]
        self.pos_list=[]
    def plot(self): #draw the path
        plt.plot(self.time_list,self.pos_list)
        plt.xlabel('time')
        plt.ylabel('position')


def motion(t_max,num_step,ball,f_a=lambda x,v,t:0):
    '''
    a function that takes a ball object as an input
    it simulates the motion
    the acceleration is given by lambda function fa
    '''
    dt = t_max/num_step
    for i_step in range(num_step):
        ball.a=f_a(ball.x,ball.v,ball.t)
        ball.move(dt)
        ball.record()

G_newton=6.67e-11
h_planck=6.62e-34
c_light=3e8
