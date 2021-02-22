# Chapitre 1

## Statistiques descriptives

### 1.1 Généralités

Une statistique est une application d'une population $Ω$ vers un ensemble de valeurs $C$.

$$
\left\{
    \begin{array}{ll}
        X: & Ω → C\\
        & ω → X(ω)
    \end{array}
\right.
$$

- $Ω$ : population finie d'individus $ω$. On va mesurer/observer un caractère particulier sur ces individus.  
**`self.pop`**  

- $C$ : ensemble des valeurs possibles du caractère, appelées aussi modalités.  
**`self.moda`**  

- $X$ : Statistique (parfois appelée aussi caractère). Application qui à tout individu associe la
valeur de son caractère.  
**`self.serie`**  

<!---->
- Une statistique peut être quantitative ou
qualitative.
- Une statistique quantitative peut être discrète ou continue.
- Une statistique peut être multiple (à n paramètres).

### 1.2 Statistique simple (univariée)

#### 1.2.1 Notations

>On va se limiter à des statistiques quantitatives.

- Ω population finie de $N$ individus.
- $C \subset R$

**Première représentation :** Une série statistique est un $N$-uplet $X= (v_1,\,v_2,\,...,\,v_N)$  
**Par exemple :** $X= (2.1,\,5.23,\,0.61,\,2.1,\,7.2,\,0.61)$  
On parle alors de **série statistique brute**.

**Seconde représentation :**  
L'ensemble des valeurs observables de $X$ est fini. On peut écrire :

$$
X(Ω) =\{x_1,\,x_2,\,...,\,x_p\}\;(1≤p≤N)
$$

pour la suite on supposera $x_1<x_2<...<x_p$.

- Effectif $n_i=\#(X^−1 \{x_i\})$ : nombre de fois que la valeur $x_i$ a été observée dans la population
ou nombre d'individus admettant $x_i$ comme valeur du caractère.  
**`self.ef(i)`**

- Effectif cumulé $N_i = \sum^i_{j=1} n_j = \#(X^{-1}\{]−\infin,x_i]\})$ : nombre d'individus présentant une
valeur de caractère plus petite que $x_i$, ou égale.On a la relation $N_i=N_{i−1}+n_i$ en posant $N_0=0$ et peut remarquer que $N_p=N$  
**`self.efC(i)`**

- Fréquence $f_i=n_i/N$.  
  **`self.fr(i)`**

- Fréquence cumulée $F_i=N_i/N=\sum^i_{j=1} f_j=F_{i−1}+f_i$ en posant $F_0=0$. On remarque que
$F_p=1$  
**`self.frC(i)`**

Une série statistique est une famille de la forme $(x_i,n_i)_{i\in [1,p]}$ ou $(x_i,f_i)_{i\in [1,p]}$  
On parle parfois de **série statistique dépouillée** ou de **série statistique regroupée et
ordonnée**.

#### 1.2.2 Paramètresde position

**Le mode**  
C'est la valeur du caractère d'effectif maximal

$$
mode = x_i \text{ tq } n_i=\max_{1≤j≤p}(n_j)
$$

Attention : il n'est pas forcément unique.

**La médiane**  
C'est la valeur du caractère qui sépare la population en deux parties égales.  
Attention : parfois dificile à définir.

$$
η\text{ tq }\#\{ω_i\,|\,X(ω_i)<η\}=\#\{ω_i\,|\,X(ω_i)>η\}\\
η\text{ tq }\#\{ω_i\,|\,X(ω_i)≤η\}=\#\{ω_i\,|\,X(ω_i)≥η\}\\
η=x_i\text{ tq }N_{i−1}<N/2≤N_i
$$

**Les quantiles**  
Dans le même esprit, on peut définir :

- les quartiles : 3 valeurs qui découpent la population en 4 parties égales. Le deuxième quartile
étant alors égal à la médiane.
- les déciles : 9 valeurs qui découpent la population en 10 parties égales.
- les centiles : 99 valeurs qui découpent la population en 100 parties égales.
- ou tout autre découpage.

**La moyenne arithmétique**  
$$
m(X)=\bar{x}=\frac{1}{N}\sum^p_{i=1}(n_ix_i)=\sum^p_{i=1}(f_ix_i)=\frac{1}{N}\sum^N_{i=1}v_i
$$
Remarque : si on pose $n=(n_1,\,n_2,\,...,\,n_p)$ et $X=(x_1,\,x_2,\,...,\,x_p)$ alors :
$$
\sum^p_{i=1}(n_ix_i)=n·X^t\text{ et }m(X)=\frac{1}{N}n·X^t
$$

#### 1.2.3 Paramètres de dispersion

**L'étendue**  
C'est la plage de valeur du caractère observée sur la population :
$$
w=\max_{1≤i≤p}(x_i)−\min_{1≤i≤p}(x_i)=\max_{1≤i≤N}(v_i)−\min_{1≤i≤N}(v_i)
$$  
Attention : sensible aux erreurs de mesure.

**Les quantiles**  
Dans le même ordre d'idée que l'étendue, on peut donner l'intervalle séparant le plus petit et
le plus grand décile (80% de la population) ou celui séparant le quartile inférieur $Q_I$ et le
quartile supérieur $Q_S$ (50% de la population) ou tout autre intervalle définie de manière
similaire.  

Intérêt : Élimine les mesures aberrantes.

**L'écart arithmétique moyen** [^1]  
Calcule la moyenne des écarts à la moyenne
$$
E=\frac{1}{N}\sum_{1≤i≤p}n_i|x_i−\bar{x}|=\sum_{1≤i≤p}f_i|x_i−\bar{x}|=\frac{1}{N}\sum_{1≤i≤p}|v_i−\bar{x}|
$$

[^1]: peu utilisé.

**L'écart quadratique moyen ou variance**  
Calcule la moyenne des carrés des écarts à la moyenne
<!-- 



 
V(X) =σ^2 X=
 
#### 1

#### N

#### ∑

 
1 ≤i≤p
 
 
ni(xi−x)^2 =
 
#### ∑

 
1 ≤i≤p
 
 
fi(xi−x)^2 =
 
#### 1

#### N

#### ∑

 
1 ≤i≤N
 
 
(vi−x)^2
 
RelationdeKo enig-Huygens

 
σX^2 =
 
#### (

#### 1

#### N

#### ∑

 
1 ≤i≤p
 
 
ni.x^2 i
 
#### )

 
−x^2 =
 
#### (

#### ∑

 
1 ≤i≤p
 
 
fi.x^2 i
 
#### )

 
−x^2 =
 
#### (

#### 1

#### N

#### ∑

 
1 ≤i≤N
 
 
vi^2
 
#### )

 
−x^2
 
L'écartty pe
C'estlaracinecarrédelavariance:mêmedimensionquelecaractèreétudié.

 
σX=
 
#### √

#### V(X) =

#### √

#### 1

#### N

#### ∑

 
1 ≤i≤p
 
 
ni(xi−x)^2 =
 
#### √

#### √

#### √

#### √

#### (

#### ∑

 
1 ≤i≤p
 
 
fi.x^2 i
 
#### )

 
−x^2 =...
 

#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.4 Lesmoments

Momentd'ordrek

 
mk(X) =
 
#### 1

#### N

 
∑p
 
 
i=
 
 
(ni.xki) =
 
 
∑p
 
 
i=
 
 
(fi.xki) =
 
#### 1

#### N

#### ∑N

 
i=
 
 
vik
 
Momentcentréd'ordrek

 
μk(X) =
 
#### 1

#### N

 
∑p
 
 
i=
 
 
(ni.(xi−x)k) =
 
 
∑p
 
 
i=
 
 
(fi.(xi−x)k) =
 
#### 1

#### N

#### ∑N

 
i=
 
 
(vi−x)k
 
Propriétés:

- m 0 (X) =μ 0 (X) = 1
- m 1 (X) =xetμ 1 (X) = 0
- μ 2 (X) =σX^2
- σ^2 X=m 2 (X)−m 1 (X)^2 (RelationdeKo enig-Huygens)
- Siunesériestatistique estsymétrique parrap portàsa moyennealors toussesmoments
centrésd'ordreimpairsontnuls.
- Par contre il ne sut pas de vérifier que μ 3 (X) = 0  pour conclure que la série est
symétriqueparrap portàsamoyenne.


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.5 Paramètresdeformes

Premierco ecientdeFisher:co ecientd'asymétrie

 
δ=
 
 
μ 3
σ^3
 
#### =

 
μ 3
μ^32 /^2
 
- sériesymétrique→δ= 0
- grandsécarts positifs%àlamoyenne→δ > 0 ("b ossedécaléeverslagauche")
- grandsécartsnégatifs%àlamoyenne→δ < 0 ("b ossedécaléeversladroite")
- leco ecientd'asymétrieestconsidérécommesignificatiflorsque|δ|> 0 , 5
- S'appliqueessentiellementàunesérieunimo dale.

Secondco ecientdeFisher:co ecientd'aplatissement

 
a=
 
 
μ 4
σ^4
 
#### =

 
μ 4
μ^22
 
- Unegrandevaleurdeatraduitunresserrementautourdelamoyenne("courb eenpic")
- Une petitevaleurdeatraduitunétalementdelasérie("courb eplate")
- Siladistributionestnormalealorsa=
- S'appliqueessentiellementàunesérieunimo dale.


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.6 Découpageenclasses

LorsqueXestuncaractèrecontinuouquelesfréquencesfisontfaibles(ppro chedeN)
onestamenéàdécouperledomainedevaleursdeXenclasses(sous-intervalles).

 
C 1 = [a 0 ,a 1 ],C 2 =]a 1 ,a 2 ],...,Cp′=]ap′− 1 ,ap′]
 
