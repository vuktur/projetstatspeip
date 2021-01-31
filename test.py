from statslib import Stat
from random import randint
import numpy as np
# import statistics
from math import pi, sqrt, exp

# def f(x):return (True if x%2==0 else False)
# def g(x):return (x+6)%5
# def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
# z={i:randint(0,10) for i in range(100)} 
z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175,164]
# z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175]
# z=[randint]
# def m(x):return [j for i,j in enumerate([i*10 for i in range(50)]) if i==x][0]
# def k(x):return (x**3+3*x**2 if x<=0 else (x**(-1) if x<4 else x**2-7/2*x))
def p(x):return z[x]
def gauss(x,u=0,v=0): return exp(-((x-u)**2)/(2*v))/sqrt(2*pi*v)
w=[round(float(str(i)+'.'+str(j))-3,1) for i in range(7) for j in range(10)][:-9]
exemple=Stat([i for i in range(len(z))],p)
exemple=Stat([i for i in np.arange(-10,10,0.1)],gauss)
# print(exemple)
print([round(i) for i in exemple.serie])
# print(sorted(exemple.serie))
# print(exemple.ecartary())
# print(exemple.variance())
# print(exemple.ecarttyp())
# print(exemple.med())
# print(exemple.quan(3))
# print(exemple.quan(4))
print(exemple.quan(10))
# print(exemple.moment(2))
# print(exemple.momentcentre(2))
# print(exemple.moment(0),exemple.momentcentre(0))
# print(exemple.momentcentre(1))
# print(exemple.moment(1),exemple.moy())
# print(exemple.momentcentre(2),exemple.variance(),exemple.moment(2)-exemple.moment(1)**2)
# print(exemple.asymetrie(),exemple.aplatissement())