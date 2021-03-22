# Statistiques descriptives

## 1.1 Généralités

Une statistique est une application d'une population <img src="/svgs/9432d83304c1eb0dcb05f092d30a767f.svg?invert_in_darkmode" align=middle width=11.87217899999999pt height=22.465723500000017pt/> vers un ensemble de valeurs <img src="/svgs/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode" align=middle width=12.92464304999999pt height=22.465723500000017pt/>.

<p align="center"><img src="/svgs/816e5284cdfa5b04058a245bc2516b9f.svg?invert_in_darkmode" align=middle width=135.93580935pt height=39.452455349999994pt/></p>

- <img src="/svgs/9432d83304c1eb0dcb05f092d30a767f.svg?invert_in_darkmode" align=middle width=11.87217899999999pt height=22.465723500000017pt/> : population finie d'individus <img src="/svgs/ae4fb5973f393577570881fc24fc2054.svg?invert_in_darkmode" align=middle width=10.82192594999999pt height=14.15524440000002pt/>. On va mesurer/observer un caractère particulier sur ces individus.  
    >`population`  

- <img src="/svgs/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode" align=middle width=12.92464304999999pt height=22.465723500000017pt/> : ensemble des valeurs possibles du caractère, appelées aussi modalités.  
    >`modalites`  

- <img src="/svgs/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode" align=middle width=14.908688849999992pt height=22.465723500000017pt/> : Statistique (parfois appelée aussi caractère). Application qui à tout individu associe la valeur de son caractère.  
    >`serie`  

<!---->
- Une statistique peut être quantitative ou qualitative.
- Une statistique quantitative peut être discrète ou continue.
- Une statistique peut être multiple (à n paramètres).

## 1.2 Statistique simple (univariée)

### 1.2.1 Notations

On va se limiter à des statistiques quantitatives.

- <img src="/svgs/9432d83304c1eb0dcb05f092d30a767f.svg?invert_in_darkmode" align=middle width=11.87217899999999pt height=22.465723500000017pt/> population finie de <img src="/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.99998994999999pt height=22.465723500000017pt/> individus.
- <img src="/svgs/e3bb5bfea0152a88315d1a74ba447c5e.svg?invert_in_darkmode" align=middle width=47.45074124999999pt height=22.465723500000017pt/>

#### **Première représentation :**

Une série statistique est un <img src="/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.99998994999999pt height=22.465723500000017pt/>-uplet <img src="/svgs/306fce9f96a39e508d3b04ae388780bc.svg?invert_in_darkmode" align=middle width=137.2623186pt height=24.65753399999998pt/>  
Par exemple : <img src="/svgs/a72b37518a0a1f2b05175c7133b14a49.svg?invert_in_darkmode" align=middle width=250.52492684999996pt height=24.65753399999998pt/>  
On parle alors de **série statistique brute**.

#### **Seconde représentation :**

L'ensemble des valeurs observables de <img src="/svgs/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode" align=middle width=14.908688849999992pt height=22.465723500000017pt/> est fini. On peut écrire :

<p align="center"><img src="/svgs/27aadf1542a4776b41fbb0c0e8d8f247.svg?invert_in_darkmode" align=middle width=257.6605416pt height=17.031940199999998pt/></p>

pour la suite on supposera <img src="/svgs/732e682517452adfd4dff74f020455bf.svg?invert_in_darkmode" align=middle width=129.16192575pt height=17.723762100000005pt/>.

- Effectif <img src="/svgs/a01d1b2597aed9929188ca3cf36f56aa.svg?invert_in_darkmode" align=middle width=110.07910319999999pt height=29.190975000000005pt/> : nombre de fois que la valeur <img src="/svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode" align=middle width=14.045887349999989pt height=14.15524440000002pt/> a été observée dans la population ou nombre d'individus admettant <img src="/svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode" align=middle width=14.045887349999989pt height=14.15524440000002pt/> comme valeur du caractère.  
    >`effectif(i)`  

- Effectif cumulé <img src="/svgs/6ef99c2fbff3789cb37df634de7cbe14.svg?invert_in_darkmode" align=middle width=229.75649399999995pt height=31.75825949999999pt/> : nombre d'individus présentant une valeur de caractère plus petite que <img src="/svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode" align=middle width=14.045887349999989pt height=14.15524440000002pt/>, ou égale. On a la relation <img src="/svgs/9c2336b85a1d77d777cee5ba4d0a2a61.svg?invert_in_darkmode" align=middle width=100.44026849999999pt height=22.465723500000017pt/> en posant <img src="/svgs/44b33ca837e30e13d9658b47036b4e43.svg?invert_in_darkmode" align=middle width=50.71906784999999pt height=22.465723500000017pt/> et peut remarquer que <img src="/svgs/c817eca814074b3f0b81676561387597.svg?invert_in_darkmode" align=middle width=57.723763349999984pt height=22.465723500000017pt/>  
    >`effectifC(i)`  

- Fréquence <img src="/svgs/c5583eb3f88ed4af35d4022a0b001bf8.svg?invert_in_darkmode" align=middle width=73.08404234999999pt height=24.65753399999998pt/>.  
    >`frequence(i)`  

- Fréquence cumulée <img src="/svgs/fc40cb104f4f52a357f0352112cd8581.svg?invert_in_darkmode" align=middle width=236.80521314999996pt height=31.75825949999999pt/> en posant <img src="/svgs/aeb792c734d2b6ac8b5ccc2392cc384a.svg?invert_in_darkmode" align=middle width=48.08209724999998pt height=22.465723500000017pt/>. On remarque que <img src="/svgs/5ee293bd08b56b52d49f2ed4e4e40efb.svg?invert_in_darkmode" align=middle width=48.30601379999999pt height=22.465723500000017pt/>  
    >`frequenceC(i)`  

Une série statistique est une famille de la forme <img src="/svgs/e08ca08c779b851a20348c1215511b88.svg?invert_in_darkmode" align=middle width=88.48429259999997pt height=24.65753399999998pt/> ou <img src="/svgs/a72651d020c44198566a79091b782a44.svg?invert_in_darkmode" align=middle width=86.66540354999998pt height=24.65753399999998pt/>  
On parle parfois de **série statistique dépouillée** ou de **série statistique regroupée et ordonnée**.