avecp′≤peta 0 ≤x 1 < xp≤ap′

Intérêt :Représentationgraphique(histogramme)etmiseenévidenced'uneclassemo dale
(classedehauteurmaximaledansl'histogramme)
→Lesclasses peuventêtreéventuellementdelargeursdifférentes.

- Onnotealorsnil'effectifdelaclasseCi:ni= #{X−^1 ]ai− 1 ,ai]}.
- On peut ensuitedéfinirNi, fi et Fi commevuprécédemment pourune sériestatistique
dé pouillée.

Lasérieestalorsdonnéesouslaformedelafamille((n 1 ,C 1 ),(n 2 ,C 2 ),...(np′,Cp′))
On parle alors d'une série statistique en classes ou regroup ée en classes ou encore,
parfois,classée.

- Àtoutesérieclasséeon peutfairecorres pondreunesériestatistiquedé pouillée(x′i,ni)i∈J 1 ,p′K
oùx′iestlecentredelaclasseCi(x′i= (ai− 1 +ai)/ 2 ).


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.7 Histogramme

Lorsquelastatistiqueestdécoup éeenclasses,onnelareprésenteplusparundiagramme
enbâtons,maisparunhistogramme.Chaqueclasseestreprésentéeparunrectangledontla
baseestpro portionnelleàlalargeurdelaclasseetlasurfacepro portionnelleàl'effectif(ou,
cequirevientaumême,àlafréquence)delaclasse.C'estbienlasurfaceetnonlahauteurdu
rectangle qui est pro portionnelle à l'effectif. Cette remarque prend toute son im portance
lorsquelesclassessontdelargeursdifférentes.


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

