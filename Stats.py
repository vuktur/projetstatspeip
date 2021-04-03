from math import sqrt

class Stats():
    def __init__(self,NbObservation,SérieStatistique,typeStat):
        self.O=NbObservation
        self.X=SérieStatistique
        self.T = typeStat
        self.M=[]
        for x in self.X:
            if self.T=="brute":
                if x not in self.M :
                    self.M.append(x)
            if self.T == "dépouillée":
                self.M.append(x[0])
    # def effectif(self,i): return self.X.count(i)
    # def fréquence(self,i): return self.effectif(i)/self.O

    # def moyenne_b(self):
    #     moy = 0
    #     for i in self.M:
    #         moy += self.fréquence(i)*i
    #     return round(moy,2)

    # def médiane_b(self):
    #     L=sorted(self.X)
    #     if len(L)%2==0:
    #         return round((L[round(len(L)/2)]+L[round(len(L)/2)-1])/2)
    #     else :
    #         return L[round(len(L)/2)]

    # def Quartiles_b(self):
    #     L = sorted(self.X)
    #     if len(L)>=3:
    #         if len(L) % 2 == 0:
    #             p=round((L[round(len(L)/4)]+L[round(len(L)/4)-1])/2)
    #             d=round((L[round(len(L)/2)]+L[round(len(L)/2)-1])/2)
    #             t=round((L[round(len(L)/4)*3]+L[(round(len(L)/4)*3)-1])/2)
    #         else:
    #             p=L[round(len(L)/4)]
    #             d=L[round(len(L)/2)]
    #             t=L[round(len(L)/4*3)]
    #     else:
    #         print("Il n'y a pas assez d'observations")
    #     return (p,d,t)

    # def Variance_b(self):
    #     V=0
    #     for i in self.M:
    #         V += self.fréquence(i)*((i-self.moyenne_b())**2)
    #     return round(V,2)

    # def écart_type_b(self):
    #     V=sqrt(self.Variance_b())
    #     return round(V,2)

    def asymétrie_b(self):
        u=0
        for i in self.M:
            u+=self.fréquence(i)*((i-self.moyenne_b())**3)
        o=self.Variance_b()**(3/2)
        if u/o==0:
            return "courbe symétrique"
        elif u/o<0:
            return "bosse décalé vers la droite"
        elif u/o>0:
            return "bosse décalé vers la gauche"

    def applatissement_b(self):
        u = 0
        for i in self.M:
            u += self.fréquence(i) * ((i - self.moyenne_b()) ** 4)
        o=self.Variance_b()**2
        if 2.5<=(u/o)<=3.5:
            return "distribution normale"
        elif u/o>3.5:
            return "courbe en pic"
        elif u/o<2.5:
            return "courbe plate"

    def moyenne_d(self):
        moy=0
        for i in range(len(self.X)):
            moy+=self.X[i][0]*self.X[i][1]
        return moy/self.O

    def mode_d(self):
        max=0
        j=0
        for i in range(len(self.X)):
            if self.X[i][1]>max:
                max=self.X[i][1]
                j=self.X[i][0]
        return j

    def médiane_d(self):
        L = sorted(self.X)
        l=[]
        for i in range(len(L)):
            for j in range(L[i][1]):
                l.append(L[i][0])
        if len(l) % 2 == 0:
            return round((l[round(len(l) / 2)] + l[round(len(l) / 2) - 1]) / 2)
        else:
            return l[round(len(l) / 2)]

    def Quartiles_d(self):
        L = sorted(self.X)
        l = []
        for i in range(len(L)):
            for j in range(L[i][1]):
                l.append(L[i][0])
        if len(l) >= 3:
            if len(L) % 2 == 0:
                p = round((l[round(len(l) / 4)] + l[round(len(l) / 4) - 1]) / 2)
                d = round((l[round(len(l) / 2)] + l[round(len(l) / 2) - 1]) / 2)
                t = round((l[round(len(l) / 4) * 3] + l[(round(len(l) / 4) * 3) - 1]) / 2)
            else:
                p = l[round(len(l) / 4)]
                d = l[round(len(l) / 2)]
                t = l[round(len(l) / 4 * 3)]
        else:
            print("Il n'y a pas assez d'observations")
        return (p, d, t)

    def Variance_d(self):
        V=0
        for i in range(len(self.X)):
            V += self.X[i][1]*((self.X[i][0]-self.moyenne_d())**2)
        return round(V/self.O,2)

    def écart_type_d(self):
        V=sqrt(self.Variance_d())
        return round(V,2)

    def étendue_d(self):
        L = sorted(self.X)
        min=L[0][0]
        max=L[len(L)-1][0]
        return max-min

    def asymétrie_d(self):
        u=0
        for i in range(len(self.X)):
            u+=self.X[i][1]*((self.X[i][0]-self.moyenne_d())**3)
        o=self.Variance_d()**(3/2)
        if (u/self.O)/o==0:
            return "courbe symétrique"
        elif (u/self.O)/o<0:
            return "bosse décalé vers la droite"
        elif (u/self.O)/o>0:
            return "bosse décalé vers la gauche"

    def applatissement_d(self):
        u = 0
        for i in range(len(self.X)):
            u += self.X[i][1] * ((self.X[i][0] - self.moyenne_d()) ** 4)
        o=self.Variance_d()**2
        if 2.5<=((u/self.O)/o)<=3.5:
            return "distribution normale"
        elif (u/self.O)/o>3.5:
            return "courbe en pic"
        elif (u/self.O)/o<2.5:
            return "courbe plate"


    def __str__(self):
        if self.T=="brute":
            return "Attributs de la statistique : Moyenne : {} ; Mode : {} ; Médiane : {} ;\n Quartiles : {} ; Variance : {} ;\n Ecart-type : {} ; Etendue : {} ;\n Courbe : {} ; Distribution : {} ; type : {} .".format(
                self.moyenne_b(), self.mode_b(), self.médiane_b(), self.Quartiles_b(), self.Variance_b(), self.écart_type_b(),
                self.étendue_b(), self.applatissement_b(), self.asymétrie_b(),self.T)

        if self.T=="dépouillée":
            return "Attributs de la statistique : Moyenne : {} ; Mode : {} ; Médiane : {} ;\n Quartiles : {} ; Variance : {} ;\n Ecart-type : {} ; Etendue : {} ;\n Courbe : {} ; Distribution : {} ; type : {} .".format(
                self.moyenne_d(), self.mode_d(), self.médiane_d(), self.Quartiles_d(), self.Variance_d(), self.écart_type_d(),
                self.étendue_d(), self.applatissement_d(), self.asymétrie_d(),self.T)
        else:
            return "type non valide"

    def brute(self):
        L = sorted(self.X)
        l = []
        for i in range(len(L)):
            for j in range(L[i][1]):
                l.append(L[i][0])
        self.X = l
        self.T = "brute"

    def depouille(self):
        L = sorted(self.X)
        l = []
        for i in self.M:
            if i in self.X:
                l.append((i,self.X.count(i)))
        self.X = l
        self.T = "dépouillée"



st1=Stats(10,[(1, 3), (2, 1), (5, 2), (3, 1), (7, 1), (6, 1), (9, 1)],"dépouillée")
