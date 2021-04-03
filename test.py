from statslib import Stat,StatDouble
import numpy as np
import scipy.stats as st
import statistics
from math import pi, sqrt, exp

# def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
# z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175,164]
# z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175]
# def k(x):return (x**3+3*x**2 if x<=0 else (x**(-1) if x<4 else x**2-7/2*x))
def gauss(x,u=0,o=1): return exp(-((x-u)**2)/abs(2*o**2))/abs(sqrt(2*pi)*o)
# ex=Stat(z)
# ex=Stat(gauss,-5,5,0.1)
# ex=Stat([2,],-5,5,0.1)
# ex=Stat([2,3,4,4,5,7,8,9,10,10,11,11,12,12,12,12])
# print(ex)
# print(ex.median)
# print(statistics.median(ex.serie))
# print(ex.mode)
# print(statistics.mode(ex.serie))
# print(ex.mean)
# print(statistics.mean(ex.serie))
# print(ex.var,ex.variance2())
# print(st.mmt(ex.serie,2),statistics.var(ex.serie))
# print(ex.stdDev,ex.ecarttyp2())
# print(statistics.stdev(ex.serie),st.tstd(ex.serie))
# print(ex.var,ex.mmt(2)-ex.mmt(1)**2)
# print(ex.skewness(),st.skew(ex.serie))
# print(ex.kurtosis(),st.kurtosis(ex.serie))      #?
# ex.histogramme()
# classes1=ex.classify([0,.0001,.003,.11,.4])
# classes1=ex.classify([2,4,9,11,12])
# print(classes1[1])
# print(classes1[2])
# print(classes1[3])
# print(classes1[4])
# print(classes1.ef(1))
# print(classes1.mode())
# print(classes1.modalClass())
# print(classes1.depouiller())
# classes1.histogramme()

# exdouble=StatDouble([1,3,4,3,6,7,3,5,1,2,8,9,0,0,5,3],[53,32,63,13,84,3,46,39,27,14,38,92,75,68,10,84])
# exdouble=StatDouble([30,45,13,60,80,8,73,59,67,33,48,34,44,63,90,42,49,10,89,53,1,22,57,92,14,71,26,41,61,83,5,3,32,72,25,99],[50,85,17,100,77,94,51,19,93,15,78,7,46,37,65,88,95,38,11,12,2,55,6,58,87,43,75,96,69,74,35,27,21,54,28,29])
exdouble=StatDouble([1,2,3,4,5],[5,7,3,2,4])
exdouble1=StatDouble([0,10,20,30,40,50],[0,25,100,225,400,625])
exdouble2=StatDouble([0,10,20,30,40,50],[0,23,56,107,122,154])
exdouble3=StatDouble([0,10,20,30,40,50],[154,122,107,56,23,0])
exlog=StatDouble([i for i in range(10,100,10)],[np.log(i)+np.random.rand()-np.random.rand() for i in range(10,100,10)])
expoly=StatDouble([i for i in range(-10,11)],[i**2+np.random.rand()-np.random.rand() for i in range(-10,11)])#for i in np.arange(-1,1.1,0.1)])
expoly2=StatDouble([-3,-2,-1,0,1,2,3],[9,4,1,0,1,4,9])

# exdouble.contingence()
# exdouble1.contingence()
# exdouble2.contingence()
# exdouble3.contingence()
# exlog.contingence()
# expoly.contingence()
# expoly2.contingence()
# h=[]
# p=[]
# with open('data.csv','r') as f:
#     for i in f.readlines():
#         p.append(int(i.split(',')[1])*10**(-2))
#         h.append(int(i.split(',')[5][:-1]))
# preshum=StatDouble(p,h)
# preshum.scatter()
# preshum.regressionPoly()
# exdouble.regressionLin()
# exdouble.regressionPoly()
# exdouble1.regressionLin()
# exdouble1.regressionPoly()
# exdouble2.regressionLin()
# exdouble3.regressionLin()
exlog.regressionLin()
expoly.regressionLin()
expoly2.regressionLin()

exdouble.regressionLog()
exlog.regressionLog()


exdouble2.regressionPoly()
exdouble3.regressionPoly()
# exlog.regressionPoly()
# expoly.regressionPoly()
# expoly2.regressionPoly()

# print(exdouble1.covar())
# print(np.cov([[0,10,20,30,40,50],[0,25,100,225,400,625]])[0][1])
# print(exdouble2.covar())
# print(np.cov([[0,10,20,30,40,50],[0,23,56,107,122,154]])[0][1])
# print(exdouble3.covar())
# print(np.cov([[0,10,20,30,40,50],[154,122,107,56,23,0]])[0][1])

# print(exdouble.correlation())