Exemple:ontravaillesurunestatistiquedécoup éesselon lesquatreclasses suivantes:
[2,4],]4,9],]9,11],]11,12]etchaqueclasseestd'effectif4.
L'axedesordonnées peutêtrevucommeunedensité.


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.8 Laclassemo dale(paramètre de position)

C'estlaclassecorres pondantaurectangleleplushautdansl'histogramme(onparlebien
icidehauteuretnondesurface).Elle peutnepasêtreunique.Ilarrivequ'ondéfinisselemo de
delastatistiquecommelemilieudelaclassemo dale(cettedéfinitionn'estpasentièrement
équivalenteàcelledonnéeplushaut).Dansl'exempleprécédent,laclassemo daleestladernière
(classe]11,12])etlemo deest11,5.


#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

## 1.3 Statistique double (bivariée)

### 1.3.1 Notations

 
Onvaselimiteràdesstatistiquesquantitatives.
 
- Ω populationfiniedeNindividus.
- {UnestatistiquedoubleC estuneapplicationdeΩdansR^2.
    C: Ω −→ R^2
       ω 7−→ C(ω)

C(ω)estdelaforme(x,y).On peutdéfinirdeuxstatistiquessimplesàpartirdeC

Première{ statistiquemarginale
X: Ω −→ R
ω 7−→ lapremièrevaleurducoupleC(ω)

Seconde{ statistiquemarginale
Y : Ω −→ R
ω 7−→ lasecondevaleurducoupleC(ω)

Parabusdelangage,onécritqueC= (X,Y).


#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

 
LesensemblesdesvaleursobservablesdeXetY sontfinis.On peutécrire:
 
 
X(Ω) ={x 1 ,x 2 ,...,xp} parordrecroissant
 
 
Y(Ω) ={y 1 ,y 2 ,...,xq} parordrecroissant
 
avec 1 ≤p≤N, 1 ≤q≤Netapriorip 6 =q

Effectifsetfréquences

- Effectifnij = #(C−^1 {(xi,yj)}): nombred'individus admettant (xi,yj)commevaleurdu
caractèreC
- Effectifni• = #(X−^1 {xi}): nombred'individusadmettant xi commepremièrevaleurdu
caractèreC ounombred'individusadmettantxicommevaleurducaractèreX
    Remarque:ni•=

#### ∑

 
1 ≤j≤qnij
 
- Effectifn•j = #(Y−^1 {yj}): nombre d'individus admettantyj commeseconde valeurdu
caractèreC ounombred'individusadmettantyjcommevaleurducaractèreY
    Remarque:n•j=

#### ∑

 
1 ≤i≤pnij
 
OndéfinitégalementleseffectifscumulésNi•etN•jainsiquelesfréquencesfij,fi•,f•j,Fi•et
F•j endivisantleseffectifscorres pondantsparN.Ainsi,parexemple

 
fij=
 
#### 1

#### N

 
nij
 

#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

 
Tableaudecontingence
 
 
X\Y y 1 ... yj ... yq total
x 1 n 11 ... n 1 j ... n 1 q n 1 •
..
.
 
#### ..

#### .

#### ..

#### .

#### ..

#### .

#### ..

#### .

 
xi ni 1 ... nij ... niq ni•
..
.
 
#### ..

#### .

#### ..

#### .

#### ..

#### .

#### ..

#### .

 
xp np 1 ... npj ... npj n 1 •
total n• 1 ... n•j ... n•q N
 
 
X\Y y 1 ... yj ... yq total
x 1 f 11 ... f 1 j ... f 1 q f 1 •
..
.
 
#### ..

#### .

#### ..

#### .

#### ..

#### .

#### ..

#### .

 
xi fi 1 ... fij ... fiq fi•
..
.
 
#### ..

#### .

#### ..

#### .

#### ..

#### .

#### ..

#### .

 
xp fp 1 ... fpj ... fpj f 1 •
total f• 1 ... f•j ... f•q 1
 

#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.3.2 Covarianceetco ecientdecorrélation

Covariance
ElledonneunemesuredulienexistantentrelesdeuxcaractèresXetY.

 
cov(X,Y) =σXY =
 
#### (

#### 1

#### N

 
∑p
 
 
i=
 
 
∑q
 
 
j=
 
 
nijxiyj
 
#### )

 
−xy=
 
#### 1

#### N

 
∑p
 
 
i=
 
 
∑q
 
 
j=
 
 
nij(xi−x)(yj−y)
 
Si les deux caractères sont indé pendants l'un de l'autre alors la covariance est nulle.
Récipro quefausse.

Co ecientdecorrélation
C'estunenormalisationdelacovariancequiéviteleseffetsd'échelle.

 
ρXY =
 
 
σXY
σXσY
 
- − 1 ≤ρXY ≤ 1
- SiXetY sontindé pendantsalorsρXY = 0.Récipro quefausse.
- S'ilexisteunerelationaneentreXetY alorsρXY =± 1 .Récipro quefausse.


#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.3.3 Droitederégressionlinéaire

DroitederégressiondeYenX
Onchercheladroited'équationY =aX+bappro chant"aumieux"lenuagede pointsdela
statistiquedoubleC.



 

 
 
a=
 
 
σXY
σX^2
b=y−
 
 
σXY
σ^2 X
 
 
x
 
Cettedroitepasseparle point(x,y)

DroitederégressiondeXenY
Onchercheladroited'équationX=αY +βappro chant"aumieux"lenuagede pointsdela
statistiquedoubleC.



 

 
 
α=
 
 
σXY
σ^2 Y
β=x−
 
 
σXY
σ^2 Y
 
 
y
 
Cettedroitepasseaussiparle point(x,y)

Lesdeuxdroitessontconfonduesssia=

#### 1

 
α
 
 
ssi
 
 
σXY^2
σ^2 Xσ^2 Y
 
 
= 1ssiρ^2 XY = 1
 

#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.3.4 Régressionlogarithmique

Lorsque le nuagede points nesemble pasrectiligne, on  peutchercher d'autres ty pe de
relationentreXetY,toutens'appuyantsurlatechniquedelarégressionlinéaire.

Sionsoup çonneunerelationdelaformeY =βXα
Enpassantaulogarithme,larelationdevient:ln(Y) = ln(β) +α·ln(X)
Oncalculealorsladroitederégressionsurlecouple(X′,Y′) = (ln(X),ln(Y))
SilerésultatestY′=A·X′+Betqueleco ecientdecorrélationestsatisfaisant
AlorsonadmetqueY 'eB·XA(i.e.β=eBetα=A)

Sionsoup çonneunerelationdelaformeY =βαX
Enpassantaulogarithme,larelationdevient:ln(Y) = ln(β) + ln(α)·X
Oncalculealorsladroitederégressionsurlecouple(X′,Y′) = (X,ln(Y))
SilerésultatestY′=A·X′+Betqueleco ecientdecorrélationestsatisfaisant
AlorsonadmetqueY 'eB·(eA)X(i.e.β=eBetα=eA)


#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.3.5 Régression polynomiale

Y = (x 1 ,x 2 ,...,xN)etY = (y 1 ,y 2 ,...,yn)
Onchercheunerelationdelaformeyi'P(xi)oùP(x) =

 
∑n
k=0akx
 
 
k
 
On poseSk=

#### ∑N

 
i=1x
 
 
k
i (=N·mk(X))etTk=
 
#### ∑N

 
i=1yix
 
k
i
SoitM lamatricecarréed'ordren+ 1définiepar:[M]`,c=S`+c− 2
SoitBlevecteurt(T 0 ,T 1 ,...,Tn)
EtsoitAlevecteurd'inconnuest(a 0 ,a 1 ,...,an)

AestsolutiondusystèmeM·A=B

 -->