### 1.2.2 Paramètres de position

#### **Le mode**

C'est la valeur du caractère d'effectif maximal  
>`mode`  

<p align="center"><img src="/svgs/bd82aeee09fd7f9f89e5248ebf1f1198.svg?invert_in_darkmode" align=middle width=208.2415797pt height=25.1935035pt/></p>

Attention : il n'est pas forcément unique.

#### **La médiane**

C'est la valeur du caractère qui sépare la population en deux parties égales.  
Attention : parfois dificile à définir.  
>`mediane`  

<p align="center"><img src="/svgs/93ab49d67867cce6c408da99c54c8235.svg?invert_in_darkmode" align=middle width=821.77889475pt height=16.438356pt/></p>

#### **Les quantiles**

Dans le même esprit, on peut définir :

- les quartiles : 3 valeurs qui découpent la population en 4 parties égales. Le deuxième quartile étant alors égal à la médiane.
- les déciles : 9 valeurs qui découpent la population en 10 parties égales.
- les centiles : 99 valeurs qui découpent la population en 100 parties égales.
- ou tout autre découpage.

>`quantile(n)`  

#### **La moyenne arithmétique**

<p align="center"><img src="/svgs/ce40a5369133d61caa40c4beb743b41f.svg?invert_in_darkmode" align=middle width=353.32083435pt height=47.806078649999996pt/></p>
>`moyenne`  
Remarque : si on pose <img src="/svgs/7685763f4490468237d95f4d0979209e.svg?invert_in_darkmode" align=middle width=133.04728139999997pt height=24.65753399999998pt/> et <img src="/svgs/dc22bdb0ee16a1b736295db4ad0bca79.svg?invert_in_darkmode" align=middle width=136.67340554999998pt height=24.65753399999998pt/> alors :
<p align="center"><img src="/svgs/f762ac4295d4bc1d55e719963c9df35a.svg?invert_in_darkmode" align=middle width=280.3509027pt height=45.67365495pt/></p>

### 1.2.3 Paramètres de dispersion

#### **L'étendue**

C'est la plage de valeur du caractère observée sur la population :
<p align="center"><img src="/svgs/39b4e0b84a65070d92fdfc266955a245.svg?invert_in_darkmode" align=middle width=333.13530525pt height=25.1935035pt/></p>
>`etendue`  
Attention : sensible aux erreurs de mesure.

#### **Les intervalles interquantiles**

Dans le même ordre d'idée que l'étendue, on peut donner l'intervalle séparant le plus petit et
le plus grand décile (80% de la population) ou celui séparant le quartile inférieur <img src="/svgs/7489a81e11a84e87ad3fdb840ce3a3fa.svg?invert_in_darkmode" align=middle width=19.71579389999999pt height=22.465723500000017pt/> et le
quartile supérieur <img src="/svgs/8739b5fc531248a9c6865293033d1264.svg?invert_in_darkmode" align=middle width=21.69637634999999pt height=22.465723500000017pt/> (50% de la population) ou tout autre intervalle définie de manière
similaire.  

Intérêt : Élimine les mesures aberrantes.

#### **L'écart arithmétique moyen** *(peu utilisé)*

Calcule la moyenne des écarts à la moyenne.
<p align="center"><img src="/svgs/f65690ad72dcf7e6fcf35a4fe8b7d401.svg?invert_in_darkmode" align=middle width=373.62640754999995pt height=43.6202118pt/></p>
>`ecartMoyen`  

#### **L'écart quadratique moyen ou variance**

Calcule la moyenne des carrés des écarts à la moyenne.
<p align="center"><img src="/svgs/7d4012064076fd01288d3a4d08f4766e.svg?invert_in_darkmode" align=middle width=474.8084847pt height=43.6202118pt/></p>
>`variance`  

Relation de Koenig-Huygens
<p align="center"><img src="/svgs/71d04426b4624018085735f21b38a11c.svg?invert_in_darkmode" align=middle width=552.95186265pt height=59.1786591pt/></p>

#### **L'écart type**

C'est la racine carré de la variance : même dimension que le caractère étudié.
<p align="center"><img src="/svgs/453f55182660ce930e8d58277da7f275.svg?invert_in_darkmode" align=middle width=486.19555875pt height=69.0417915pt/></p>
>`ecartType`  

### 1.2.4 Les moments

#### **Moment d'ordre k**

<p align="center"><img src="/svgs/7a130c5d59b510e4373c4832a9116a64.svg?invert_in_darkmode" align=middle width=362.2753464pt height=45.67365495pt/></p>
>`moment(k)`  

#### **Moment centré d'ordre k**

<p align="center"><img src="/svgs/a8b10e6a9b072c10852c1f5ad6468934.svg?invert_in_darkmode" align=middle width=497.65089659999995pt height=45.67365495pt/></p>
>`momentCentre(k)`  

Propriétés:

- <img src="/svgs/d8e1d3bac861a040392dd3a4478b168e.svg?invert_in_darkmode" align=middle width=146.52961455pt height=24.65753399999998pt/>
- <img src="/svgs/5f92764b030280f42a52e9af1374635e.svg?invert_in_darkmode" align=middle width=180.582138pt height=24.65753399999998pt/>
- <img src="/svgs/ed8038b2e69eef21110e701807f3b27a.svg?invert_in_darkmode" align=middle width=87.95894744999998pt height=26.76175259999998pt/>
- <img src="/svgs/ce755bdd712efce1b6caa5ca3469daac.svg?invert_in_darkmode" align=middle width=149.36322719999998pt height=26.76175259999998pt/> (Relation de Koenig-Huygens)
- Si une série statistique est symétrique par rapport à sa moyenne alors tous ses moments centrés d'ordre impair sont nuls.
- Par contre il ne sufft pas de vérifier que <img src="/svgs/daf6602f8c2e83b9a173db6e6b03d1e5.svg?invert_in_darkmode" align=middle width=75.11032484999998pt height=24.65753399999998pt/> pour conclure que la série est symétrique par rapport à sa moyenne.

### 1.2.5 Paramètres de formes

#### **Premier coeffcient de Fisher : coeffcient d'asymétrie**

