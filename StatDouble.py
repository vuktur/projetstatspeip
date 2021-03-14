from math import sqrt

class Stats():
    def __init__(self,NbObservation,SérieStatistique):
        self.O=NbObservation
        self.X=SérieStatistique
        self.M=[]
        for x in self.X:
            if x not in self.M :
                self.M.append(x)

    def effectif(self,i):
        return self.X.count(i)

    def fréquence(self,i):
        return self.effectif(i)/self.O

    def moyenne(self):
        moy = 0
        for i in self.M:
            moy += self.fréquence(i)*i
        return round(moy,2)

    def médiane(self):
        L=sorted(self.X)
        if len(L)%2==0:
            return round((L[round(len(L)/2)]+L[round(len(L)/2)-1])/2)
        else :
            return L[round(len(L)/2)]

    def Quartiles(self):
        L = sorted(self.X)
        if len(L)>=3:
            if len(L) % 2 == 0:
                p=round((L[round(len(L)/4)]+L[round(len(L)/4)-1])/2)
                d=round((L[round(len(L)/2)]+L[round(len(L)/2)-1])/2)
                t=round((L[round(len(L)/4)*3]+L[(round(len(L)/4)*3)-1])/2)
            else:
                p=L[round(len(L)/4)]
                d=L[round(len(L)/2)]
                t=L[round(len(L)/4*3)]
        else:
            print("Il n'y a pas assez d'observations")
        return (p,d,t)

    def Variance(self):
        V=0
        for i in self.M:
            V += self.fréquence(i)*((i-self.moyenne())**2)
        return round(V,2)

    def écart_type(self):
        V=sqrt(self.Variance())
        return round(V,2)

    def étendue(self):
        L = sorted(self.X)
        min=L[0]
        max=L[len(L)-1]
        return max-min

    def mode(self):
        max=0
        j=0
        for i in self.M:
            if self.effectif(i)>max:
                max=self.effectif(i)
                j=i
        return j

    def asymétrie(self):
        u=0
        for i in self.M:
            u+=self.fréquence(i)*((i-self.moyenne())**3)
        o=self.Variance()**(3/2)
        if u/o==0:
            return "courbe symétrique"
        elif u/o<0:
            return "bosse décalé vers la droite"
        elif u/o>0:
            return "bosse décalé vers la gauche"

    def applatissement(self):
        u = 0
        for i in self.M:
            u += self.fréquence(i) * ((i - self.moyenne()) ** 4)
        o=self.Variance()**2
        if 2.5<=(u/o)<=3.5:
            return "distribution normale"
        elif u/o>3.5:
            return "courbe en pic"
        elif u/o<2.5:
            return "courbe plate"

    def __str__(self):
        return "Attributs de la statistique : Moyenne : {} ; Mode : {} ; Médiane : {} ;\n Quartiles : {} ; Variance : {} ;\n Ecart-type : {} ; Etendue : {} ;\n Courbe : {} ; Distribution : {} .".format(
            self.moyenne(), self.mode(), self.médiane(), self.Quartiles(), self.Variance(), self.écart_type(),
            self.étendue(), self.applatissement(), self.asymétrie())



class StatDouble():
    def __init__(self,NbObservation,SérieStatistique):
        # les séries doivent être brutes et non dépouillées
        self.O = NbObservation
        #O pour Observation
        self.D = SérieStatistique
        self.M = []
        for x in self.D:
            if x not in self.M:
                self.M.append(x)
        X=[]
        for x in self.D:
            X.append(x[0])
        self.X=Stats(self.O,X)
        Y = []
        for x in self.D:
            Y.append(x[1])
        self.Y=Stats(self.O,Y)

    def covariance(self):
        sum=0
        for i in range(len(self.M)):
            sum+= (self.X.X[i]-self.X.moyenne())*(self.Y.X[i]-self.Y.moyenne())
        return sum/self.O

    def correlation(self):
        return self.covariance()/(self.X.écart_type()*self.Y.écart_type())

    def regretion(self):
        a=self.covariance()/self.X.Variance()
        b=self.Y.moyenne()-((self.covariance()/self.X.Variance())*self.X.moyenne())
        DYX="Y = "+str(round(a,4))+"*X +"+str(round(b,4))
        a = self.covariance() / self.Y.Variance()
        b = self.X.moyenne() - ((self.covariance() / self.Y.Variance()) * self.Y.moyenne())
        DXY = "X = "+str(round(a,4))+"*Y +"+str(round(b,4))
        return (DYX,DXY)

    def __str__(self):
        return "Attributs de la première statistique : Moyenne : {} ; Mode : {} ; Médiane : {} ;\n Quartiles : {} ; Variance : {} ;\n Ecart-type : {} ; Etendue : {} ;\n Courbe : {} ; Distribution : {} .\n" \
               "\nAttributs de la deuxième statistique : Moyenne : {} ; Mode : {} ; Médiane : {} ;\n Quartiles : {} ; Variance : {} ;\n Ecart-type : {} ; Etendue : {} ;\n Courbe : {} ; Distribution : {} .\n" \
               "\nCovariance : {} ; Coefficient de Corrélation : {} ; Droites de Régression : de Y en X : {} ; de X en Y : {} .".format(
            self.X.moyenne(), self.X.mode(), self.X.médiane(), self.X.Quartiles(), self.X.Variance(),
            self.X.écart_type(),
            self.X.étendue(), self.X.applatissement(), self.X.asymétrie(),self.Y.moyenne(), self.Y.mode(), self.Y.médiane(), self.Y.Quartiles(),
            self.Y.Variance(),
            self.Y.écart_type(),
            self.Y.étendue(), self.Y.applatissement(), self.Y.asymétrie(),
            self.covariance(),self.correlation(),self.regretion()[0],self.regretion()[1])


std=StatDouble(4,[(1,2),(3,4),(2,6),(1,3)])
print(std)