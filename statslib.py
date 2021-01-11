class Stat():
    def __init__(self,population,statistique,modalites):
        self.O=population
        self.X=statistique
        self.C=modalites
    def __repr__(self):
        return f"{{ {self.X.__name__} : {(self.O if len(self.O)<10 else 'pop.')} -> {(self.C if len(self.C)<10 else 'mod.')}\n{{ {' '*(len(self.X.__name__)+2)} w -> {self.X.__name__}(w)"
    def effectif(self):
        pass
def f(a):return (1 if a%2==0 else 0)
newstat=Stat((1,2,3,4,5,6,7,8,9),f,(0,1))
print(newstat)