<p align="center"><img src="/svgs/cb3e478992ac3cd014877484c6320f57.svg?invert_in_darkmode" align=middle width=105.60552089999999pt height=37.94230605pt/></p>
>`asymetrie()`  

- série symétrique <img src="/svgs/c2e5ae93c3285eed27016a596aac766e.svg?invert_in_darkmode" align=middle width=59.06941424999998pt height=22.831056599999986pt/>
- grands écarts positifs % à la moyenne <img src="/svgs/e43ff65ce143920f52e00f636f3b19cc.svg?invert_in_darkmode" align=middle width=59.06941424999998pt height=22.831056599999986pt/> ("bosse décalée vers la gauche")
- grands écarts négatifs % à la moyenne <img src="/svgs/758b6909fa7d2f54c42fd40119748456.svg?invert_in_darkmode" align=middle width=59.06941424999998pt height=22.831056599999986pt/> ("bosse décalée vers la droite")
- le coeffcient d'asymétrie est considéré comme significatif lorsque <img src="/svgs/8ef4aeac9b67a9a87122a3673729f803.svg?invert_in_darkmode" align=middle width=59.98279319999999pt height=24.65753399999998pt/>
- S'applique essentiellement à une série unimodale.

#### **Second coeffcient de Fisher : coeffcient d'aplatissement**

<p align="center"><img src="/svgs/e83a22a4c47a0104d6c7ae7f11be1ec1.svg?invert_in_darkmode" align=middle width=94.96623344999999pt height=33.85762545pt/></p>
>`aplatissement()`  

- Une grande valeur de <img src="/svgs/c745b9b57c145ec5577b82542b2df546.svg?invert_in_darkmode" align=middle width=10.57650494999999pt height=14.15524440000002pt/> traduit un resserrement autour de la moyenne ("courbe en pic")
- Une petite valeur de <img src="/svgs/c745b9b57c145ec5577b82542b2df546.svg?invert_in_darkmode" align=middle width=10.57650494999999pt height=14.15524440000002pt/> traduit un étalement de la série ("courbe plate")
- Si la distribution est normale alors <img src="/svgs/123bc99947b62e73c7e949812274cfda.svg?invert_in_darkmode" align=middle width=40.713337499999994pt height=21.18721440000001pt/>
- S'applique essentiellement à une série unimodale.

### 1.2.6 Découpage en classes

Lorsque <img src="/svgs/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode" align=middle width=14.908688849999992pt height=22.465723500000017pt/> est un caractère continu ou que les fréquences <img src="/svgs/9b6dbadab1b122f6d297345e9d3b8dd7.svg?invert_in_darkmode" align=middle width=12.69888674999999pt height=22.831056599999986pt/> sont faibles (<img src="/svgs/2ec6e630f199f589a2402fdf3e0289d5.svg?invert_in_darkmode" align=middle width=8.270567249999992pt height=14.15524440000002pt/> proche de <img src="/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.99998994999999pt height=22.465723500000017pt/>) on est amené à découper le domaine de valeurs de <img src="/svgs/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode" align=middle width=14.908688849999992pt height=22.465723500000017pt/> en classes (sous-intervalles).  
>`classer([limites des classes])`  

<p align="center"><img src="/svgs/0cad4d52130e0f91e2bab2bd87511ed9.svg?invert_in_darkmode" align=middle width=316.78013565pt height=17.031940199999998pt/></p>
avec <img src="/svgs/0ee177bdbe85037fed8cd7195b0eb778.svg?invert_in_darkmode" align=middle width=43.07063969999999pt height=24.7161288pt/> et <img src="/svgs/55afe0e28373190feca14b7d25a55f3e.svg?invert_in_darkmode" align=middle width=134.6694096pt height=20.908638300000003pt/>

**Intérêt :** Représentation graphique (histogramme) et mise en évidence d'une classe modale (classe de hauteur maximale dans l'histogramme)  
<img src="/svgs/e5d134f35dc4949fab12ec64d186248a.svg?invert_in_darkmode" align=middle width=16.43840384999999pt height=14.15524440000002pt/> Les classes peuvent être éventuellement de largeurs différentes.

- On note alors <img src="/svgs/de3e4ddbaf93c2db6b330ad1998cc995.svg?invert_in_darkmode" align=middle width=14.517775799999992pt height=14.15524440000002pt/> l'effectif de la classe <img src="/svgs/ef8601bbd2a50c3695ed7512680fa2ed.svg?invert_in_darkmode" align=middle width=182.18636039999998pt height=26.76175259999998pt/>.
- On peut ensuite définir <img src="/svgs/3bf9c1fe4273ed003fd49e744378a5ac.svg?invert_in_darkmode" align=middle width=17.85866609999999pt height=22.465723500000017pt/>, <img src="/svgs/9b6dbadab1b122f6d297345e9d3b8dd7.svg?invert_in_darkmode" align=middle width=12.69888674999999pt height=22.831056599999986pt/> et <img src="/svgs/e17c35f619f835117e1ff8e25d5f8a9c.svg?invert_in_darkmode" align=middle width=15.22169714999999pt height=22.465723500000017pt/> comme vu précédemment pour une série statistique dépouillée.

La série est alors donnée sous la forme de la famille <img src="/svgs/c671eed7dc1c7acd2128b25d42c3629d.svg?invert_in_darkmode" align=middle width=228.02332244999994pt height=24.65753399999998pt/>
On parle alors d'une série statistique **en classes** ou **regroupée en classes** ou encore,
parfois, **classée**.

- À toute série classée on peut faire correspondre une série statistique dépouillée <img src="/svgs/30b38cb240941f3ba9d4cf14e2e17939.svg?invert_in_darkmode" align=middle width=92.93066969999998pt height=24.7161288pt/> où <img src="/svgs/ddd6961256143776d6a303917925424e.svg?invert_in_darkmode" align=middle width=14.045887349999989pt height=24.7161288pt/> est le centre de la classe <img src="/svgs/2a6c039c1feb0541af7fafd78fcef15a.svg?invert_in_darkmode" align=middle width=150.9839826pt height=24.7161288pt/>.

### 1.2.7 Histogramme

