#pct cycle vs the omega design

from edgeflows import *
from analysis import *
from distributions import *
from scipy.stats import iqr

E = 2000
B = 20
Nt =100
W = [1,2,5,10,15,20,25,30]
print(B)

# for w in W:
#     upgrade_network(E,Nt,B,w)

data = []
for w in W:
    filename = 'Graphmls/Graphpostupgrade' + '_' + str(E)+ '_' + str(Nt) + '_' + str(B) + '_' + str(w)
    data.append(get_pcts(filename,500))

iqrs = []
for d in data:
    iqrs.append(iqr(d))

fig = plt.figure()
ax = fig.add_subplot()
ax.scatter(W,iqrs)
plt.show()
