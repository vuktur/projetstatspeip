from fractions import Fraction
import numpy as np
# from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt

class Stat():
    def __init__(self,stat,pStart=0,pStop=None,pStep=1):
        self.serie=[]
        if isinstance(stat,tuple) and (isinstance(stat[0],list) or callable(stat[0])):
            self.createDouble(stat,pStart,pStop,pStep)
        if(isinstance(stat,list)):
            if(pStart==None):pStart=0
            if(pStop==None):pStop=len(stat)
            self.serie=stat
        elif(callable(stat)):
            try:self.serie=[stat(i) for i in np.arange(pStart,pStop,pStep)]
            except:raise
        self.pop=np.arange(pStart,pStop,pStep).tolist()
        self.N=len(np.arange(pStart,pStop,pStep))
        self.moda=sorted(list(dict.fromkeys(self.serie))) # <- modalites
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
    def ef(self,n):     return sum(1 for i in self.serie if i==self.moda[n-1] and n>0)
        # ef renvoie l'effectif d'une certaine valeur
    def efC(self,n):    return sum(self.ef(i) for i in range(1,n+1))
        # efC fait la somme des effectifs pour les valeurs inferieures ou egales
    def fr(self,n):     return (self.ef(n)/self.N if n>0 else 0)
        # fr renvoie la frequence a laquelle aparait une valeur donnee
    def frC(self,n):    return sum(self.fr(i) for i in range(1,n+1))
        # frC fait le somme des frequences pour les valeurs inferieures ou egales
    def mode(self):
        m=[self.moda[i] for i in range(len(self.moda)) if self.ef(i+1)==max([self.ef(j+1) for j in range(len(self.moda))])]
        if len(m)==1:return m[0]
        else:return m
        # mode renvoie la valeur la plus fréquente
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
    # @staticmethod
    # def staticQuan(liste,n):
    #     q=[]
    #     s=sorted(liste)
    #     for i in range(1,n):
    #         a=(i*len(s)/n)
    #         b=(a-a%.5+.5 if (a%.5<.25 if a>len(s)/2 else a%.5<=.25) else a-a%.5+1)
    #         q.append(s[int(b)-1] if b%1==0 else (s[int(b)]+s[int(b)-1])/2)
    #     return q
            # def quan(self,n):return [(sorted(self.serie)[int(((i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+.5 if ((i*len(sorted(self.serie))/n)%.5<.25 if (i*len(sorted(self.serie))/n)>len(sorted(self.serie))/2 else (i*len(sorted(self.serie))/n)%.5<=.25) else (i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+1))-1] if ((i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+.5 if ((i*len(sorted(self.serie))/n)%.5<.25 if (i*len(sorted(self.serie))/n)>len(sorted(self.serie))/2 else (i*len(sorted(self.serie))/n)%.5<=.25) else (i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+1)%1==0 else (sorted(self.serie)[int(((i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+.5 if ((i*len(sorted(self.serie))/n)%.5<.25 if (i*len(sorted(self.serie))/n)>len(sorted(self.serie))/2 else (i*len(sorted(self.serie))/n)%.5<=.25) else (i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+1))]+sorted(self.serie)[int(((i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+.5 if ((i*len(sorted(self.serie))/n)%.5<.25 if (i*len(sorted(self.serie))/n)>len(sorted(self.serie))/2 else (i*len(sorted(self.serie))/n)%.5<=.25) else (i*len(sorted(self.serie))/n)-(i*len(sorted(self.serie))/n)%.5+1))-1])/2) for i in range(1,n)]
        # quan renvoie les quantiles d'ordre n : les valeurs séparant la série en n parties
        # de meme effectif
    def moy(self):      return self.mmt(1)#sum(i for i in self.serie)/self.N
        # moy rnevoie la moyenne arithmetique de la serie : la somme des valeurs divisee 
        # par la taille de l'echantillon
    def etendue(self):  return max(self.serie)-min(self.serie)
        # etendue renvoie l'ecart entre la plus petite et la plus grande valeur de la serie
    def ecartmoy(self): return sum(abs(i-self.mmt(1)) for i in self.serie)/self.N
        # ecartmoy renvoie l'ecart moyen : la dispersion des valeurs autour de la moyenne
    def variance(self): return self.mmtctr(2)#sum((i-self.mmt(1))**2 for i in self.serie)/self.N
        # variance donne la variance de la serie, utilisee pour calculer l'ecart type
    def ecarttyp(self): return (abs(self.variance()))**(1/2)
        # ecarttyp donne l'ecart type, une mesure de disperssion des valeurs
    # NB : apres des recherches, pour obtenir le meme resultat que les methodes de scipy et 
        # statistics, il faudrait appliquer un facteur de correction de n/(n-1) pour eviter
        # des erreurs s'accumulant a chaque iterations : 
    def variance2(self): return sum(((i-self.mmt(1))**2)*(self.N/(self.N-1)) for i in self.serie)/self.N
    def ecarttyp2(self): return (abs(self.variance2()))**(1/2)
        # corrigés a n/(n-1)
    def mmt(self,k):    return sum(i**k for i in self.serie)/self.N
        # mmt donne le moment d'ordre k, une autre valeur de disperssion
    def mmtctr(self,k): return sum((i-self.mmt(1))**k for i in self.serie)/self.N
        # mmtctr donne le moment centre d'ordre k, cette fois ci autour de la moyenne
    def asym(self):     return (self.mmtctr(3)/self.mmtctr(2)**(3/2))
        # asym donne le coefficient d'asymetrie (skewness)
    def apla(self):     return (self.mmtctr(4)/self.mmtctr(2)**2)
        # apla donne le coefficient d'aplatissement (kurtosis)
    def cla(self,claScope=[]): 
        claScope=sorted(claScope)
        claList=[[j for j in sorted(self.serie) if (claScope[i]<=j<=claScope[i+1] if i==0 else claScope[i]<j<=claScope[i+1])] for i in range(len(claScope)-1)] # str(Fraction(self.serie[j]).limit_denominator()) 
        return StatCla(claList,claScope=claScope)
        # cla renvoie une instance de la classe Cla, derivee de la classe Stat, ou la serie est constituee 
        # des classes delimitees par les arguments *args de la fonction
    def createDouble(self,stat,pStart,pStop,pStep):
        return StatDbl(stat,pStart,pStop,pStep)

