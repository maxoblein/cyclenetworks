#pct_iqr vs ratio batchsize to Ne

from upgrade import *
from analysis import *
from distributions import *
from scipy.stats import iqr

E = 1000
B = np.arange(2,22,2)
Nt =100
print(B)
w = 5

for b in B:
    upgrade_network(E,Nt,b,w=w)

data = []
for b in B:
    filename = 'Graphmls/Graphpostupgrade' + '_' + str(E)+ '_' + str(Nt) + '_' + str(b) + '_' +str(w)
    data.append(get_pcts(filename,500))

iqrs = []
for d in data:
    iqrs.append(iqr(d))

fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(B,iqrs)
plt.show()
