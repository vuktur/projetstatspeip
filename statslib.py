class Stat():
    def __init__(self,population,statistique,modalites=None):
        self.O=population
        self.X=statistique
        self.C=modalites
    def __repr__(self):
        return f"{{ {self.X.__name__} : {(self.O if len(self.O)<10 else 'pop.')} -> {(self.C if len(self.C)<10 and self.C!=None else 'mod.')}\n{{ {' '*(len(self.X.__name__)+2)} w -> {self.X.__name__}(w)"
    def test(self):return [self.X(i) for i in self.O]
    def effectif(self,i):return sum(1 for j in self.O if self.X(j)==self.C[i])
    def effectifCummule(self,i):return sum(self.effectif(j) for j in range(0,i))

def f(x):return (True if x%2==0 else False)
div2=Stat((1,2,3,4,5,6,7,8,9),f,(True,False))
print(div2)
print(div2.effectif(0))
print(div2.effectif(1))

def g(x):return (x+6)%10
exemple=Stat((1,2,3,4,5,6,7,8,9),g)
print(exemple.test())