from projetstatspeip import Stat,StatDouble
import numpy as np
import scipy.stats as st
import statistics
from math import pi, sqrt, exp

ex=Stat([2,3,4,4,6,6,8,9,10,10,11,11,12,12,12,12])
excl=ex.classer([2,4,9,11,12])
excl.histogramme()
exd=StatDouble([5,3,6,7,2,6,7,8,1,2,9,7,3,6,0,4],[2,3,4,4,6,6,8,9,10,10,11,11,12,12,12,12])
exd.contingence()