Lorsque la statistique est découpée en classes, on ne la représente plus par un diagramme
en bâtons, mais par un histogramme. Chaque classe est représentée par un rectangle dont la
base est proportionnelle à la largeur de la classe et la **surface** proportionnelle à l'effectif (ou, ce qui revient au même, à la fréquence) de la classe. C'est bien la surface et non la hauteur du
rectangle qui est proportionnelle à l'effectif. Cette remarque prend toute son importance
lorsque les classes sont de largeurs différentes.

![Histogramme](Figure_1.png)

Exemple : on travaille sur une statistique découpées selon les quatre classes suivantes :
<img src="/svgs/d7ecfadde2c9f0430d56fc2f80d8a2b2.svg?invert_in_darkmode" align=middle width=186.30125579999998pt height=24.65753399999998pt/> et chaque classe est d'effectif <img src="/svgs/ecf4fe2774fd9244b4fd56f7e76dc882.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/>.  
L'axe des ordonnées peut être vu comme une densité.

### 1.2.8 La classe modale (paramètre de position)

C'est la classe correspondant au rectangle le plus haut dans l'histogramme (on parle bien
ici de hauteur et non de surface).Elle peut ne pas être unique. Il arrive qu'on définisse le mode
de la statistique comme le milieu de la classe modale (cette définition n'est pas entièrement
équivalente à celle donnée plus haut). Dans l'exemple précédent, la classe modale est la dernière
(classe <img src="/svgs/194d1fcf5f5a6b9d1cb7fe4d3cd6affc.svg?invert_in_darkmode" align=middle width=49.31516864999999pt height=24.65753399999998pt/>) et le mode est <img src="/svgs/f13e05ce3a39ac7aac70f5e2a459c98c.svg?invert_in_darkmode" align=middle width=29.22385289999999pt height=21.18721440000001pt/>.

## 1.3 Statistique double (bivariée)

### 1.3.1 Notations

On va se limiter à des statistiques quantitatives.

- <img src="/svgs/9432d83304c1eb0dcb05f092d30a767f.svg?invert_in_darkmode" align=middle width=11.87217899999999pt height=22.465723500000017pt/> population finie de <img src="/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.99998994999999pt height=22.465723500000017pt/> individus.
- Une statistique double <img src="/svgs/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode" align=middle width=12.92464304999999pt height=22.465723500000017pt/> est une application de <img src="/svgs/9432d83304c1eb0dcb05f092d30a767f.svg?invert_in_darkmode" align=middle width=11.87217899999999pt height=22.465723500000017pt/> dans <img src="/svgs/5160d9ee65d9c04247ae4a76b360933a.svg?invert_in_darkmode" align=middle width=6.5525476499999895pt height=26.76175259999998pt/>.

<p align="center"><img src="/svgs/e266f192365d3f5e780fe28ba1a694e5.svg?invert_in_darkmode" align=middle width=131.96777055pt height=39.452455349999994pt/></p>

<img src="/svgs/9774edfd40601dffbb4bedf81e5dfe23.svg?invert_in_darkmode" align=middle width=36.53197679999999pt height=24.65753399999998pt/> est de la forme <img src="/svgs/7392a8cd69b275fa1798ef94c839d2e0.svg?invert_in_darkmode" align=middle width=38.135511149999985pt height=24.65753399999998pt/>. On peut définir deux statistiques simples à partir de <img src="/svgs/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode" align=middle width=12.92464304999999pt height=22.465723500000017pt/>

#### **Première statistique marginale**

<p align="center"><img src="/svgs/7be0100f5c055bcc64f0407288a57e81.svg?invert_in_darkmode" align=middle width=343.67815019999995pt height=39.452455349999994pt/></p>

#### **Seconde statistique marginale**

<p align="center"><img src="/svgs/424928b410832e267e117a21c73e6887.svg?invert_in_darkmode" align=middle width=334.65990525pt height=39.452455349999994pt/></p>

Par **abus de langage**, on écrit que <img src="/svgs/6268401255cbff3d217f3bd65e3ffc1b.svg?invert_in_darkmode" align=middle width=82.12538564999998pt height=24.65753399999998pt/>.

Les ensembles des valeurs observables de <img src="/svgs/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode" align=middle width=14.908688849999992pt height=22.465723500000017pt/> et <img src="/svgs/91aac9730317276af725abd8cef04ca9.svg?invert_in_darkmode" align=middle width=13.19638649999999pt height=22.465723500000017pt/> sont finis. On peut écrire :
<p align="center"><img src="/svgs/3c23d9910d4dd5b32974ed60bcdaf103.svg?invert_in_darkmode" align=middle width=605.00688105pt height=17.031940199999998pt/></p>

avec <img src="/svgs/2ed2f03af9b82fe1a23429c1077b79d0.svg?invert_in_darkmode" align=middle width=161.26629089999997pt height=22.465723500000017pt/> et a priori <img src="/svgs/1859373ede9845374c1811d49cde9a1d.svg?invert_in_darkmode" align=middle width=38.11630349999999pt height=22.831056599999986pt/>

#### **Effectifs et fréquences**

- Effectif <img src="/svgs/f3d032992176fb571e0fff26d6de2c64.svg?invert_in_darkmode" align=middle width=166.80234449999998pt height=26.76175259999998pt/> : nombre d'individus admettant <img src="/svgs/7469daf7516909be38c3fd6291d2c581.svg?invert_in_darkmode" align=middle width=49.94493569999999pt height=24.65753399999998pt/> comme valeur du caractère <img src="/svgs/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode" align=middle width=12.92464304999999pt height=22.465723500000017pt/>
- Effectif <img src="/svgs/caeacb3bc6eeec772b9012cb2d4549a0.svg?invert_in_darkmode" align=middle width=127.60473659999998pt height=26.76175259999998pt/> : nombre d'individus admettant <img src="/svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode" align=middle width=14.045887349999989pt height=14.15524440000002pt/> comme première valeur du caractère <img src="/svgs/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode" align=middle width=12.92464304999999pt height=22.465723500000017pt/> ou nombre d'individus admettant <img src="/svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode" align=middle width=14.045887349999989pt height=14.15524440000002pt/> comme valeur du caractère <img src="/svgs/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode" align=middle width=14.908688849999992pt height=22.465723500000017pt/>  
    >Remarque : $n_{i\bull}=\sum_{1\leq j\leq q}n_{ij}$
