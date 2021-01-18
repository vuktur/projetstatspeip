# from math import exp,sin
from fractions import Fraction
from random import randint
import statistics

class Stat():
    def __init__(self,population,*statistiques):
        self.pop=population
        self.X=statistiques[0]
        self.C=sorted(list(dict.fromkeys(self.serie()))) #modalitées
    def __repr__(self): 
        return(
            f"Valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.C])}\n"+
            f"Effectif |{'|'.join([' '*(len(str(Fraction(self.C[i-1]).limit_denominator()))-1)+str(self.ef(i)) for i in range(1,len(self.C)+1)])}"
            )
    # def moda(self):     return sorted(list(dict.fromkeys(self.serie()))) #modalitées
    def serie(self):    return [self.X(i) for i in self.pop]
    def ef(self,i):     return sum(1 for j in self.pop if self.X(j)==self.C[i-1] and i>0)
    def efC(self,i):    return sum(self.ef(j) for j in range(1,i+1))
    def fr(self,i):     return (self.ef(i)/len(self.pop) if i>0 else 0)
    def frC(self,i):    return sum(self.fr(j) for j in range(1,i+1))
    def mode(self):     return [self.C[i-1] for i in range(0,len(self.C)) if self.ef(i)==max([self.ef(j) for j in range(1,len(self.C)+1)])]
    def med(self):      return self.quan(2)[0]
    def moy(self):      return sum(i for i in self.serie())/len(self.pop)
    def etnd(self):     return max(i for i in self.serie())-min(i for i in self.serie())
    def quan(self,r,a=[]):#,l=[]):
        l=[]
        s=sorted(self.serie())
        for i in range(r-1):
            print(s)
            print(l)
            print(len(s),r-i,len(s)/(r-i),len(s)//(r-i),s[len(s)//r-i],s[13//2])
            print(s[len(s)//r-i],(s[len(s)//r-i]+s[len(s)//r-i-1])/2)
            m=(s[len(s)//r-i] if len(s)%r-i!=0 else (s[len(s)//r-i]+s[len(s)//r-i-1])/2)
            l.append(float(m))
            s=[i for i in s if i>m]
        # for i in s:self.quan(r/2,i,l) if r/2!=1 else None
        return sorted(list(dict.fromkeys(l)))
        # print(r)
        # if not s:
        #     s=sorted(self.serie())
        # if r%2==0:
        #     m=(s[len(s)//2] if len(s)%2!=0 else (s[len(s)//2]+s[len(s)//2-1])/2)
        #     l.append(float(m))
        #     s=[[i for i in s if i<m],[i for i in s if i>m]]
        #     print(s)
        #     print(l)
        #     for i in s:self.quan(r/2,i,l) if r/2!=1 else None
        # else:print('odd')
        # return sorted(list(dict.fromkeys(l)))
 
# def f(x):return (True if x%2==0 else False)
# def g(x):return (x+6)%5
# def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
z={i:randint(0,10) for i in range(20)}
def m(x):return [j for i,j in enumerate([i*10 for i in range(50)]) if i==x][0]
def k(x):return (x**3+3*x**2 if x<=0 else (x**(-1) if x<4 else x**2-7/2*x))
def p(x):return z[x]
exemple=Stat(tuple([i for i in range(20)]),p)
# print(exemple.pop)
# print(exemple.serie())
# print(exemple.C)
# print(exemple.ef(4))
# print(exemple.efC(5))
# print(exemple.ef(0))
# print(exemple.efC(len(exemple.C))==len(exemple.pop))
# print(exemple.fr(4))
# print(exemple.frC(5))
# print(exemple.fr(0))
# print(exemple.frC(len(exemple.C))==1)
# print(exemple)
# print(exemple.mode())
# print(exemple.med())
# print(exemple.moy())
# print(exemple.etnd())
print(exemple.quan(3))