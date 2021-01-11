class Stat():
    def __init__(self,population,statistique,modalites):
        self.O=population
        self.X=statistique
        self.C=modalites
    def __repr__(self):
        return f"{{ {self.X.__name__} : {(self.O if len(self.O)<10 else 'pop.')} -> {(self.C if len(self.C)<10 else 'mod.')}\n{{ {' '*(len(self.X.__name__)+2)} w -> {self.X.__name__}(w)"
    
    def effectif(self,i):
        return sum(1 for j in self.O if self.X(j)==self.C[i])
def f(a):return (True if a%2==0 else False)
newstat=Stat((1,2,3,4,5,6,7,8,9),f,(False,True))
print(newstat)
print(newstat.effectif(0))
print(newstat.effectif(1))