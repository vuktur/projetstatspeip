from math import exp
from math import sin
from fractions import Fraction

class Stat():
    def __init__(self,population,*statistiques):
        self.O=population
        self.X=statistiques[0]
        self.C=tuple(sorted(list(dict.fromkeys(self.serie())))) #modalitées
    def __repr__(self): 
        return(
            f"Valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.C])}\n"+
            f"Effectif |{'|'.join([' '*(len(str(Fraction(self.C[i-1]).limit_denominator()))-1)+str(self.ef(i)) for i in range(1,len(self.C)+1)])}"
            )
    def serie(self):    return [self.X(i) for i in self.O]
    def ef(self,i):     return sum(1 for j in self.O if self.X(j)==self.C[i-1] and i>0)
    def efC(self,i):    return sum(self.ef(j) for j in range(1,i+1))
    def fr(self,i):     return (self.ef(i)/len(self.O) if i>0 else 0)
    def frC(self,i):    return sum(self.fr(j) for j in range(1,i+1))
    def mode(self):     return [self.C[i-1] for i in range(0,len(self.C)) if self.ef(i)==max([self.ef(j) for j in range(1,len(self.C)+1)])]
    def med(self):      return self.quan(2)
        # l=len(self.serie())
        # s=sorted(self.serie())
        # return (s[l//2] if l%2!=0 else (s[l//2]+s[l//2-1])/2)
    def quan(self,r,a=[],l=[]):
        print(r)
        if not a:
            a=sorted(self.serie())
        if r%2==0:
            m=(a[len(a)//2] if len(a)%2!=0 else (a[len(a)//2]+a[len(a)//2-1])/2)
            l.append(float(m))
            a=[[i for i in a if i<m],[i for i in a if i>m]]
            print(a,l)
            for i in a:self.quan(r/2,i,l) if r/2!=1 else None
        return sorted(l)
        # else:print('odd')
    # def quan(self,r):
    #     r-=2
    #     a=[i for i in sorted(self.serie()) if i<self.med()]
    #     b=[i for i in sorted(self.serie()) if i>self.med()]
    #     if r==0:pass


# def f(x):return (True if x%2==0 else False)
# def g(x):return (x+6)%5
# def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
def l(x):return [j for i,j in enumerate([10,20,30,40]) if i==x][0]
def m(x):return [j for i,j in enumerate([i*10 for i in range(50)]) if i==x][0]
def k(x):return (x**3+3*x**2 if x<=0 else (x**(-1) if x<4 else x**2-7/2*x))
exemple=Stat(tuple([i for i in range(0,32)]),m)
# print(exemple.serie())
# print(exemple.C)
# print(exemple.ef(4))
# print(exemple.efC(5))
# print(exemple.ef(0))
# print(exemple.efC(len(exemple.C))==len(exemple.O))
# print(exemple.fr(4))
# print(exemple.frC(5))
# print(exemple.fr(0))
# print(exemple.frC(len(exemple.C))==1)
print(exemple)
# print(exemple.mode())
# print(exemple.med())
print(exemple.quan(4))