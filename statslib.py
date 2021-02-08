from fractions import Fraction
# from decimal import Decimal, ROUND_HALF_UP

class Stat():
    def __init__(self,statistique,population):
        self.pop=population
        self.N=len(self.pop)
        self.X=statistique
        self.serie=[self.X(i) for i in self.pop]
        self.moda=sorted(list(dict.fromkeys(self.serie))) # <- modalites
    # repr renvoie lors du print un tableau avec les modalites dans l'ordre croissant
    # et leur effectif.
    def __repr__(self): 
        return(
            f"Valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.moda])}\n"+
            f"Effectif |{'|'.join([' '*(len(str(Fraction(self.moda[i-1]).limit_denominator()))-1)+str(self.ef(i)) for i in range(1,len(self.moda)+1)])}\n\n"+
            f"Moyenne : {self.moy()}\nEcart-type : {self.ecarttyp()}\n")
    # ef renvoie l'effectif d'une certaine valeur
    def ef(self,n):     return sum(1 for i in self.pop if self.X(i)==self.moda[n-1] and n>0)
    # efC fait la somme des effectifs pour les valeurs inferieures ou egales
    def efC(self,n):    return sum(self.ef(i) for i in range(1,n+1))
    # fr renvoie la frequence a laquelle aparait une valeur donnee
    def fr(self,n):     return (self.ef(n)/self.N if n>0 else 0)
    # frC fait le somme des frequences pour les valeurs inferieures ou egales
    def frC(self,n):    return sum(self.fr(i) for i in range(1,n+1))
    # mode renvoie la valeur la plus fréquente
    def mode(self):     return [self.moda[i-1] for i in range(0,len(self.moda)) if self.ef(i)==max([self.ef(j) for j in range(1,len(self.moda)+1)])]
    # med renvoie la médiane : la valeur de la serie telle qu'il y a autant de valeurs 
    # d'un cote que de l'autre (suivie d'une autre facon, sans utiliser les quantiles)
    def med(self):      return self.quan(2)[0]
        # l=len(self.serie())
        # s=sorted(self.serie())
        # return (s[l//2] if l%2!=0 else (s[l//2]+s[l//2-1])/2)
    # quan renvoie les quantiles d'ordre n : les valeurs séparant la série en n parties
    # de meme effectif
    def quan(self,n):
        q=[]
        s=sorted(self.serie)
        for i in range(1,n):
            a=(i*len(s)/n)
            b=(a-a%0.5+0.5 if (a%0.5<0.25 if a>len(s)/2 else a%0.5<=0.25) else a-a%0.5+1)
            q.append(s[int(b)-1] if b%1==0 else (s[int(b)]+s[int(b)-1])/2)
        return q
    # moy rnevoie la moyenne arithmetique de la serie : la somme des valeurs divisee 
    # par la taille de l'echantillon
    def moy(self):      return sum(i for i in self.serie)/self.N
    # etendue renvoie l'ecart entre la plus petite et la plus grande valeur de la serie
    def etendue(self):  return max(i for i in self.serie)-min(i for i in self.serie)
    # def quandis(self,p):return self.quanUnsorted(100)[p-100]
    # ecartmoy renvoie l'ecart moyen : la dispersion des valeurs autour de la moyenne
    def ecartmoy(self): return sum(abs(i-self.moy()) for i in self.serie)/self.N
    # variance donne la variance de la serie : 
    def variance(self): return sum((i-self.moy())**2 for i in self.serie)/self.N
    def ecarttyp(self): return (abs(self.variance()))**(1/2)
    def mmt(self,k):    return sum(i**k for i in self.serie)/self.N
    def mmtctr(self,k): return sum((i-self.moy())**k for i in self.serie)/self.N
    def asym(self):     return (self.mmtctr(3)/self.ecarttyp()**3)
    def apla(self):     return (self.mmtctr(4)/self.ecarttyp()**4)
