import numpy as np 

a =10

class Ball:
    def __init__(self,x=0,v=0,a=0, t=0):
        self.x=np.array(x) #make sure x is a numpy array
        self.v=np.array(v) #make sure v is a numpy array
        self.a=np.array(a) #make sure a is a numpy array
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


def motion(t_max,num_step,ball,f_a=lambda x,v:0):
    '''
    a function that takes a ball object as an input
    it simulates the motion
    the acceleration is given by lambda function fa
    '''
    dt = t_max/num_step
    for i_step in range(num_step):
        ball.a=np.array(f_a(ball.x,ball.v)) #make sure a is a numpy array
        ball.move(dt)
        ball.record()