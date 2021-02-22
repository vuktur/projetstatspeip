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
- $C$ : ensemble des valeurs possibles du caractère, appelées aussi modalités.
- $X$ : Statistique (parfois appelée aussi caractère). Application qui à tout individu associe la
valeur de son caractère.
<!---->
- Une statistique peut être quantitative ou qualitative.
- Une statistique quantitative peut être discrète ou continue.
- Une statistique peut être multiple (à n paramètres).

### 1.2 Statistique simple (univariée)

#### 1.2.1 Notations

On va se limiter à des statistiques quantitatives.

- Ω population finie de $N$ individus.
- $C \subset R$

**Première représentation :** Une série statistique est un $N$-uplet $X= (v_1,\,v_2,\,...,\,v_N)$  

**Par exemple :** $X= (2.1,\,5.23,\,0.61,\,2.1,\,7.2,\,0.61)$

On parle alors de **série statistique brute**.

**Seconde représentation :**
→L'ensembledesvaleursobservablesdeXestni.Onp eutécrire:

```
X(Ω) ={x 1 ,x 2 ,...,xp} (1≤p≤N)
```
p ourlasuiteonsupp oserax 1 < x 2 < ... < xp.

- Eectifni= #(X−^1 {xi}):nombredefoisquelavaleurxiaétéobservéedanslap opulation
ounombred'individusadmettantxicommevaleurducaractère.
- EectifcumuléNi =

```
∑i
j=1nj = #(X
```
− (^1) {]−∞,x
i]}): nombred'individusprésentantune
valeurdecaractèreplusp etitequexi,ouégale.OnalarelationNi=Ni− 1 +nienp osant


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

N 0 = 0etp eutremarquerqueNp=N

- Fréquencefi=ni/N.
- FréquencecumuléeFi=Ni/N=

∑i
j=1fj =Fi−^1 +fienp osantF^0 = 0.Onremarqueque
Fp= 1

- Unesériestatistiqueestunefamilledelaforme(xi,ni)i∈J 1 ,pKou(xi,fi)i∈J 1 ,pK
Onparle parfoisdesérie statistique dép ouilléeou desérie statistique regroup ée et
ordonnée..


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.2 Paramètresdep osition

Lemo de
C'estlavaleurducaractèred'eectifmaximal

```
mode = xitqni= max
1 ≤j≤p
```
```
(nj)
```
Attention:iln'estpasforcémentunique.

Lamédiane
C'estlavaleurducaractèrequiséparelap opulationendeuxpartieségales.
Attention:parfoisdicileàdénir.

```
ηtq#{ωi|X(ωi)< η}= #{ωi|X(ωi)> η}
```
```
ηtq#{ωi|X(ωi)≤η}= #{ωi|X(ωi)≥η}
η=xitqNi− 1 < N/ 2 ≤Ni
```

#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

Lesquantiles
Danslemêmeesprit,onp eutdénir

- lesquartiles: 3 valeursquidécoup entlap opulationen 4 partieségales.Ledeuxièmequartile
étantalorségalàlamédiane
- lesdéciles: 9 valeursquidécoup entlap opulationen 10 partieségales.
- lescentiles: 99 valeursquidécoup entlap opulationen 100 partieségales.
- outoutautredécoupage.

Lamoyennearithmétique

```
m(X) =x=
```
#### 1

#### N

```
∑p
```
```
i=
```
```
(nixi) =
```
```
∑p
```
```
i=
```
```
(fixi) =
```
#### 1

#### N

#### ∑N

```
i=
```
```
vi
```
Remarque:sionp osen=(n 1 ,n 2 ,...np)etX=(x 1 ,x 2 ,...xp)alors

```
∑p
```
```
i=
```
```
(nixi) = n·Xt et m(X) =
```
#### 1

#### N

```
n·Xt
```

#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.3 Paramètresdedisp ersion

L'étendue
C'estlaplagedevaleurducaractèreobservéesurlap opulation

```
w= max
1 ≤i≤p
```
```
(xi)−min
1 ≤i≤p
```
```
(xi) = max
1 ≤i≤N
```
```
(vi)− min
1 ≤i≤N
```
```
(vi)
```
Attention:sensibleauxerreursdemesure.

Lesquantiles
Danslemêmeordred'idéequel'étendue,onp eutdonnerl'intervalleséparantleplusp etitet
le plus granddécile(80% delap opulation) ou celui séparant lequartile inférieurQI etle
quartile sup érieur QS (50% de la p opulation) ou tout autre intervalle déni de manière
similaire.

