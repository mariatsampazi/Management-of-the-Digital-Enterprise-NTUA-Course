import scipy
import numpy as np
import math
from scipy import stats
from scipy.stats import pearsonr

x=[8,1,5,3,7]
y=[9,7,9,5,10]


corr=stats.pearsonr(x, y)[0] # calculate Pearson's correlation
sim=(corr+1)/2 #Calculate Similarity
print(round(sim,4)) #print similarity