class StatCla(Stat):
    def __init__(self,stat,pStart=0,pStop=None,pStep=1,claScope=[]):
        super(StatCla,self).__init__(stat,pStart=0,pStop=None,pStep=1)
        self.moda=sorted(list(dict.fromkeys((tuple(i) for i in self.serie))))
        self.claScope=claScope
        self.widths=[self.claScope[i+1]-self.claScope[i] for i in range(len(self.claScope)-1)]
        self.heights=[self.ef(i+1)/self.widths[i] for i in range(len(self.serie))]
    def ef(self,n):      return len(self.serie[n-1])
    def mode(self):      return max(self.heights)
    def claMod(self):    return [self.serie[i] for i in range(len(self.serie)) if self.heights[i]==self.mode()]
    def depo(self):
        l=[]
        for i in self.serie:
            with Stat(i) as inst:
                l.append(inst.med())
        return l
    def histogram(self):
        plt.bar([(self.claScope[i+1]+self.claScope[i])/2 for i in range(len(self.claScope)-1)],height=self.heights,width=self.widths,color='#4287f5',edgecolor='#0041a8',linewidth=1,alpha=.7)
        plt.grid(axis='y',alpha=.7)
        plt.xticks(np.arange(min(self.claScope)-2,max(self.claScope)+3,1))#max(self.ef(i+1)/max(len(j) for j in self.serie) for i in range(len(self.serie)))])
        plt.show()

class OnlyTwoStatsError(Exception):
    def __init__(self):
        super().__init__("You only can analyse two stats at the time for now...")

class StatDbl():
    def __init__(self,stat,pStart,pStop,pStep):
        if len(stat)>2: raise OnlyTwoStatsError()
        else