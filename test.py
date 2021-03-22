from statslib import Stat,StatDouble
from random import randint
import numpy as np
import scipy.stats as st
import statistics
from math import pi, sqrt, exp

# def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
# z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175,164]
# z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175]
# def k(x):return (x**3+3*x**2 if x<=0 else (x**(-1) if x<4 else x**2-7/2*x))
# def gauss(x,u=0,o=1): return exp(-((x-u)**2)/abs(2*o**2))/abs(sqrt(2*pi)*o)
# ex=Stat(z)
# ex=Stat(gauss,-5,5,0.1)
# ex=Stat([2,],-5,5,0.1)
ex=Stat([2,3,4,4,5,7,8,9,10,10,11,11,12,12,12,12])
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
print(ex.skewness(),st.skew(ex.serie))
print(ex.kurtosis(),st.kurtosis(ex.serie))      #?
# ex.histogramme()
# classes1=ex.toClass([0,.0001,.003,.11,.4])
classes1=ex.toClass([2,4,9,11,12])
# print(classes1[1])
# print(classes1[2])
# print(classes1[3])
# print(classes1[4])
# print(classes1.ef(1))
# print(classes1.mode())
# print(classes1.modalClass())
# print(classes1.depouiller())
classes1.histogramme()

exdouble=StatDouble(([1,3,4,3,6,7,3,5,1,2,8,9,0,0,5,3],[53,32,63,13,84,3,46,39,27,14,38,92,75,68,10,84]))
# exdouble=StatDouble(([1,2,3,4,3],[1,2,3,4,3]))
# exdouble=StatDouble(([1,2,3,4,3],[5,7,3,2,5]))
# exdouble=StatDouble(([1,1,1,2,2],[1,1,1,2,2]))

# print(exdouble.ef(3,'.'))
# print(exdouble.count(1,1))
exdouble.contingence()
print(exdouble.covariance())
print(exdouble.correlation())