- Effectif <img src="/svgs/7c488a6443bc67369a6c2e66f1345796.svg?invert_in_darkmode" align=middle width=126.01049999999998pt height=26.76175259999998pt/> : nombre d'individus admettant <img src="/svgs/2b442e3e088d1b744730822d18e7aa21.svg?invert_in_darkmode" align=middle width=12.710331149999991pt height=14.15524440000002pt/> comme seconde valeur du caractère <img src="/svgs/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode" align=middle width=12.92464304999999pt height=22.465723500000017pt/> ou nombre d'individus admettant <img src="/svgs/2b442e3e088d1b744730822d18e7aa21.svg?invert_in_darkmode" align=middle width=12.710331149999991pt height=14.15524440000002pt/> comme valeur du caractère <img src="/svgs/91aac9730317276af725abd8cef04ca9.svg?invert_in_darkmode" align=middle width=13.19638649999999pt height=22.465723500000017pt/>  
    >Remarque : $n_{\bull j}=\sum_{1\leq i\leq q}n_{ij}$

On définit également les effectifs cumulés <img src="/svgs/98e5c1dd2c14d0be9bfdb8e7c9fe318c.svg?invert_in_darkmode" align=middle width=17.85866609999999pt height=22.465723500000017pt/> et <img src="/svgs/af7654e30d32b8385d4ed085a9fde4e7.svg?invert_in_darkmode" align=middle width=19.312276499999992pt height=22.465723500000017pt/> ainsi que les fréquences <img src="/svgs/ba42201b72d1d6add54c1bb88d8eaeaf.svg?invert_in_darkmode" align=middle width=18.80339504999999pt height=22.831056599999986pt/>, <img src="/svgs/3031505543dae4267cb09b2144f59284.svg?invert_in_darkmode" align=middle width=12.69888674999999pt height=22.831056599999986pt/>, <img src="/svgs/f4ee880ad33b81928e2e99bd168a4af1.svg?invert_in_darkmode" align=middle width=14.152495499999992pt height=22.831056599999986pt/>, <img src="/svgs/7d7fc5210eb7077c976b108b93f42a12.svg?invert_in_darkmode" align=middle width=15.22169714999999pt height=22.465723500000017pt/>, et <img src="/svgs/5fb0e32c90ec8017fde1abdb949f5f25.svg?invert_in_darkmode" align=middle width=16.67530754999999pt height=22.465723500000017pt/> en divisant les effectifs correspondants par <img src="/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.99998994999999pt height=22.465723500000017pt/>. Ainsi, par exemple :
<p align="center"><img src="/svgs/684419682b7a49681408d15e11ea21fd.svg?invert_in_darkmode" align=middle width=64.95965685pt height=29.47417935pt/></p>

#### **Tableau de contingence**

| <img src="/svgs/9c864b453280f7ec9ba9d77c38997eb0.svg?invert_in_darkmode" align=middle width=36.32426159999999pt height=24.65753399999998pt/> |     <img src="/svgs/f7019b486d7fc8f840b0ce0bb0d41714.svg?invert_in_darkmode" align=middle width=14.61197759999999pt height=14.15524440000002pt/>     | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |     <img src="/svgs/fba353e8e83ce14fc4a80553757972f7.svg?invert_in_darkmode" align=middle width=14.16393989999999pt height=14.15524440000002pt/>     | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |     <img src="/svgs/617a5934f5b14109a76200cd306b4eb9.svg?invert_in_darkmode" align=middle width=14.497269599999992pt height=14.15524440000002pt/>     |   <img src="/svgs/734d29955e0a96cf7c5f2aed7eb642ad.svg?invert_in_darkmode" align=middle width=33.75775094999999pt height=22.831056599999986pt/>    |
| :-------------: | :-----------: | :------: | :-----------: | :------: | :-----------: | :----------: |
|      <img src="/svgs/277fbbae7d4bc65b6aa601ea481bebcc.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=14.15524440000002pt/>      |   <img src="/svgs/97e77257a20e92280b9a9735400f7a21.svg?invert_in_darkmode" align=middle width=22.97196989999999pt height=14.15524440000002pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/b7df48bfa55acd3b1559cf5415a8dba7.svg?invert_in_darkmode" align=middle width=22.52393219999999pt height=14.15524440000002pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/d5bbfaccbed056fe901c3650a522f9c0.svg?invert_in_darkmode" align=middle width=22.85726189999999pt height=14.15524440000002pt/>    | <img src="/svgs/edbbe21b29e169bff7d5daca6a1a1ce8.svg?invert_in_darkmode" align=middle width=16.41942389999999pt height=14.15524440000002pt/> |
|    <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>     |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    | <img src="/svgs/cdf98f18597b1c136efd19c96642f893.svg?invert_in_darkmode" align=middle width=17.35155014999999pt height=26.484018000000006pt/> |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    | <img src="/svgs/cdf98f18597b1c136efd19c96642f893.svg?invert_in_darkmode" align=middle width=17.35155014999999pt height=26.484018000000006pt/> |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>   |
|      <img src="/svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode" align=middle width=14.045887349999989pt height=14.15524440000002pt/>      |   <img src="/svgs/6594529f73eaa7eb7e372b96206898cf.svg?invert_in_darkmode" align=middle width=21.07032179999999pt height=14.15524440000002pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/894246f28d69aaede1ebed600795650c.svg?invert_in_darkmode" align=middle width=20.62228409999999pt height=14.15524440000002pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/b649b78123a41e24413853f05856f807.svg?invert_in_darkmode" align=middle width=20.95561379999999pt height=14.15524440000002pt/>    | <img src="/svgs/c3f9f1711fd17127e2368c78282aac87.svg?invert_in_darkmode" align=middle width=14.517775799999992pt height=14.15524440000002pt/> |
|    <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>     |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    | <img src="/svgs/cdf98f18597b1c136efd19c96642f893.svg?invert_in_darkmode" align=middle width=17.35155014999999pt height=26.484018000000006pt/> |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    | <img src="/svgs/cdf98f18597b1c136efd19c96642f893.svg?invert_in_darkmode" align=middle width=17.35155014999999pt height=26.484018000000006pt/> |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>   |
|      <img src="/svgs/0957a9bbf01d2ea5f621f1d068d404d9.svg?invert_in_darkmode" align=middle width=16.17146519999999pt height=14.15524440000002pt/>      |   <img src="/svgs/4758b0192cc1cecd71386c020d9566a7.svg?invert_in_darkmode" align=middle width=23.19590129999999pt height=14.15524440000002pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/6753432b877266f039151dd765848ac6.svg?invert_in_darkmode" align=middle width=22.747863599999988pt height=14.15524440000002pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/462b62927ae7eae5add3862a22cade43.svg?invert_in_darkmode" align=middle width=23.08119164999999pt height=14.15524440000002pt/>    | <img src="/svgs/3778addc66841b321d572411ae787043.svg?invert_in_darkmode" align=middle width=16.64335364999999pt height=14.15524440000002pt/> |
|     <img src="/svgs/734d29955e0a96cf7c5f2aed7eb642ad.svg?invert_in_darkmode" align=middle width=33.75775094999999pt height=22.831056599999986pt/>     | <img src="/svgs/b5091e05f468cc795f179b748a996cd2.svg?invert_in_darkmode" align=middle width=16.41942389999999pt height=14.15524440000002pt/> | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> | <img src="/svgs/b4432313b94fdf0060abed8466b8789e.svg?invert_in_darkmode" align=middle width=15.971386199999989pt height=14.15524440000002pt/> | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> | <img src="/svgs/858d9dfcc05145ec105262807940efa4.svg?invert_in_darkmode" align=middle width=16.304714249999993pt height=14.15524440000002pt/> |     <img src="/svgs/f9c4988898e7f532b9f826a75014ed3c.svg?invert_in_darkmode" align=middle width=14.99998994999999pt height=22.465723500000017pt/>      |

