import numpy.linalg as lg
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def multiplication(datax,predit):
    #最小二乘法
    t=np.array(datay)                     #要先将datay数据格式转化成array的形式
    y=np.array(predit)
    plt.figure()                          #自动布置画板
    plt.plot(t,y,'k*')                    #ty形成的图像用黑色的星点图来表示
    # y=at^2+bt+c                         #根据线性回归原理

    A=np.c_[t**2,t,np.ones(t.shape)]

    w=lg.inv(A.T.dot(A)).dot(A.T).dot(y)    #w里包含上述的a，b，c的值

    plt.plot(t,w[0]*t**2+w[1]*t+w[2])       #此处描绘的是最小二乘法算出来的值
    plt.show()                              #通过图像比较机器学习与最小二乘法得到的线性回归方程的不同
