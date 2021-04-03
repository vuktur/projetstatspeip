from fractions import Fraction
import numpy as np
# from math import sqrt
# from decimal import Decimal, ROUND_HALF_UP
import matplotlib.pyplot as plt
from numpy.linalg import LinAlgError

#=================================================================================================================

class Stat():
    def __init__(self,statistique,populationStart=0,populationStop=10,populationStep=1):
        self.serie=[]
        if(isinstance(statistique,list)): #si c'est une liste
            if(populationStop==None):populationStop=len(statistique)
            self.serie=statistique
        elif(callable(statistique)): #si c'est une fonction
            try:self.serie=[statistique(i) for i in np.arange(populationStart,populationStop,populationStep)]
            except:raise
        self.pop=np.arange(populationStart,populationStop,populationStep).tolist()
        self.N=len(np.arange(populationStart,populationStop,populationStep))
        if not isinstance(self.serie[0],list): #si ce n'est pas une stat classee
            self.modalites=sorted(list(dict.fromkeys(self.serie)))
            self.mode=[i for i in self.modalites if self.effectif(i)==max(self.effectif(j) for j in self.modalites)]
            self.mediane=self.quantile(2)[0]
            self.moyenne=self.moment(1)
            self.etendue=max(self.serie)-min(self.serie)
            self.variance=self.momentCentre(2)
            self.ecarttype=abs(self.variance)**(1/2)
            self.ecartmoyen=sum(abs(i-self.moment(1)) for i in self.serie)/self.N

    def __repr__(self):return(
        # np.array2string(np.array([[i for i in self.modalites],[self.effectif(i) for i in self.modalites]]))+'\n'+
        f"Moyenne : {self.moyenne} , Mode : {self.mode} , Médiane : {self.mediane}\nVariance : {self.variance} , Ecart-type : {self.ecarttype} , Etendue : {self.etendue}\nCourbe : {self.applatissement()} , Distribution : {self.asymetrie()}")

    def __iter__(self): yield from self.serie

    def __getitem__(self,n): 
        try: return self.serie[n]
        except: pass

    def __enter__(self): return self

    def __exit__(self,*args):
        del self
        return True

    def effectif(self,n): 
        return self.serie.count(n)

    def effectifC(self,n): 
        return sum(self.effectif(i) for i in sorted(self.modalites) if i<=n)

    def frequence(self,n): 
        return (self.effectif(n)/self.N)

    def frequenceC(self,n): 
        return sum(self.frequence(i) for i in sorted(self.modalites) if i<=n)

    def quantile(self,n): 
        if isinstance(self.serie[0],list): return None
        q,s=[],sorted(self.serie)
        for i in range(1,n):
            a=(i*len(s)/n)
            b=(a-a%.5+.5 if (a%.5<.25 if a>len(s)/2 else a%.5<=.25) else a-a%.5+1)
            q.append(s[int(b)-1] if b%1==0 else (s[int(b)]+s[int(b)-1])/2)
        return q

    def moment(self,k): 
        if isinstance(self.serie[0],list): return None
        return sum(i**k for i in self.serie)/self.N

    def momentCentre(self,k): 
        return sum((i-self.moment(1))**k for i in self.serie)/self.N

    def asymetrie(self): 
        return (self.momentCentre(3)/self.momentCentre(2)**(3/2))

    def applatissement(self): 
        return (self.momentCentre(4)/self.momentCentre(2)**2)

    def classer(self,bacs=[]): 
        bacs=sorted(bacs)
        claList=[[j for j in sorted(self.serie) if (bacs[i]<=j<=bacs[i+1] if i==0 else bacs[i]<j<=bacs[i+1])] for i in range(len(bacs)-1)] # str(Fraction(self.serie[j]).limit_denominator()) 
        return StatClassee(claList,bacs=bacs)

#=================================================================================================================

