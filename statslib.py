from fractions import Fraction
import numpy as np
# from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt

class Stat():
    def __init__(self,stat,pStart=0,pStop=None,pStep=1):
        self.serie=[]
        if isinstance(stat,tuple):
            raise DoubleTryError()
        if(isinstance(stat,list)):
            if(pStop==None):pStop=len(stat)
            self.serie=stat
        elif(callable(stat)):
            try:self.serie=[stat(i) for i in np.arange(pStart,pStop,pStep)]
            except:raise
        self.population=np.arange(pStart,pStop,pStep).tolist()
        self.N=len(np.arange(pStart,pStop,pStep))
        self.modalites=sorted(list(dict.fromkeys(self.serie)))
        self.mode=self.modeFunction()
        self.mediane=self.quantile(2)[0]
        self.moyenne=self.moment(1)
        self.etendue=max(self.serie)-min(self.serie)
        self.ecartMoyen=sum(abs(i-self.moment(1)) for i in self.serie)/self.N
        self.variance=self.momentCentre(2)
        self.ecartType=abs(self.variance)**(1/2)
    def __repr__(self):return(
        f"Valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.modalites])}\n"+
        f"Effectif |{'|'.join([' '*(len(str(Fraction(self.modalites[i-1]).limit_denominator()))-1)+str(self.effectif(i)) for i in range(1,len(self.modalites)+1)])}\n\n"+
        f"Moyenne : {self.moyenne} , Mode : {self.mode} , Médiane : {self.mediane}\nVariance : {self.variance} , Ecart-type : {self.ecartType} , Etendue : {self.etendue}\nCourbe : {self.aplatissement()} , Distribution : {self.asymetrie()}")
        # repr renvoie lors du print un tableau avec les modalites dans l'ordre croissant
        # et leur effectif.
    def __iter__(self): yield from self.serie
    def __getitem__(self,n): #return self.serie[n]
        try: return self.serie[n]
        except: pass
    def __enter__(self): return self
    def __exit__(self,*args):
        del self
        return True
    def effectif(self,n):     return sum(1 for i in self.serie if i==self.serie[n-1] and n>0)
        # effectif renvoie l'effectif d'une certaine valeur
    def effectifC(self,n):    return sum(self.effectif(i) for i in range(1,n+1))
        # effectifC fait la somme des effectifs pour les valeurs inferieures ou egales
    def frequence(self,n):     return (self.effectif(n)/self.N if n>0 else 0)
        # frequence renvoie la frequence a laquelle aparait une valeur donnee
    def frequenceC(self,n):    return sum(self.frequence(i) for i in range(1,n+1))
        # frequenceC fait le somme des frequences pour les valeurs inferieures ou egales
    def modeFunction(self):
        m=[self.modalites[i] for i in range(len(self.modalites)) if self.effectif(i+1)==max([self.effectif(j+1) for j in range(len(self.modalites))])]
        if len(m)==1:   return m[0]
        else:           return m
        # mode renvoie la valeur la plus fréquente
    def quantile(self,n): 
        q=[]
        s=sorted(self.serie)
        if(self):
            for i in range(1,n):
                a=(i*len(s)/n)
                b=(a-a%.5+.5 if (a%.5<.25 if a>len(s)/2 else a%.5<=.25) else a-a%.5+1)
                q.append(s[int(b)-1] if b%1==0 else (s[int(b)]+s[int(b)-1])/2)
        return q
        # quantile renvoie les quantiles d'ordre n : les valeurs séparant la série en n parties
        # de meme effectif
    # NB : apres des recherches, pour obtenir le meme resultat que les methodes de scipy et 
    # statistics, il faudrait appliquer un facteur de correction de n/(n-1) pour eviter
    # des erreurs s'accumulant a chaque iterations : 
    def variance2(self): return sum(((i-self.moment(1))**2)*(self.N/(self.N-1)) for i in self.serie)/self.N
    def ecarttyp2(self): return (abs(self.variance2()))**(1/2)
    # corrigés a n/(n-1)
    def moment(self,k):    return sum(i**k for i in self.serie)/self.N
        # moment donne le moment d'ordre k, une autre valeur de disperssion
    def momentCentre(self,k): return sum((i-self.moment(1))**k for i in self.serie)/self.N
        # momentCentre donne le moment centre d'ordre k, cette fois ci autour de la moyenne
    def asymetrie(self):     return (self.momentCentre(3)/self.momentCentre(2)**(3/2))
        # asymetrie donne le coefficient d'asymetrie (skewness)
    def aplatissement(self):     return (self.momentCentre(4)/self.momentCentre(2)**2)
        # aplatissement donne le coefficient d'aplatissement (kurtosis)
    def classer(self,claScope=[]): 
        claScope=sorted(claScope)
        claList=[[j for j in sorted(self.serie) if (claScope[i]<=j<=claScope[i+1] if i==0 else claScope[i]<j<=claScope[i+1])] for i in range(len(claScope)-1)] # str(Fraction(self.serie[j]).limit_denominator()) 
        return StatCla(claList,claScope=claScope)
        # classer renvoie une instance de la classe Cla, derivee de la classe Stat, ou la serie est constituee 
        # des classes delimitees par les arguments *args de la fonction

