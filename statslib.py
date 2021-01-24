from math import sqrt
from fractions import Fraction
from random import randint
import statistics

class Stat():
    def __init__(self,population,statistique):
        self.pop=population
        self.N=len(self.pop)
        self.X=statistique
        self.C=sorted(list(dict.fromkeys(self.serie()))) #modalitées
    def __repr__(self): 
        return(
            f"Valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.C])}\n"+
            f"Effectif |{'|'.join([' '*(len(str(Fraction(self.C[i-1]).limit_denominator()))-1)+str(self.ef(i)) for i in range(1,len(self.C)+1)])}"
            )
    # def moda(self):     return sorted(list(dict.fromkeys(self.serie()))) #modalitées
    def serie(self):    return [self.X(i) for i in self.pop]
    def ef(self,n):     return sum(1 for i in self.pop if self.X(i)==self.C[n-1] and n>0)
    def efC(self,n):    return sum(self.ef(i) for i in range(1,n+1))
    def fr(self,n):     return (self.ef(n)/self.N if n>0 else 0)
    def frC(self,n):    return sum(self.fr(i) for i in range(1,n+1))
    def mode(self):     return [self.C[i-1] for i in range(0,len(self.C)) if self.ef(i)==max([self.ef(j) for j in range(1,len(self.C)+1)])]
    def med(self):      return self.quan(2)[0]
    def moy(self):      return sum(i for i in self.serie())/self.N
    def etendue(self):  return max(i for i in self.serie())-min(i for i in self.serie())
    # def quan(self,r):
    #     l=[]
    #     s=sorted(self.serie())
    #     print(s)
    #     for i in range(r-1):
    #         print(l)
    #         print(len(s)/(r-i),len(s)//(r-i))
    #         print(s[len(s)//(r-i)],(s[len(s)//(r-i)]+s[len(s)//(r-i)-1])/2)
    #         print((len(s)-(r-i)+1)%(r-i))
    #         # l.append(float(s[len(s)//(r-i)] if (len(s)-(r-i)+1)%(r-i)==0 else (s[len(s)//(r-i)]+s[len(s)//(r-i)-1])/2))
    #         l.append(float(s[len(s)//(r-i)] if len(s)//(r-i)+0.5==len(s)/(r-i) else (s[len(s)//(r-i)]+s[len(s)//(r-i)-1])/2))
    #         s=[s[j] for j in range(len(s)) if j>(len(s)//(r-i))]
    #         print(s)
    #     return sorted(list(dict.fromkeys(l)))
    def quan(self,n):
        q=[]
        s=sorted(self.serie())
        # print(s)
        for i in range(1,n):
            # print(s[int(i*(len(s)/n)-0.5)],(s[int(i*(len(s)/n))]+s[int(i*(len(s)/n))-1])/2)
            # if (i*(len(s)/n)-0.5)%1==0: q.append(s[int(i*(len(s)/n)-0.5)])
            # else: q.append((s[int(i*(len(s)/n))]+s[int(i*(len(s)/n))-1])/2)
            # q.append(s[int(i*(len(s)/n)-0.5)] if (i*(len(s)/n)-0.5)%1==0 else (s[int(i*(len(s)/n))]+s[int(i*(len(s)/n))-1])/2)
            pass
        return q
    def ecartary(self): return sum(abs(i-self.moy()) for i in self.serie())/self.N
    def variance(self): return sum((i-self.moy())**2 for i in self.serie())/self.N
    def ecarttyp(self): return sqrt(abs(self.variance()))
    def moment(self,k): return sum(i**k for i in self.serie())/self.N
    def momentcentre(self,k): return sum((i-self.moy())**k for i in self.serie())/self.N
    def coeffasy(self): return (self.momentcentre(3)/self.variance()**3)



def test():
    # def f(x):return (True if x%2==0 else False)
    # def g(x):return (x+6)%5
    # def h(x):return abs((1/2)*(exp(x)+exp(-x))*sin(x))
    z={i:randint(0,10) for i in range(100)} 
    def m(x):return [j for i,j in enumerate([i*10 for i in range(50)]) if i==x][0]
    def k(x):return (x**3+3*x**2 if x<=0 else (x**(-1) if x<4 else x**2-7/2*x))
    def p(x):return z[x]
    exemple=Stat(tuple([i for i in range(10)]),p)
    # print(exemple.quan(4))
    # i=3
    # for j in range(2,50):
    #     if j<i:pass
    #     else:
    #         z={i:randint(0,10) for i in range(100)}
    #         exemple=Stat(tuple([i for i in range(j)]),p)
    #         print(sorted(exemple.serie()))
    #         print(exemple.quan(i))

    # exemple=Stat(tuple([i for i in range(11)]),p)
    # print(sorted(exemple.serie()))
    # print(exemple.quan(3))
    # print(exemple.ecartary())
    # print(exemple.variance())
    # print(exemple.ecarttyp())
    # print(exemple.moment(2))
    # print(exemple.momentcentre(2))
    # print(exemple.moment(0),exemple.momentcentre(0))
    # print(exemple.momentcentre(1))
    # print(exemple.moment(1),exemple.moy())
    # print(exemple.momentcentre(2),exemple.variance())
    # print(exemple.variance(),exemple.moment(2)-exemple.moment(1)**2)
if __name__=='__main__':test()