class StatClassee(Stat):
    def __init__(self,stat,populationStart=0,populationStop=None,populationStep=1,bacs=[]):
        super().__init__(stat,populationStart,populationStop,populationStep)
        self.modalites=sorted(list(dict.fromkeys((tuple(i) for i in self.serie))))
        self.bacs=bacs
        self.widths=[self.bacs[i+1]-self.bacs[i] for i in range(len(self.bacs)-1)]
        self.heights=[self.effectif(i)/self.widths[i] for i in range(len(self.serie))]

    def __enter__(self): 
        return self

    def __exit__(self,*args):
        del self
        return True

    def effectif(self,n): 
        return len(self.serie[n])

    def mode(self): 
        return max(self.heights)

    def classeModale(self): 
        return [self.serie[i] for i in range(len(self.serie)) if self.heights[i]==self.mode()]

    def depouiller(self):
        l=[]
        for i in self.serie:
            with Stat(i) as inst:
                l.append(inst.mediane())
        return l

    def histogramme(self):
        plt.bar([(self.bacs[i+1]+self.bacs[i])/2 for i in range(len(self.bacs)-1)],height=self.heights,width=self.widths,color='#4287f5',edgecolor='#0041a8',linewidth=1,alpha=.7)
        plt.grid(axis='y',alpha=.7)
        plt.xticks(np.arange(min(self.bacs)-2,max(self.bacs)+3,1))
        plt.show()

#=================================================================================================================

class StatDouble():
    def __init__(self,X,Y,populationStart=0,populationStop=None,populationStep=1):
        if len(X)!=len(Y): raise ValueError(f'Les deux listes doivent avoir la même taille... ({len(X)}, {len(Y)})')
        self.X=Stat(X,populationStart,populationStop,populationStep)
        self.Y=Stat(Y,populationStart,populationStop,populationStep)
        self.N=self.X.N

    def __iter__(self): 
        yield from ((self.X[i],self.Y[i]) for i in self.N)

    def __getitem__(self,n): 
        try: return [(self.X[i],self.Y[i]) for i in self.N][n]
        except: pass

    def __enter__(self): 
        return self
 
    def __exit__(self,*args):
        del self
        return True

    def effectif(self,m='.',n='.'): 
        return sum(1 for i in range(self.N) if (m=='.' or self.X[i]==m) and (n=='.' or self.Y[i]==n)) 

    # def effectifC(self,m='.',n='.'): 
    #   return sum(self.effectif(i) for i in self.X.modalites)

    def frequence(self,m='.',n='.'): 
        return self.effectif(m,n)/self.N

    # def frequenceC(self,m='.',n='.'): 
    #   return sum(self.frequence(i) for i in range(1,n+1))

    def contingence(self):
        data=([[self.effectif(i,j) for j in self.Y.modalites]+[self.effectif(i,'.')] for i in self.X.modalites]+[[self.effectif('.',j) for j in self.Y.modalites]+[self.N]])
        text=[[f"{j}" for j in i] for i in data]
        rows=[f'{i}' for i in self.X.modalites]+['.']
        columns=[f'{j}' for j in self.Y.modalites]+['.']
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

    def covar(self): 
        return sum((self.X[i]-self.X.moyenne)*(self.Y[i]-self.Y.moyenne) for i in range(self.N))/(self.N)

    def correlation(self): 
        return self.covar()/(self.X.ecarttype*self.Y.ecarttype)

    def scatter(self,called=False): 
        s=plt.scatter(self.X.serie,self.Y.serie,c='#F00')
        if not called: plt.show()
        return s

    def regressionLin(self):
        t=np.array([min(self.X.serie),max(self.X.serie)+1])
        a=self.covar()/self.X.ecarttype**2
        b=self.Y.moyenne-self.X.moyenne*a
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
                a=s.covar()/s.X.ecarttype**2
                b=s.Y.moyenne-s.X.moyenne*a
                plt.plot(t,np.exp(b)*t**a,'b-')
        if type!=1:   #type 2
            with StatDouble(self.X.serie,[np.log(j) for j in self.Y]) as s: 
                a=s.covar()/s.X.ecarttype**2
                b=s.Y.moyenne-s.X.moyenne*a
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