Intérêt:Éliminelesmesuresab errantes.

L'écartarithmétiquemoyen
Calculelamoyennedesécartsàlamoyenne

```
E=
```
#### 1

#### N

#### ∑

```
1 ≤i≤p
```
```
ni|xi−x|=
```
#### ∑

```
1 ≤i≤p
```
```
fi|xi−x|=
```
#### 1

#### N

#### ∑

```
1 ≤i≤N
```
```
|vi−x|
```
p euutilisé.


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

L'écartquadratiquemoyenouvariance
Calculelamoyennedescarrésdesécartsàlamoyenne

```
V(X) =σ^2 X=
```
#### 1

#### N

#### ∑

```
1 ≤i≤p
```
```
ni(xi−x)^2 =
```
#### ∑

```
1 ≤i≤p
```
```
fi(xi−x)^2 =
```
#### 1

#### N

#### ∑

```
1 ≤i≤N
```
```
(vi−x)^2
```
RelationdeKo enig-Huygens

```
σX^2 =
```
#### (

#### 1

#### N

#### ∑

```
1 ≤i≤p
```
```
ni.x^2 i
```
#### )

```
−x^2 =
```
#### (

#### ∑

```
1 ≤i≤p
```
```
fi.x^2 i
```
#### )

```
−x^2 =
```
#### (

#### 1

#### N

#### ∑

```
1 ≤i≤N
```
```
vi^2
```
#### )

```
−x^2
```
L'écarttyp e
C'estlaracinecarrédelavariance:mêmedimensionquelecaractèreétudié.

```
σX=
```
#### √

#### V(X) =

#### √

#### 1

#### N

#### ∑

```
1 ≤i≤p
```
```
ni(xi−x)^2 =
```
#### √

#### √

#### √

#### √

#### (

#### ∑

```
1 ≤i≤p
```
```
fi.x^2 i
```
#### )

```
−x^2 =...
```

#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.4 Lesmoments

Momentd'ordrek

```
mk(X) =
```
#### 1

#### N

```
∑p
```
```
i=
```
```
(ni.xki) =
```
```
∑p
```
```
i=
```
```
(fi.xki) =
```
#### 1

#### N

#### ∑N

```
i=
```
```
vik
```
Momentcentréd'ordrek

```
μk(X) =
```
#### 1

#### N

```
∑p
```
```
i=
```
```
(ni.(xi−x)k) =
```
```
∑p
```
```
i=
```
```
(fi.(xi−x)k) =
```
#### 1

#### N

#### ∑N

```
i=
```
```
(vi−x)k
```
Propriétés:

- m 0 (X) =μ 0 (X) = 1
- m 1 (X) =xetμ 1 (X) = 0
- μ 2 (X) =σX^2
- σ^2 X=m 2 (X)−m 1 (X)^2 (RelationdeKo enig-Huygens)
- Siunesériestatistique estsymétrique parrapp ortàsa moyennealors toussesmoments
centrésd'ordreimpairsontnuls.
- Par contre il ne sut pas de vérier que μ 3 (X) = 0 p our conclure que la série est
symétriqueparrapp ortàsamoyenne.


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.5 Paramètresdeformes

Premierco ecientdeFisher:co ecientd'asymétrie

```
δ=
```
```
μ 3
σ^3
```
#### =

```
μ 3
μ^32 /^2
```
- sériesymétrique→δ= 0
- grandsécartsp ositifs%àlamoyenne→δ > 0 ("b ossedécaléeverslagauche")
- grandsécartsnégatifs%àlamoyenne→δ < 0 ("b ossedécaléeversladroite")
- leco ecientd'asymétrieestconsidérécommesignicatiflorsque|δ|> 0 , 5
- S'appliqueessentiellementàunesérieunimo dale.

Secondco ecientdeFisher:co ecientd'aplatissement

```
a=
```
```
μ 4
σ^4
```
#### =

```
μ 4
μ^22
```
- Unegrandevaleurdeatraduitunresserrementautourdelamoyenne("courb eenpic")
- Unep etitevaleurdeatraduitunétalementdelasérie("courb eplate")
- Siladistributionestnormalealorsa=
- S'appliqueessentiellementàunesérieunimo dale.


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.6 Découpageenclasses

LorsqueXestuncaractèrecontinuouquelesfréquencesfisontfaibles(ppro chedeN)
onestamenéàdécoup erledomainedevaleursdeXenclasses(sous-intervalles).

