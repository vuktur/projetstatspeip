from math import pi, sqrt, exp
from fractions import Fraction
from random import randint
# import statistics
# from decimal import Decimal, ROUND_HALF_UP

class Stat():
    def __init__(self,population,statistique):
        self.pop=population
        self.N=len(self.pop)
        self.X=statistique
        self.v=[self.X(i) for i in self.pop]
        self.C=sorted(list(dict.fromkeys(self.v))) #modalitées
    def __repr__(self): 
        return(
            f"Valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.C])}\n"+
            f"Effectif |{'|'.join([' '*(len(str(Fraction(self.C[i-1]).limit_denominator()))-1)+str(self.ef(i)) for i in range(1,len(self.C)+1)])}\n\n"+
            f"Moyenne : {self.moy()}\nEcart-type : {self.ecarttyp()}\n")
    def serie(self):    return [self.X(i) for i in self.pop]
    def ef(self,n):     return sum(1 for i in self.pop if self.X(i)==self.C[n-1] and n>0)
    def efC(self,n):    return sum(self.ef(i) for i in range(1,n+1))
    def fr(self,n):     return (self.ef(n)/self.N if n>0 else 0)
    def frC(self,n):    return sum(self.fr(i) for i in range(1,n+1))
    def mode(self):     return [self.C[i-1] for i in range(0,len(self.C)) if self.ef(i)==max([self.ef(j) for j in range(1,len(self.C)+1)])]
    def med(self):      return self.quan(2)[0]
        # l=len(self.serie())
        # s=sorted(self.serie())
        # return (s[l//2] if l%2!=0 else (s[l//2]+s[l//2-1])/2)
    def moy(self):      return sum(i for i in self.v)/self.N
    def etendue(self):  return max(i for i in self.v)-min(i for i in self.v)
    def quan(self,n):
        q=[]
        s=sorted(self.v)
        for i in range(1,n):
            a=(i*len(s)/n)
            b=(a-a%0.5+0.5 if (a%0.5<0.25 if a>len(s)/2 else a%0.5<=0.25) else a-a%0.5+1)
            print(b)
            q.append(s[int(b)-1] if b%1==0 else (s[int(b)]+s[int(b)-1])/2)
        return q 
    def ecartary(self): return sum(abs(i-self.moy()) for i in self.v)/self.N
    def variance(self): return sum((i-self.moy())**2 for i in self.v)/self.N
    def ecarttyp(self): return sqrt(abs(self.variance()))
    def moment(self,k): return sum(i**k for i in self.v)/self.N
    def momentcentre(self,k): return sum((i-self.moy())**k for i in self.v)/self.N
    def asymetrie(self): return (self.momentcentre(3)/self.ecarttyp()**3)
    def aplatissement(self): return (self.momentcentre(4)/self.ecarttyp()**4)


def test():
    # def f(x):return (True if x%2==0 else False)
    # def g(x):return (x+6)%5
    # def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
    # z={i:randint(0,10) for i in range(100)} 
    # z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175,164]
    # z=[130,140,170,160,136,165,130,135,140,135,161,136,180,190,141,132,165,168,182,177,172,168,175,181,173,169,178,179,175]
    z=[randint]
    # def m(x):return [j for i,j in enumerate([i*10 for i in range(50)]) if i==x][0]
    # def k(x):return (x**3+3*x**2 if x<=0 else (x**(-1) if x<4 else x**2-7/2*x))
    def p(x):return z[x]
    # def gauss(x,u=,o): return exp(-(x**2)/2)/sqrt(2*pi)
    w=[round(float(str(i)+'.'+str(j))-3,1) for i in range(7) for j in range(10)][:-9]
    exemple=Stat([i for i in range(len(z))],p)

    print(exemple)
    # print(exemple.v)
    # print(sorted(exemple.v))
    # print(exemple.ecartary())
    # print(exemple.variance())
    # print(exemple.ecarttyp())
    # print(exemple.med())
    # print(exemple.quan(3))
    # print(exemple.quan(4))
    # print(exemple.moment(2))
    # print(exemple.momentcentre(2))
    # print(exemple.moment(0),exemple.momentcentre(0))
    # print(exemple.momentcentre(1))
    # print(exemple.moment(1),exemple.moy())
    # print(exemple.momentcentre(2),exemple.variance(),exemple.moment(2)-exemple.moment(1)**2)
    # print(exemple.asymetrie(),exemple.aplatissement())
if __name__=='__main__':test()