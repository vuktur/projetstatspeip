from fractions import Fraction
import numpy as np
# from math import sqrt
# from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt

class Stat():
    def __init__(self,statistique,populationStart=0,populationStop=10,populationStep=1):
        # au lieu de nbObservations , jai mis start stop step pour pouvoir faire par exemple entre -50 et 50 de 10 en 10... 
        self.serie=[] # jai remplace self.x par un truc plus explicite
        if (isinstance(statistique,tuple)): 
        #si statistique est un tuple, contenant deux statistiques (x et y) appeller stats doubles...
            pass
        if(isinstance(statistique,list)):
            # si la statistique est une liste de valeurs... 
            if(populationStop==None):populationStop=len(statistique)
            self.serie=statistique
        elif(callable(statistique)): # si la stat est une fonction
            try:self.serie=[statistique(i) for i in np.arange(populationStart,populationStop,populationStep)]
            except:raise
        self.pop=np.arange(populationStart,populationStop,populationStep).tolist()
        self.N=len(np.arange(populationStart,populationStop,populationStep))
        if isinstance(self.serie[0],list): 
            self.moda=sorted(list(dict.fromkeys((tuple(i) for i in self.serie))))
        # <- si les membres de la stat sont des classes
        # else: self.moda=sorted(list(dict.fromkeys(self.serie))) # <- modalites
        else: 
            self.moda=[]
            for i in self.serie:
                if i not in self.moda :
                    self.moda.append(i)
            self.moda.sort()
    def effectif(self,n): return ( self.serie.count(self.moda[n-1]) if n>0 else 0 )
    # renvoie l'effectif d'une certaine valeur
    def effectifCumule(self,n): return sum(self.effectif(i) for i in range(1,n+1))
    # fait la somme des effectifs pour les valeurs inferieures ou egales
    def frequence(self,n): return ( self.effectif(n)/self.N if n>0 else 0 )
    # renvoie la frequence a laquelle aparait une valeur donnee
    def frequenceCumule(self,n): return sum(self.frequence(i) for i in range(1,n+1))
    # fait le somme des frequences pour les valeurs inferieures ou egales
    def mode(self):
        m=[]
        maximum=max([self.effectif(j+1) for j in range(len(self.moda))])
        for i in range(len(self.moda)):
            if self.effectif(i+1)==maximum:
                m.append(self.moda[i])
        if len(m)==1:return m[0]
        else:return m
    # renvoie la valeur la plus fréquente
    def med(self):      return self.quan(2)[0]
            # l=len(self.serie())
            # s=sorted(self.serie())
            # return (s[l//2] if l%2!=0 else (s[l//2]+s[l//2-1])/2)
        # med renvoie la médiane : la valeur de la serie telle qu'il y a autant de valeurs 
        # d'un cote que de l'autre (suivie d'une autre facon, sans utiliser les quantiles)
    def quan(self,n):#return Stat.staticQuan(self.serie,n)
        q=[]
        s=sorted(self.serie)
        if(self):
            for i in range(1,n):
                a=(i*len(s)/n)
                b=(a-a%.5+.5 if (a%.5<.25 if a>len(s)/2 else a%.5<=.25) else a-a%.5+1)
                q.append(s[int(b)-1] if b%1==0 else (s[int(b)]+s[int(b)-1])/2)
        return q




    def __repr__(self):return(
        f"Valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.moda])}\n"+
        f"Effectif |{'|'.join([' '*(len(str(Fraction(self.moda[i-1]).limit_denominator()))-1)+str(self.ef(i)) for i in range(1,len(self.moda)+1)])}\n\n"+
        f"Moyenne : {self.moy()} , Mode : {self.mode()} , Médiane : {self.med()}\nVariance : {self.variance()} , Ecart-type : {self.ecarttyp()} , Etendue : {self.etendue()}\nCourbe : {self.apla()} , Distribution : {self.asym()}")
        # repr renvoie lors du print un tableau avec les modalites dans l'ordre croissant
        # et leur effectif.
    def __iter__(self): 
        yield from self.serie
    def __getitem__(self,n):
        return self.serie[n]
    def __enter__(self):
        return self
    def __exit__(self,*args):
        del self
        return True