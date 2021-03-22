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
        self.pop=np.arange(pStart,pStop,pStep).tolist()
        self.N=len(np.arange(pStart,pStop,pStep))
        if not isinstance(self.serie[0],list):
            self.moda=sorted(list(dict.fromkeys(self.serie)))
            self.mode=self.modeF()
            self.median=self.quantile(2)[0]
            self.mean=self.mmt(1)
            self.size=max(self.serie)-min(self.serie)
            self.meanDev=sum(abs(i-self.mmt(1)) for i in self.serie)/self.N
            self.var=self.mmtCentral(2)
            self.stdDev=abs(self.var)**(1/2)
    def __repr__(self):return(
        f"Valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.moda])}\n"+
        f"Effectif |{'|'.join([' '*(len(str(Fraction(self.moda[i-1]).limit_denominator()))-1)+str(self.count(i)) for i in range(1,len(self.moda)+1)])}\n\n"+
        f"Moyenne : {self.mean} , Mode : {self.mode} , Médiane : {self.median}\nVariance : {self.var} , Ecart-type : {self.stdDev} , Etendue : {self.size}\nCourbe : {self.kurtosis()} , Distribution : {self.skewness()}")
    def __iter__(self): yield from self.serie
    def __getitem__(self,n): 
        try: return self.serie[n]
        except: pass
    def __enter__(self): return self
    def __exit__(self,*args):
        del self
        return True
    def count(self,n):     return sum(1 for i in self.serie if i==self.serie[n-1] and n>0)
    def countC(self,n):    return sum(self.count(i) for i in range(1,n+1))
    def freq(self,n):     return (self.count(n)/self.N if n>0 else 0)
    def freqC(self,n):    return sum(self.freq(i) for i in range(1,n+1))
    def modeF(self):
        if isinstance(self.serie[0],list): return None
        m=[self.moda[i] for i in range(len(self.moda)) if self.count(i+1)==max([self.count(j+1) for j in range(len(self.moda))])]
        if len(m)==1:   return m[0]
        else:           return m
    def quantile(self,n): 
        if isinstance(self.serie[0],list): return None
        q=[]
        s=sorted(self.serie)
        if(self):
            for i in range(1,n):
                a=(i*len(s)/n)
                b=(a-a%.5+.5 if (a%.5<.25 if a>len(s)/2 else a%.5<=.25) else a-a%.5+1)
                q.append(s[int(b)-1] if b%1==0 else (s[int(b)]+s[int(b)-1])/2)
        return q
    # NB : apres des recherches, pour obtenir le meme resultat que les methodes de scipy et 
    # statistics, il faudrait appliquer un facteur de correction de n/(n-1) pour eviter
    # des erreurs s'accumulant a chaque iterations : 
    # def variance2(self): return sum(((i-self.mmt(1))**2)*(self.N/(self.N-1)) for i in self.serie)/self.N
    # def ecarttyp2(self): return (abs(self.variance2()))**(1/2)
    # corrigés a n/(n-1)
    def mmt(self,k): 
        if isinstance(self.serie[0],list): return None
        return sum(i**k for i in self.serie)/self.N
    def mmtCentral(self,k): return sum((i-self.mmt(1))**k for i in self.serie)/self.N
    def skewness(self):     return (self.mmtCentral(3)/self.mmtCentral(2)**(3/2))
    def kurtosis(self):     return (self.mmtCentral(4)/self.mmtCentral(2)**2)
    def classify(self,bacs=[]): 
        bacs=sorted(bacs)
        claList=[[j for j in sorted(self.serie) if (bacs[i]<=j<=bacs[i+1] if i==0 else bacs[i]<j<=bacs[i+1])] for i in range(len(bacs)-1)] # str(Fraction(self.serie[j]).limit_denominator()) 
        return StatClass(claList,bacs=bacs)