| <img src="/svgs/9c864b453280f7ec9ba9d77c38997eb0.svg?invert_in_darkmode" align=middle width=36.32426159999999pt height=24.65753399999998pt/> |     <img src="/svgs/f7019b486d7fc8f840b0ce0bb0d41714.svg?invert_in_darkmode" align=middle width=14.61197759999999pt height=14.15524440000002pt/>     | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |     <img src="/svgs/fba353e8e83ce14fc4a80553757972f7.svg?invert_in_darkmode" align=middle width=14.16393989999999pt height=14.15524440000002pt/>     | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |     <img src="/svgs/617a5934f5b14109a76200cd306b4eb9.svg?invert_in_darkmode" align=middle width=14.497269599999992pt height=14.15524440000002pt/>     |   <img src="/svgs/734d29955e0a96cf7c5f2aed7eb642ad.svg?invert_in_darkmode" align=middle width=33.75775094999999pt height=22.831056599999986pt/>    |
| :-------------: | :-----------: | :------: | :-----------: | :------: | :-----------: | :----------: |
|      <img src="/svgs/277fbbae7d4bc65b6aa601ea481bebcc.svg?invert_in_darkmode" align=middle width=15.94753544999999pt height=14.15524440000002pt/>      |   <img src="/svgs/298429dc6f0abd6cb73642bd86b18177.svg?invert_in_darkmode" align=middle width=21.153080849999988pt height=22.831056599999986pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/fc6fcda71a88c2f0aa1efee48bacfd5e.svg?invert_in_darkmode" align=middle width=20.70504314999999pt height=22.831056599999986pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/7067d781d9c3ff63c795f032a519ff95.svg?invert_in_darkmode" align=middle width=21.038371199999993pt height=22.831056599999986pt/>    | <img src="/svgs/31bf297270723f6ace1cd58754a6c4a1.svg?invert_in_darkmode" align=middle width=14.60053319999999pt height=22.831056599999986pt/> |
|    <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>     |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    | <img src="/svgs/cdf98f18597b1c136efd19c96642f893.svg?invert_in_darkmode" align=middle width=17.35155014999999pt height=26.484018000000006pt/> |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    | <img src="/svgs/cdf98f18597b1c136efd19c96642f893.svg?invert_in_darkmode" align=middle width=17.35155014999999pt height=26.484018000000006pt/> |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>   |
|      <img src="/svgs/9fc20fb1d3825674c6a279cb0d5ca636.svg?invert_in_darkmode" align=middle width=14.045887349999989pt height=14.15524440000002pt/>      |   <img src="/svgs/dc19633fa39ed0205e2e82955064a493.svg?invert_in_darkmode" align=middle width=19.25143274999999pt height=22.831056599999986pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/ba42201b72d1d6add54c1bb88d8eaeaf.svg?invert_in_darkmode" align=middle width=18.80339504999999pt height=22.831056599999986pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/3129a07c994b80cf1c31361358ea640b.svg?invert_in_darkmode" align=middle width=19.13672474999999pt height=22.831056599999986pt/>    | <img src="/svgs/3031505543dae4267cb09b2144f59284.svg?invert_in_darkmode" align=middle width=12.69888674999999pt height=22.831056599999986pt/> |
|    <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>     |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    | <img src="/svgs/cdf98f18597b1c136efd19c96642f893.svg?invert_in_darkmode" align=middle width=17.35155014999999pt height=26.484018000000006pt/> |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    | <img src="/svgs/cdf98f18597b1c136efd19c96642f893.svg?invert_in_darkmode" align=middle width=17.35155014999999pt height=26.484018000000006pt/> |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>    |   <img src="/svgs/5f73ac7f4b10f3b9bf369b4b37f93371.svg?invert_in_darkmode" align=middle width=4.5662248499999905pt height=29.771689199999994pt/>   |
|      <img src="/svgs/0957a9bbf01d2ea5f621f1d068d404d9.svg?invert_in_darkmode" align=middle width=16.17146519999999pt height=14.15524440000002pt/>      |   <img src="/svgs/7f4b1d9dcee9160e777e3c1ed3d79a85.svg?invert_in_darkmode" align=middle width=21.377012249999993pt height=22.831056599999986pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/01b422811c0b7964a521bf9cbbec5285.svg?invert_in_darkmode" align=middle width=20.928974549999985pt height=22.831056599999986pt/>    | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> |   <img src="/svgs/ef96892953f30f5d59d07f50af9b59a9.svg?invert_in_darkmode" align=middle width=21.26230259999999pt height=22.831056599999986pt/>    | <img src="/svgs/e544fa6d8d609efad5a1e4bf79f21cee.svg?invert_in_darkmode" align=middle width=14.824464599999992pt height=22.831056599999986pt/> |
|     <img src="/svgs/734d29955e0a96cf7c5f2aed7eb642ad.svg?invert_in_darkmode" align=middle width=33.75775094999999pt height=22.831056599999986pt/>     | <img src="/svgs/58205a6a9a9bdea4cd4e5700a9469ae9.svg?invert_in_darkmode" align=middle width=14.60053319999999pt height=22.831056599999986pt/> | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> | <img src="/svgs/f4ee880ad33b81928e2e99bd168a4af1.svg?invert_in_darkmode" align=middle width=14.152495499999992pt height=22.831056599999986pt/> | <img src="/svgs/e378afcd7cae11e7306c61a9c35bf6cf.svg?invert_in_darkmode" align=middle width=19.17798959999999pt height=14.15524440000002pt/> | <img src="/svgs/b1ed82cb42e65ae6c64adce6e7afe9d5.svg?invert_in_darkmode" align=middle width=14.48582519999999pt height=22.831056599999986pt/> |     <img src="/svgs/034d0a6be0424bffe9a6e7ac9236c0f5.svg?invert_in_darkmode" align=middle width=8.219209349999991pt height=21.18721440000001pt/>      |