```
C 1 = [a 0 ,a 1 ],C 2 =]a 1 ,a 2 ],...,Cp′=]ap′− 1 ,ap′]
```
avecp′≤peta 0 ≤x 1 < xp≤ap′

Intérêt :Représentationgraphique(histogramme)etmiseenévidenced'uneclassemo dale
(classedehauteurmaximaledansl'histogramme)
→Lesclassesp euventêtreéventuellementdelargeursdiérentes.

- Onnotealorsnil'eectifdelaclasseCi:ni= #{X−^1 ]ai− 1 ,ai]}.
- Onp eut ensuitedénirNi, fi et Fi commevu précédemmentp ourune sériestatistique
dép ouillée.

Lasérieestalorsdonnéesouslaformedelafamille((n 1 ,C 1 ),(n 2 ,C 2 ),...(np′,Cp′))
On parle alors d'une série statistique en classes ou regroup ée en classes ou encore,
parfois,classée.

- Àtoutesérieclasséeonp eutfairecorresp ondreunesériestatistiquedép ouillée(x′i,ni)i∈J 1 ,p′K
oùx′iestlecentredelaclasseCi(x′i= (ai− 1 +ai)/ 2 ).


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.7 Histogramme

Lorsquelastatistiqueestdécoup éeenclasses,onnelareprésenteplusparundiagramme
enbâtons,maisparunhistogramme.Chaqueclasseestreprésentéeparunrectangledontla
baseestprop ortionnelleàlalargeurdelaclasseetlasurfaceprop ortionnelleàl'eectif(ou,
cequirevientaumême,àlafréquence)delaclasse.C'estbienlasurfaceetnonlahauteurdu
rectangle qui est prop ortionnelle à l'eectif. Cette remarque prend toute son imp ortance
lorsquelesclassessontdelargeursdiérentes.


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

Exemple:ontravaillesurunestatistiquedécoup éesselon lesquatreclasses suivantes:
[2,4],]4,9],]9,11],]11,12]etchaqueclasseestd'eectif4.
L'axedesordonnéesp eutêtrevucommeunedensité.


#### 1.2. STATISTIQUESIMPLE(UNIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.2.8 Laclassemo dale(paramètre dep osition)

C'estlaclassecorresp ondantaurectangleleplushautdansl'histogramme(onparlebien
icidehauteuretnondesurface).Ellep eutnepasêtreunique.Ilarrivequ'ondénisselemo de
delastatistiquecommelemilieudelaclassemo dale(cettedénitionn'estpasentièrement
équivalenteàcelledonnéeplushaut).Dansl'exempleprécédent,laclassemo daleestladernière
(classe]11,12])etlemo deest11,5.


#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

## 1.3 Statistique double (bivariée)

### 1.3.1 Notations