class StatClass(Stat):
    def __init__(self,stat,pStart=0,pStop=None,pStep=1,bacs=[]):
        super(StatClass,self).__init__(stat,pStart=0,pStop=None,pStep=1)
        self.moda=sorted(list(dict.fromkeys((tuple(i) for i in self.serie))))
        self.bacs=bacs
        self.widths=[self.bacs[i+1]-self.bacs[i] for i in range(len(self.bacs)-1)]
        self.heights=[self.count(i+1)/self.widths[i] for i in range(len(self.serie))]
    def count(self,n):      return len(self.serie[n-1])
    def mode(self):      return max(self.heights)
    def modalClass(self):    return [self.serie[i] for i in range(len(self.serie)) if self.heights[i]==self.mode()]
    def depouiller(self):
        l=[]
        for i in self.serie:
            with Stat(i) as inst:
                l.append(inst.median())
        return l
    def histogramme(self):
        plt.bar([(self.bacs[i+1]+self.bacs[i])/2 for i in range(len(self.bacs)-1)],height=self.heights,width=self.widths,color='#4287f5',edgecolor='#0041a8',linewidth=1,alpha=.7)
        plt.grid(axis='y',alpha=.7)
        plt.xticks(np.arange(min(self.bacs)-2,max(self.bacs)+3,1))#max(self.count(i+1)/max(len(j) for j in self.serie) for i in range(len(self.serie)))])
        plt.show()

class DoubleTryError(Exception):
    def __init__(self):
        super().__init__("You can use StatDouble instead of Stat to analyse two stats at the time")
class OnlyTwoError(Exception):
    def __init__(self):
        super().__init__("You only can analyse two stats at the time for now...")
# class DifferentType(Exception):
#     def __init__(self):
#         super().__init__("The two stats must be of the same type (two functions or two lists)")
class DifferentLenghError(Exception):
    def __init__(self):
        super().__init__("The two lists must have the same count...")

class StatDouble():
    def __init__(self,stat,pStart=0,pStop=None,pStep=1):
        if len(stat)>2: raise OnlyTwoError()
        if len(stat[0])!=len(stat[1]): raise DifferentLenghError()
        self.serie=(Stat(stat[0],pStart,pStop,pStep),Stat(stat[1],pStart,pStop,pStep))
        self.N=self.serie[0].N
    def count(self,m='.',n='.'): 
        return sum(1 
                    for i in range(self.N) 
                    if all([
                        (m=='.' or (self.serie[0][i]==self.serie[0][m-1] and m>0)), 
                        (n=='.' or (self.serie[1][i]==self.serie[1][n-1] and n>0))
                    ])
                )
    # def countC(self,m='.',n='.'):    return sum(self.count(i) for i in range(1,n+1))
    def freq(self,m='.',n='.'):     return self.count(m,n)/self.N
    # def freqC(self,m='.',n='.'):    return sum(self.freq(i) for i in range(1,n+1))
    def contingence(self):
        data=[[self.count(i,j) for j in range(1,self.N+1)]+[self.count(i,'.')] for i in range(1,self.N+1)]+[[self.count('.',j) for j in range(1,self.N+1)]+[self.N]]
        text=[[f"{j}" for j in i] for i in data]
        rows=[f'{i}' for i in self.serie[0]]+['.']
        columns=[f'{j}' for j in self.serie[1]]+['.']
        colors=plt.cm.YlOrRd(np.linspace(0,0.5,max(max(i[:-1] for i in data[:-1]))+2))
        colorsmap=[]
        for i in range(len(data)-1):
            colorsmap.append([])
            for j in range(len(data[i])-1):
                colorsmap[i].append(colors[data[i][j]])
            colorsmap[i].append(np.array([1,1,1,1]))
        colorsmap.append([np.array([1,1,1,1]) for _ in range(len(data[0]))])
        plt.table(cellText=text,rowLabels=rows,colLabels=columns,cellColours=colorsmap,loc='center')
        plt.axis('off')
        plt.show()
    def covariance(self,*args): 
        return (sum(
            self.count((i if args==() or 0 in args else '.'),(j if args==() or 1 in args else '.'))*
            (self.serie[0][i]-self.serie[0].mean if args==() or 0 in args else 1)*
            (self.serie[1][j]-self.serie[1].mean if args==() or 1 in args else 1) 
            for j in range(self.N) for i in range(self.N))/self.N)
    def correlation(self): return self.covariance(0,1)/(self.covariance(0)*self.covariance(1))
    def nuage(self): return 
    def regressionLin(self): pass
    def regressionLog(self): pass
    def regressionPoly(self): pass
