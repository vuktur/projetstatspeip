from math import exp
from math import sin
from fractions import Fraction

class Stat():
    def __init__(self,population,*statistiques):
        self.O=population
        self.X=statistiques[0]
        self.C=tuple(sorted(list(dict.fromkeys(self.serie())))) #modalitées
    def __repr__(self): return f"valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.C])}\neffectif |{'|'.join([' '*(len(str(Fraction(self.C[i-1]).limit_denominator()))-1)+str(self.ef(i)) for i in range(1,len(self.C)+1)])}"
    #return f"{{ {self.X.__name__} : {(self.O if len(self.O)<10 else 'pop.')} -> {(self.C if len(self.C)<10 else 'mod.')}\n{{ {' '*(len(self.X.__name__)+2)} w -> {self.X.__name__}(w)"
    def serie(self):    return [self.X(i) for i in self.O]
    def ef(self,i):     return sum(1 for j in self.O if self.X(j)==self.C[i-1] and i>0)
    def efC(self,i):    return sum(self.ef(j) for j in range(1,i+1))
    def fr(self,i):     return (self.ef(i)/len(self.O) if i>0 else 0)
    def frC(self,i):    return sum(self.fr(j) for j in range(1,i+1))
    def mode(self):pass
# def f(x):return (True if x%2==0 else False)
# def g(x):return (x+6)%5
# def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
def k(x):return (x**3+3*x**2 if x<=0 else (x**(-1) if x<4 else x**2-7/2*x))

exemple=Stat(tuple([i for i in range(-5,6)]),k)

print(exemple.serie())
print(exemple.C)

print(exemple.ef(4))
print(exemple.efC(5))
print(exemple.ef(0))
print(exemple.efC(len(exemple.C))==len(exemple.O))

print(exemple.fr(4))
print(exemple.frC(5))
print(exemple.fr(0))
print(exemple.frC(len(exemple.C))==1)

print(exemple)