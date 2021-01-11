from math import exp
from math import sin
from typing import NoReturn

class Stat():
    def __init__(self,population,*statistiques):
        self.O=population
        self.X=statistiques[0]
        self.C=tuple(sorted(list(dict.fromkeys(self.all())))) #modalitées
    def __repr__(self):return f"{{ {self.X.__name__} : {(self.O if len(self.O)<10 else 'pop.')} -> {(self.C if len(self.C)<10 else 'mod.')}\n{{ {' '*(len(self.X.__name__)+2)} w -> {self.X.__name__}(w)"
    def all(self):return [self.X(i) for i in self.O]
    def n(self,i):return sum(1 for j in self.O if self.X(j)==self.C[i-1] and i>0)
    def N(self,i):return sum(self.n(j) for j in range(1,i+1))
    def freq(self,i):return self.n(i)/self.N(i)

# def f(x):return (True if x%2==0 else False)
# def g(x):return (x+6)%5
def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
exemple=Stat(tuple([i for i in range(-5,6)]),h)
print(exemple.all())
print(exemple.C)
print(exemple.n(4))
print(exemple.N(5))
print(exemple.n(0))
print(exemple.N(len(exemple.C))==len(exemple.O))
print(exemple.freq(1))
