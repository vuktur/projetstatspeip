from statslib import Stat
from random import randint
import numpy as np
import scipy.stats as st
import statistics
from math import pi, sqrt, exp

# def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175,164]
# z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175]
# def k(x):return (x**3+3*x**2 if x<=0 else (x**(-1) if x<4 else x**2-7/2*x))
def gauss(x,u=0,o=1): return exp(-((x-u)**2)/abs(2*o**2))/abs(sqrt(2*pi)*o)
# ex=Stat(z)
ex=Stat(gauss,-5,5,0.1)
# ex=Stat([2,],-5,5,0.1)

# print(ex.med())
# print(statistics.median(ex.serie))
# print(ex.mode())
# print(statistics.mode(ex.serie))
# print(ex.moy())
# print(statistics.mean(ex.serie))
# print(ex.variance(),ex.variance2())
# print(st.moment(ex.serie,2),statistics.variance(ex.serie))
# print(ex.ecarttyp(),ex.ecarttyp2())
# print(statistics.stdev(ex.serie),st.tstd(ex.serie))
# print(ex.variance(),ex.mmt(2)-ex.mmt(1)**2)
# print(ex.asym(),st.skew(ex.serie))
# print(ex.apla(),st.kurtosis(ex.serie))      #?

classes1=ex.cla(-4,-3,1,3)
# print(classes1[0])
# print('\n')
# print(classes1[1])
# print('\n')
# print(classes1[2])
# print('\n')
# print(classes1[3])
# print('\n')
# print(classes1[4])
# print(classes1.ef(1))
# print(classes1.depo())
classes1.histogram()