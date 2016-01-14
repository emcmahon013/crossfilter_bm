import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd

fs = np.array([15*60,30*60,5*60,15*60,15*60])
fs = np.cumsum(fs)
f = np.array([5,10,30,20,7])
interval = len(fs)

total = []
for t in range(interval):
	if t == 0:
		x = np.arange(0,fs[t],5)
	else:
		x = np.arange(fs[t-1],fs[t],5)
	y = [np.sin(2*np.pi*f[t]*(i/fs[t])) for i in x]
	total.extend(y)

x = np.arange(0,fs[-1],5)
rest = []
final = []
for t in total:
	if t < -.5:
		rest.append(0)
	else:
		rest.append(1)
	noise = t + np.random.normal(0,.1)
	final.append(noise)

plt.plot(x,final)
plt.show()

data = pd.DataFrame({'data':final,'rest':rest})
data.to_csv('fake_data.csv',sep=',')
