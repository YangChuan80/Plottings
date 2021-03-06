import scipy.stats
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

age=[45,35,37,44,47,49,47,47,42,41,40,43,43,39,37,42,48,36,39,35]
hr=[164,185,186,167,142,150,147,153,167,170,165,158,166,173,186,165,139,179,182,192]

combo={'age':age,'hr':hr}
df=pd.DataFrame(combo)

#Regression & Correlation
regress_results=scipy.stats.linregress(age,hr)
corr_results=df.hr.corr(df.age)

print('Regression results are: ',regress_results,'\n')
print('Correlation results are: ',corr_results)

#Plot
x=range(min(age)-10,max(age)+10)
y=regress_results[0]*x+regress_results[1]

plt.scatter(age,hr)
plt.plot(x,y,color='r')
plt.show()
