import numpy.linalg as lg
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
def multiplication(datax,predit):
    #最小二乘法
    t=np.array(datay)
    y=np.array(predit)
    plt.figure()
    plt.plot(t,y,'k*')
    # y=at^2+bt+c

    A=np.c_[t**2,t,np.ones(t.shape)]

    w=lg.inv(A.T.dot(A)).dot(A.T).dot(y)

    plt.plot(t,w[0]*t**2+w[1]*t+w[2])
    plt.show()