class StatCla(Stat):
    def __init__(self,stat,pStart=0,pStop=None,pStep=1,claScope=[]):
        super(StatCla,self).__init__(stat,pStart=0,pStop=None,pStep=1)
        self.modalites=sorted(list(dict.fromkeys((tuple(i) for i in self.serie))))
        self.claScope=claScope
        self.widths=[self.claScope[i+1]-self.claScope[i] for i in range(len(self.claScope)-1)]
        self.heights=[self.effectif(i+1)/self.widths[i] for i in range(len(self.serie))]
    def effectif(self,n):      return len(self.serie[n-1])
    def mode(self):      return max(self.heights)
    def claMod(self):    return [self.serie[i] for i in range(len(self.serie)) if self.heights[i]==self.mode()]
    def depo(self):
        l=[]
        for i in self.serie:
            with Stat(i) as inst:
                l.append(inst.mediane())
        return l
    def histogram(self):
        plt.bar([(self.claScope[i+1]+self.claScope[i])/2 for i in range(len(self.claScope)-1)],height=self.heights,width=self.widths,color='#4287f5',edgecolor='#0041a8',linewidth=1,alpha=.7)
        plt.grid(axis='y',alpha=.7)
        plt.xticks(np.arange(min(self.claScope)-2,max(self.claScope)+3,1))#max(self.effectif(i+1)/max(len(j) for j in self.serie) for i in range(len(self.serie)))])
        plt.show()

class DoubleTryError(Exception):
    def __init__(self):
        super().__init__("You can use StatDbl instead of Stat to analyse two stats at the time")
class OnlyTwoError(Exception):
    def __init__(self):
        super().__init__("You only can analyse two stats at the time for now...")
# class DifferentType(Exception):
#     def __init__(self):
#         super().__init__("The two stats must be of the same type (two functions or two lists)")
class DifferentLenghError(Exception):
    def __init__(self):
        super().__init__("The two lists must have the same size...")

class StatDbl():
    def __init__(self,stat,pStart=0,pStop=None,pStep=1):
        if len(stat)>2: raise OnlyTwoError()
        if len(stat[0])!=len(stat[1]): raise DifferentLenghError()
        self.serie=(Stat(stat[0],pStart,pStop,pStep),Stat(stat[1],pStart,pStop,pStep))
        self.N=self.serie[0].N
    def effectif(self,m='.',n='.'): 
        return sum(1 
                    for i in range(self.N) 
                    if all([
                        (m=='.' or (self.serie[0][i]==self.serie[0][m-1] and m>0)), 
                        (n=='.' or (self.serie[1][i]==self.serie[1][n-1] and n>0))
                    ])
                )
        # effectif renvoie l'effectif d'un certain couple
    # def effectifC(self,m='.',n='.'):    return sum(self.effectif(i) for i in range(1,n+1))
        # effectifC fait la somme des effectifs pour les valeurs inferieures ou egales
    def frequence(self,m='.',n='.'):     return self.effectif(m,n)/self.N
        # frequence renvoie la frequence a laquelle aparait une valeur donnee
    # def frequenceC(self,m='.',n='.'):    return sum(self.frequence(i) for i in range(1,n+1))
        # frequenceC fait le somme des frequences pour les valeurs inferieures ou egales
    def contingence(self):
        data=[[self.effectif(i,j) for j in range(1,self.N+1)]+[self.effectif(i,'.')] for i in range(1,self.N+1)]+[[self.effectif('.',j) for j in range(1,self.N+1)]+[self.N]]
        print(data)
        text=[[f"{j}" for j in i] for i in data]
        print(text)
        rows=[f'{i}' for i in self.serie[0]]+['t']
        columns=[f'{j}' for j in self.serie[1]]+['t']
        colors=plt.cm.YlOrRd(np.linspace(0,0.5,max(max(data))+1))
        colorsmap=[[colors[data[j]] for j in range(len(data[i]))] for i in range(len(data))]
        plt.table(cellText=text,
                  rowLabels=rows,
                  colLabels=columns,
                  cellColours=colorsmap,
                  loc='center'
                 )
        plt.axis('off')
        plt.show()
    def covariance(self):
        pass
    def correlation(self):
        pass