### 1.3.2 Covariance et coeffcient de corrélation

#### **Covariance**

Elle donne une mesure du lien existant entre les deux caractères <img src="/svgs/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode" align=middle width=14.908688849999992pt height=22.465723500000017pt/> et <img src="/svgs/91aac9730317276af725abd8cef04ca9.svg?invert_in_darkmode" align=middle width=13.19638649999999pt height=22.465723500000017pt/>.
<p align="center"><img src="/svgs/c16a1c1a488aa7aa7d71ff6263458c6f.svg?invert_in_darkmode" align=middle width=571.72480035pt height=59.1786591pt/></p>
Si les deux caractères sont indépendants l'un de l'autre alors la covariance est nulle.  
Réciproque fausse.

#### **Coeffcient de corrélation**

C'est une normalisation de la covariance qui évite les effets d'échelle.
<p align="center"><img src="/svgs/92f4da5f91db661f29ca9dde3b910d96.svg?invert_in_darkmode" align=middle width=98.10701999999999pt height=31.939908pt/></p>

- <img src="/svgs/f6f07dd8270323611ac2358b87cc9bb3.svg?invert_in_darkmode" align=middle width=91.82747475pt height=21.18721440000001pt/>
- Si <img src="/svgs/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode" align=middle width=14.908688849999992pt height=22.465723500000017pt/> et <img src="/svgs/91aac9730317276af725abd8cef04ca9.svg?invert_in_darkmode" align=middle width=13.19638649999999pt height=22.465723500000017pt/> sont indépendants alors <img src="/svgs/bb01f7f6ea5094f2d355ae740b8880fa.svg?invert_in_darkmode" align=middle width=61.69063394999999pt height=21.18721440000001pt/>.Réciproque fausse.
- S'il existe une relation affine entre <img src="/svgs/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode" align=middle width=14.908688849999992pt height=22.465723500000017pt/> et <img src="/svgs/91aac9730317276af725abd8cef04ca9.svg?invert_in_darkmode" align=middle width=13.19638649999999pt height=22.465723500000017pt/> alors <img src="/svgs/358e6603b579c4b1a89908e68d1e0bc8.svg?invert_in_darkmode" align=middle width=61.69063394999999pt height=21.18721440000001pt/>. Réciproque fausse.

### 1.3.3 Droite de régression linéaire

#### **Droite de régression de Y en X**

On cherche la droite d'équation <img src="/svgs/51a0509459c4d95a639122aa4b6774e3.svg?invert_in_darkmode" align=middle width=85.85781929999999pt height=22.831056599999986pt/> approchant "au mieux" le nuage de points de la
statistique double <img src="/svgs/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode" align=middle width=12.92464304999999pt height=22.465723500000017pt/>.
<p align="center"><img src="/svgs/c3372c31cd57e8db014ab3eaad9d27f5.svg?invert_in_darkmode" align=middle width=131.3234241pt height=49.315569599999996pt/></p>

Cette droite passe par le point <img src="/svgs/7392a8cd69b275fa1798ef94c839d2e0.svg?invert_in_darkmode" align=middle width=38.135511149999985pt height=24.65753399999998pt/>

#### **Droite de régression de X en Y**

On cherche la droite d'équation <img src="/svgs/e53d9f8a4cd06980465cfa72a687192a.svg?invert_in_darkmode" align=middle width=92.56820429999999pt height=22.831056599999986pt/> approchant "au mieux" le nuage de points de la
statistique double <img src="/svgs/9b325b9e31e85137d1de765f43c0f8bc.svg?invert_in_darkmode" align=middle width=12.92464304999999pt height=22.465723500000017pt/>.
<p align="center"><img src="/svgs/072bf774c0d1cdd95febcebd723dcb3c.svg?invert_in_darkmode" align=middle width=131.3234241pt height=49.315569599999996pt/></p>

Cette droite passe par le point <img src="/svgs/7392a8cd69b275fa1798ef94c839d2e0.svg?invert_in_darkmode" align=middle width=38.135511149999985pt height=24.65753399999998pt/>

Les deux droites sont confondues ssi <img src="/svgs/6b09415218ae4b874cd495db9dcd6ef7.svg?invert_in_darkmode" align=middle width=225.72632939999997pt height=37.28212289999999pt/>

### 1.3.4 Régression logarithmique

Lorsque le nuage de points ne semble pas rectiligne, on peut chercher d'autres types de
relation entre <img src="/svgs/cbfb1b2a33b28eab8a3e59464768e810.svg?invert_in_darkmode" align=middle width=14.908688849999992pt height=22.465723500000017pt/> et <img src="/svgs/91aac9730317276af725abd8cef04ca9.svg?invert_in_darkmode" align=middle width=13.19638649999999pt height=22.465723500000017pt/>, tout en s'appuyant sur la technique de la régression linéaire.