```
Onvaselimiteràdesstatistiquesquantitatives.
```
- Ωp opulationniedeNindividus.
- {UnestatistiquedoubleC estuneapplicationdeΩdansR^2.
    C: Ω −→ R^2
       ω 7−→ C(ω)

C(ω)estdelaforme(x,y).Onp eutdénirdeuxstatistiquessimplesàpartirdeC

Première{ statistiquemarginale
X: Ω −→ R
ω 7−→ lapremièrevaleurducoupleC(ω)

Seconde{ statistiquemarginale
Y : Ω −→ R
ω 7−→ lasecondevaleurducoupleC(ω)

Parabusdelangage,onécritqueC= (X,Y).


#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

```
LesensemblesdesvaleursobservablesdeXetY sontnis.Onp eutécrire:
```
```
X(Ω) ={x 1 ,x 2 ,...,xp} parordrecroissant
```
```
Y(Ω) ={y 1 ,y 2 ,...,xq} parordrecroissant
```
avec 1 ≤p≤N, 1 ≤q≤Netapriorip 6 =q

Eectifsetfréquences

- Eectifnij = #(C−^1 {(xi,yj)}): nombred'individus admettant (xi,yj)commevaleurdu
caractèreC
- Eectifni• = #(X−^1 {xi}): nombred'individusadmettant xi commepremièrevaleurdu
caractèreC ounombred'individusadmettantxicommevaleurducaractèreX
    Remarque:ni•=

#### ∑

```
1 ≤j≤qnij
```
- Eectifn•j = #(Y−^1 {yj}): nombre d'individus admettantyj commeseconde valeurdu
caractèreC ounombred'individusadmettantyjcommevaleurducaractèreY
    Remarque:n•j=

#### ∑

```
1 ≤i≤pnij
```
OndénitégalementleseectifscumulésNi•etN•jainsiquelesfréquencesfij,fi•,f•j,Fi•et
F•j endivisantleseectifscorresp ondantsparN.Ainsi,parexemple

```
fij=
```
#### 1

#### N

```
nij
```

#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

```
Tableaudecontingence
```
```
X\Y y 1 ... yj ... yq total
x 1 n 11 ... n 1 j ... n 1 q n 1 •
..
.
```
#### ..

#### .

#### ..

#### .

#### ..

#### .

#### ..

#### .

```
xi ni 1 ... nij ... niq ni•
..
.
```
#### ..

#### .

#### ..

#### .

#### ..

#### .

#### ..

#### .

```
xp np 1 ... npj ... npj n 1 •
total n• 1 ... n•j ... n•q N
```
```
X\Y y 1 ... yj ... yq total
x 1 f 11 ... f 1 j ... f 1 q f 1 •
..
.
```
#### ..

#### .

#### ..

#### .

#### ..

#### .

#### ..

#### .

```
xi fi 1 ... fij ... fiq fi•
..
.
```
#### ..

#### .

#### ..

#### .

#### ..

#### .

#### ..

#### .

```
xp fp 1 ... fpj ... fpj f 1 •
total f• 1 ... f•j ... f•q 1
```

#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.3.2 Covarianceetco ecientdecorrélation

Covariance
ElledonneunemesuredulienexistantentrelesdeuxcaractèresXetY.

```
cov(X,Y) =σXY =
```
#### (

#### 1

#### N

```
∑p
```
```
i=
```
```
∑q
```
```
j=
```
```
nijxiyj
```
#### )

```
−xy=
```
#### 1

#### N

```
∑p
```
```
i=
```
```
∑q
```
```
j=
```
```
nij(xi−x)(yj−y)
```
Si les deux caractères sont indép endants l'un de l'autre alors la covariance est nulle.
Récipro quefausse.

Co ecientdecorrélation
C'estunenormalisationdelacovariancequiéviteleseetsd'échelle.

```
ρXY =
```
```
σXY
σXσY
```
- − 1 ≤ρXY ≤ 1
- SiXetY sontindép endantsalorsρXY = 0.Récipro quefausse.
- S'ilexisteunerelationaneentreXetY alorsρXY =± 1 .Récipro quefausse.


#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.3.3 Droitederégressionlinéaire

DroitederégressiondeYenX
Onchercheladroited'équationY =aX+bappro chant"aumieux"lenuagedep ointsdela
statistiquedoubleC.



```

```
```
a=
```
```
σXY
σX^2
b=y−
```
```
σXY
σ^2 X
```
```
x
```
Cettedroitepasseparlep oint(x,y)

DroitederégressiondeXenY
Onchercheladroited'équationX=αY +βappro chant"aumieux"lenuagedep ointsdela
statistiquedoubleC.



```

```
```
α=
```
```
σXY
σ^2 Y
β=x−
```
```
σXY
σ^2 Y
```
```
y
```
Cettedroitepasseaussiparlep oint(x,y)

Lesdeuxdroitessontconfonduesssia=

#### 1

```
α
```
```
ssi
```
```
σXY^2
σ^2 Xσ^2 Y
```
```
= 1ssiρ^2 XY = 1
```

#### 1.3. STATISTIQUEDOUBLE(BIVARIÉE)CHAPITRE1. STATISTIQUESDESCRIPTIVES

### 1.3.4 Régressionlogarithmique

Lorsque le nuagedep oints nesemble pasrectiligne, on p eutchercher d'autres typ e de
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

### 1.3.5 Régressionp olynomiale

Y = (x 1 ,x 2 ,...,xN)etY = (y 1 ,y 2 ,...,yn)
Onchercheunerelationdelaformeyi'P(xi)oùP(x) =

```
∑n
k=0akx
```
```
k
```
Onp oseSk=

#### ∑N

```
i=1x
```
```
k
i (=N·mk(X))etTk=
```
#### ∑N

```
i=1yix
```
k
i
SoitM lamatricecarréed'ordren+ 1déniepar:[M]`,c=S`+c− 2
SoitBlevecteurt(T 0 ,T 1 ,...,Tn)
EtsoitAlevecteurd'inconnuest(a 0 ,a 1 ,...,an)

AestsolutiondusystèmeM·A=B


