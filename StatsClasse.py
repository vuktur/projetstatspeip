from math import sqrt

class StatClass():
    def __init__(self,NbObservation,SérieStatistique):
        #SérieStatistique doit etre de la forme : [((x,x),x),((x,x),x),((x,x),x),((x,x),x),...]
        self.N=NbObservation
        self.X=SérieStatistique
        self.Xdépouille=[]
        for i in range(len(self.X)):
            self.Xdépouille.append(((self.X[i][0][0] + self.X[i][0][1]) / 2, self.X[i][1]))

    def moyenne(self):
        moy=0
        for i in range(len(self.Xdépouille)):
            moy+=self.Xdépouille[i][0]*self.Xdépouille[i][1]
        return moy/self.N

    def mode(self):
        max = 0
        modeCourant= 0
        for i in range(len(self.Xdépouille)):
            if self.Xdépouille[i][1] > max:
                max = self.Xdépouille[i][1]
                modeCourant = self.Xdépouille[i][0]
        return modeCourant

    def médiane(self):
        L = sorted(self.Xdépouille)
        l=[]
        for i in range(len(L)):
            for j in range(L[i][1]):
                l.append(L[i][0])
        if len(l) % 2 == 0:
            return round((l[round(len(l) / 2)] + l[round(len(l) / 2) - 1]) / 2)
        else:
            return l[round(len(l) / 2)]

    def Quartiles(self):
        L = sorted(self.Xdépouille)
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

    def Variance(self):
        V=0
        for i in range(len(self.Xdépouille)):
            V += self.Xdépouille[i][1]*((self.Xdépouille[i][0]-self.moyenne())**2)
        return round(V/self.N,2)

    def écart_type(self):
        V=sqrt(self.Variance())
        return round(V,2)

    def étendue(self):
        L = sorted(self.X)
        min=L[0][0][0]
        max=L[len(L)-1][0][1]
        return max-min

    def asymétrie(self):
        u=0
        for i in range(len(self.Xdépouille)):
            u+=self.Xdépouille[i][1]*((self.Xdépouille[i][0]-self.moyenne())**3)
        o=self.Variance()**(3/2)
        if (u/self.N)/o==0:
            return "courbe symétrique"
        elif (u/self.N)/o<0:
            return "bosse décalé vers la droite"
        elif (u/self.N)/o>0:
            return "bosse décalé vers la gauche"

    def applatissement(self):
        u = 0
        for i in range(len(self.Xdépouille)):
            u += self.Xdépouille[i][1] * ((self.Xdépouille[i][0] - self.moyenne()) ** 4)
        o=self.Variance()**2
        if 2.5<=((u/self.N)/o)<=3.5:
            return "distribution normale"
        elif (u/self.N)/o>3.5:
            return "courbe en pic"
        elif (u/self.N)/o<2.5:
            return "courbe plate"

    def __repr__(self):
        return "Attributs de la statistique : Moyenne : {} ; Mode : {} ; Médiane : {} ;\n Quartiles : {} ; Variance : {} ;\n Ecart-type : {} ; Etendue : {} ;\n Courbe : {} ; Distribution : {} .".format(self.moyenne(),self.mode(),self.médiane(),self.Quartiles(),self.Variance(),self.écart_type(),self.étendue(),self.applatissement(),self.asymétrie())


stc=StatClass(8,[((1,2),2),((2,3),2),((3,4),2)])
print(stc)