#### **Si on soupçonne une relation de la forme** <img src="/svgs/5804dd8e9183876fb6b31b41adf1d87b.svg?invert_in_darkmode" align=middle width=68.73412259999998pt height=22.831056599999986pt/>

En passant au logarithme, la relation devient : <img src="/svgs/47b6ce0d480af236efc89a0538552e7f.svg?invert_in_darkmode" align=middle width=186.36984464999998pt height=24.65753399999998pt/>  
On calcule alors la droite de régression sur le couple <img src="/svgs/a68f94175d6793b5f95ca4f4b7a10e48.svg?invert_in_darkmode" align=middle width=183.29541614999997pt height=24.7161288pt/>  
Si le résultat est <img src="/svgs/a2840158de0546e5f9b0fbc5969f87d7.svg?invert_in_darkmode" align=middle width=116.83180904999998pt height=24.7161288pt/> et que le coeffcient de corrélation est satisfaisant, alors on admet que <img src="/svgs/5fb3b5019ae08de202f11dcfbc44b62a.svg?invert_in_darkmode" align=middle width=90.7492212pt height=27.6567522pt/> (i.e. <img src="/svgs/24a3d3713c91550a9b63eca80d66199b.svg?invert_in_darkmode" align=middle width=50.22994184999998pt height=27.6567522pt/> et <img src="/svgs/036fb5404566f06cec86866cbb83072f.svg?invert_in_darkmode" align=middle width=44.82292649999999pt height=22.465723500000017pt/>)

#### **Si on soupçonne une relation de la forme** <img src="/svgs/a06bdd44ee5fa42ac8e1ee5111645fce.svg?invert_in_darkmode" align=middle width=67.5307677pt height=27.6567522pt/>

En passant au logarithme, la relation devient : <img src="/svgs/df7cf4ab36018e257f379aad1d91ade1.svg?invert_in_darkmode" align=middle width=186.36986609999997pt height=24.65753399999998pt/>  
On calcule alors la droite de régression sur le couple <img src="/svgs/290218763eebd8647eca7399e8d0c81e.svg?invert_in_darkmode" align=middle width=154.50151695pt height=24.7161288pt/>  
Si le résultat est <img src="/svgs/a2840158de0546e5f9b0fbc5969f87d7.svg?invert_in_darkmode" align=middle width=116.83180904999998pt height=24.7161288pt/> et que le coeffcient de corrélation est satisfaisant, alors on admet que <img src="/svgs/9737589b2bf259739f50ab232a647288.svg?invert_in_darkmode" align=middle width=108.77674829999998pt height=27.6567522pt/> (i.e. <img src="/svgs/24a3d3713c91550a9b63eca80d66199b.svg?invert_in_darkmode" align=middle width=50.22994184999998pt height=27.6567522pt/> et <img src="/svgs/f8ffbd6ee29f79dec1a8c14aa246779b.svg?invert_in_darkmode" align=middle width=50.03417759999999pt height=27.6567522pt/>)

### 1.3.5 Régression polynomiale

<img src="/svgs/499d713b1bdd782fcc26e1f729f76784.svg?invert_in_darkmode" align=middle width=138.02296859999998pt height=24.65753399999998pt/> et <img src="/svgs/00bdf147ec56189e3a015e956c2d82de.svg?invert_in_darkmode" align=middle width=132.30401084999997pt height=24.65753399999998pt/>
On cherche une relation de la forme <img src="/svgs/1ef1ad606996be9411dfe1a3006c7f34.svg?invert_in_darkmode" align=middle width=75.93984914999999pt height=24.65753399999998pt/> où <img src="/svgs/334fc086a9d9ef9b982a7f0e805cd4f1.svg?invert_in_darkmode" align=middle width=135.19610444999998pt height=27.91243950000002pt/>  
On pose <img src="/svgs/e87878f38da57717dcdda1e5d6cc9527.svg?invert_in_darkmode" align=middle width=98.95453424999998pt height=27.91243950000002pt/> (<img src="/svgs/1287d7faee93a4a79f654193e4b114b2.svg?invert_in_darkmode" align=middle width=89.30553554999999pt height=24.65753399999998pt/>) et <img src="/svgs/2aab122732e525d02020bda11a98f633.svg?invert_in_darkmode" align=middle width=112.01302365pt height=27.91243950000002pt/>  
Soit <img src="/svgs/fb97d38bcc19230b0acd442e17db879c.svg?invert_in_darkmode" align=middle width=17.73973739999999pt height=22.465723500000017pt/> la matrice carrée d'ordre <img src="/svgs/3f18d8f60c110e865571bba5ba67dcc6.svg?invert_in_darkmode" align=middle width=38.17727759999999pt height=21.18721440000001pt/> définie par : <img src="/svgs/3476fd75482303d90ebb5e32fdbf0eca.svg?invert_in_darkmode" align=middle width=100.43652299999998pt height=24.65753399999998pt/>  
Soit <img src="/svgs/61e84f854bc6258d4108d08d4c4a0852.svg?invert_in_darkmode" align=middle width=13.29340979999999pt height=22.465723500000017pt/> le vecteur <img src="/svgs/c51bb92f3e0c036c3d9ef6e51c8290e0.svg?invert_in_darkmode" align=middle width=107.61795329999998pt height=26.085962100000025pt/> et <img src="/svgs/53d147e7f3fe6e47ee05b88b166bd3f6.svg?invert_in_darkmode" align=middle width=12.32879834999999pt height=22.465723500000017pt/> le vecteur d'inconnues <img src="/svgs/d03e9345410d130c5a36c5c19a136bbc.svg?invert_in_darkmode" align=middle width=104.86685714999997pt height=26.085962100000025pt/>

<img src="/svgs/53d147e7f3fe6e47ee05b88b166bd3f6.svg?invert_in_darkmode" align=middle width=12.32879834999999pt height=22.465723500000017pt/> est solution du système <img src="/svgs/38ee00afe7e8263a8ab93edf74549df8.svg?invert_in_darkmode" align=middle width=77.15153654999999pt height=22.465723500000017pt/>
