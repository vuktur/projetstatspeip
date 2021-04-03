from math import sqrt
import Stats as St

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
        self.X= St.Stats(self.O,X,"brute")
        Y = []
        for x in self.D:
            Y.append(x[1])
        self.Y=St.Stats(self.O,Y,"brute")

    def covariance_b(self):
        sum=0
        for i in range(len(self.D)):
            sum+= (self.X.X[i]-self.X.moyenne_b())*(self.Y.X[i]-self.Y.moyenne_b())
        return sum/self.O

    def correlation_b(self):
        return self.covariance_b()/(self.X.écart_type_b()*self.Y.écart_type_b())

    def regretion_b(self):
        a=self.covariance_b()/self.X.Variance_b()
        b=self.Y.moyenne_b()-((self.covariance_b()/self.X.Variance_b())*self.X.moyenne_b())
        DYX="Y = "+str(round(a,4))+"*X +"+str(round(b,4))
        a = self.covariance_b() / self.Y.Variance_b()
        b = self.X.moyenne_b() - ((self.covariance_b() / self.Y.Variance_b()) * self.Y.moyenne_b())
        DXY = "X = "+str(round(a,4))+"*Y +"+str(round(b,4))
        return (DYX,DXY)

    def covariance_d(self):
        L = sorted(self.X.X)
        lx = []
        for i in range(len(L)):
            for j in range(L[i][1]):
                lx.append(L[i][0])
        L = sorted(self.Y.X)
        ly = []
        for i in range(len(L)):
            for j in range(L[i][1]):
                ly.append(L[i][0])
        sum = 0
        for i in range(len(lx)):
            sum += (lx[i] - self.X.moyenne_d()) * (ly[i] - self.Y.moyenne_d())
        return sum / self.O

    def correlation_d(self):
        return self.covariance_d() / (self.X.écart_type_d() * self.Y.écart_type_d())

    def regretion_d(self):
        a = self.covariance_d() / self.X.Variance_d()
        b = self.Y.moyenne_d() - ((self.covariance_d() / self.X.Variance_d()) * self.X.moyenne_d())
        DYX = "Y = " + str(round(a, 4)) + "*X +" + str(round(b, 4))
        a = self.covariance_d() / self.Y.Variance_d()
        b = self.X.moyenne_d() - ((self.covariance_d() / self.Y.Variance_d()) * self.Y.moyenne_d())
        DXY = "X = " + str(round(a, 4)) + "*Y +" + str(round(b, 4))
        return (DYX, DXY)

    def __str__(self):
        if self.X.T=="brute":
            if self.Y.T=="brute":
                return "Attributs de la première statistique : Moyenne : {} ; Mode : {} ; Médiane : {} ;\n Quartiles : {} ; Variance : {} ;\n Ecart-type : {} ; Etendue : {} ;\n Courbe : {} ; Distribution : {} .\n" \
                       "\nAttributs de la deuxième statistique : Moyenne : {} ; Mode : {} ; Médiane : {} ;\n Quartiles : {} ; Variance : {} ;\n Ecart-type : {} ; Etendue : {} ;\n Courbe : {} ; Distribution : {} .\n" \
                       "\nCovariance : {} ; Coefficient de Corrélation : {} ; Droites de Régression : de Y en X : {} ; de X en Y : {} .".format(
                    self.X.moyenne_b(), self.X.mode_b(), self.X.médiane_b(), self.X.Quartiles_b(), self.X.Variance_b(),
                    self.X.écart_type_b(),
                    self.X.étendue_b(), self.X.applatissement_b(), self.X.asymétrie_b(), self.Y.moyenne_b(),
                    self.Y.mode_b(), self.Y.médiane_b(), self.Y.Quartiles_b(),
                    self.Y.Variance_b(),
                    self.Y.écart_type_b(),
                    self.Y.étendue_b(), self.Y.applatissement_b(), self.Y.asymétrie_b(),
                    self.covariance_b(), self.correlation_b(), self.regretion_b()[0], self.regretion_b()[1])
            else :
                return "type de la série Y non valide ou type de Y différent de X"

        if self.X.T=="dépouillée":
            if self.Y.T=="dépouillée":
                return "Attributs de la première statistique : Moyenne : {} ; Mode : {} ; Médiane : {} ;\n Quartiles : {} ; Variance : {} ;\n Ecart-type : {} ; Etendue : {} ;\n Courbe : {} ; Distribution : {} .\n" \
                       "\nAttributs de la deuxième statistique : Moyenne : {} ; Mode : {} ; Médiane : {} ;\n Quartiles : {} ; Variance : {} ;\n Ecart-type : {} ; Etendue : {} ;\n Courbe : {} ; Distribution : {} .\n" \
                       "\nCovariance : {} ; Coefficient de Corrélation : {} ; Droites de Régression : de Y en X : {} ; de X en Y : {} .".format(
                    self.X.moyenne_d(), self.X.mode_d(), self.X.médiane_d(), self.X.Quartiles_d(), self.X.Variance_d(),
                    self.X.écart_type_d(),
                    self.X.étendue_d(), self.X.applatissement_d(), self.X.asymétrie_d(), self.Y.moyenne_d(),
                    self.Y.mode_d(), self.Y.médiane_d(), self.Y.Quartiles_d(),
                    self.Y.Variance_d(),
                    self.Y.écart_type_d(),
                    self.Y.étendue_d(), self.Y.applatissement_d(), self.Y.asymétrie_d(),
                    self.covariance_d(), self.correlation_d(), self.regretion_d()[0], self.regretion_d()[1])

            else :
                return "type de la série Y non valide ou type de Y différent de X"

        else :
            return "type de la série X non valide"


std=StatDouble(4,[(1,2),(3,4),(2,6),(1,3)])
std.X.depouille()
std.Y.depouille()
print(std)