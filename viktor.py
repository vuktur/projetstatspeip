from fractions import Fraction
import numpy as np
# from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt
from numpy.linalg import LinAlgError
#=================================================================================================================
class Stat():
    def __init__(self,stat,pStart=0,pStop=None,pStep=1):
        self.serie=[]
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
        # f"Valeur   |{'|'.join([str(Fraction(i).limit_denominator()) for i in self.moda])}\n"+
        # f"Effectif |{'|'.join([' '*(len(str(Fraction(i).limit_denominator())))+str(self.count(i)) for i in self.moda])}\n\n"+
        np.array2string(np.array([[i for i in self.moda],[self.count(i) for i in self.moda]]))+'\n'+
        f"Moyenne : {self.mean} , Mode : {self.mode} , Médiane : {self.median}\nVariance : {self.var} , Ecart-type : {self.stdDev} , Etendue : {self.size}\nCourbe : {self.kurtosis()} , Distribution : {self.skewness()}")
    def __iter__(self): yield from self.serie
    def __getitem__(self,n): 
        try: return self.serie[n]
        except: pass
    def __enter__(self): return self
    def __exit__(self,*args):
        del self
        return True
    # def count(self,n):     return sum(1 for i in self.serie if i==n)
    def count(self,n):     return self.serie.count(n)
    def countC(self,n):    return sum(self.count(i) for i in sorted(self.moda) if i<=n)
    def freq(self,n):     return (self.count(n)/self.N)
    def freqC(self,n):    return sum(self.freq(i) for i in sorted(self.moda) if i<=n)
    def modeF(self):
        if isinstance(self.serie[0],list): return None
        m=[i for i in self.moda if self.count(i)==max(self.count(j) for j in self.moda)]
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
#=================================================================================================================
class StatClass(Stat):
    def __init__(self,stat,pStart=0,pStop=None,pStep=1,bacs=[]):
        super().__init__(stat,pStart,pStop,pStep)
        self.moda=sorted(list(dict.fromkeys((tuple(i) for i in self.serie))))
        self.bacs=bacs
        self.widths=[self.bacs[i+1]-self.bacs[i] for i in range(len(self.bacs)-1)]
        self.heights=[self.count(i)/self.widths[i] for i in range(len(self.serie))]
    def __enter__(self): return self
    def __exit__(self,*args):
        del self
        return True
    def count(self,n):      return len(self.serie[n])
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
        plt.xticks(np.arange(min(self.bacs)-2,max(self.bacs)+3,1))
        plt.show()
#=================================================================================================================
class DifferentLenghError(Exception):
    def __init__(self): 
        super().__init__("Les deux listes doivent avoir la même taille...")
#=================================================================================================================
class StatDouble():
    def __init__(self,X,Y,pStart=0,pStop=None,pStep=1):
        if len(X)!=len(Y): raise ValueError(f'bad input shape ({len(X)}, {len(Y)})')
        self.X=Stat(X,pStart,pStop,pStep)
        self.Y=Stat(Y,pStart,pStop,pStep)
        self.N=self.X.N
    def __iter__(self): yield from ((self.X[i],self.Y[i]) for i in self.N)
    def __getitem__(self,n): 
        try: return [(self.X[i],self.Y[i]) for i in self.N][n]
        except: pass
    def __enter__(self): return self
    def __exit__(self,*args):
        del self
        return True
    def count(self,m='.',n='.'): 
        return sum(1 for i in range(self.N) if (m=='.' or self.X[i]==m) and (n=='.' or self.Y[i]==n)) 
    # def countC(self,m='.',n='.'):    return sum(self.count(i) for i in self.X.moda)
    def freq(self,m='.',n='.'):     return self.count(m,n)/self.N
    # def freqC(self,m='.',n='.'):    return sum(self.freq(i) for i in range(1,n+1))
    def contingence(self):
        data=([[self.count(i,j) for j in self.Y.moda]+[self.count(i,'.')] for i in self.X.moda]+[[self.count('.',j) for j in self.Y.moda]+[self.N]])
        text=[[f"{j}" for j in i] for i in data]
        rows=[f'{i}' for i in self.X.moda]+['.']
        columns=[f'{j}' for j in self.Y.moda]+['.']
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
    def covar(self): return sum((self.X[i]-self.X.mean)*(self.Y[i]-self.Y.mean) for i in range(self.N))/(self.N)
    def correlation(self): return self.covar()/(self.X.stdDev*self.Y.stdDev)
    def scatter(self,called=False): 
        s=plt.scatter(self.X.serie,self.Y.serie,c='#F00')
        if not called: plt.show()
        return s
    def regressionLin(self):
        t=np.array([min(self.X.serie),max(self.X.serie)+1])
        a=self.covar()/self.X.stdDev**2
        b=self.Y.mean-self.X.mean*a
        plt.plot(t,a*t+b,'b-')
        self.scatter(True)
        plt.show()
    def regressionLog(self,type=None,prec=200): 
        for i in range(self.N):
            if self.Y[i]<=0: raise RuntimeWarning('Valeur de log invalide (inf. ou égale à 0)')
            if self.X[i]<=0: 
                if type==1: raise RuntimeWarning('Valeur de log invalide (inf. ou égale à 0)')
                if type==None: type=2
        t=np.linspace(min(self.X.serie),max(self.X.serie),prec)
        if type!=2:   #type 1
            with StatDouble([np.log(i) for i in self.X],[np.log(j) for j in self.Y]) as s: 
                a=s.covar()/s.X.stdDev**2
                b=s.Y.mean-s.X.mean*a
                plt.plot(t,np.exp(b)*t**a,'b-')
        if type!=1:   #type 2
            with StatDouble(self.X.serie,[np.log(j) for j in self.Y]) as s: 
                a=s.covar()/s.X.stdDev**2
                b=s.Y.mean-s.X.mean*a
                plt.plot(t,np.exp(b)*np.exp(a)**t,'g-')
        self.scatter(True)
        plt.show()
    def regressionPoly(self,deg=1,prec=200): 
        u=np.linspace(min(self.X.serie),max(self.X.serie),prec)
        m=np.array([[sum(x**(i+j) for x in self.X) for i in range(self.N+1)] for j in range(self.N+1)],dtype='float')
        b=np.array([sum(self.Y[i]*self.X[i]**k for i in range(self.N)) for k in range(self.N+1)],dtype='float')
        try:a=np.linalg.solve(m,b)
        except LinAlgError: raise LinAlgError("La matrice qui résulte des séries est singulière.")
        for i in range(self.N+1):print(f"{a[i]}x^({i})+",end='')
        plt.plot(u,sum(a[i]*u**i for i in range(self.N+1)),'b-')
        self.scatter(True)
        plt.show()
