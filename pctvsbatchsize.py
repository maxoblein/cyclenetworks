#pct_iqr vs ratio batchsize to Ne

from upgrade import *
from analysis import *
from distributions import *
from scipy.stats import iqr

E = 2000
B = 20
Nt =100
print(B)
W = [1,2,5,10]
wd = 2

# for w in W:
#     upgrade_network(E,Nt,B,w=w)

data = []
for w in W:
    filename = 'Graphmls/Graphpostupgrade' + '_' + str(E)+ '_' + str(Nt) + '_' + str(B) + '_' + str(wd)
    data.append(get_pcts(filename,500,w))

fig, ax = plt.subplots()



ax.boxplot(data)

ind = np.arange(len(W)+1)
ax.set_xticks(ind)
labels = [' ']
for label in W:
    labels.append(str(label))
ax.set_xticklabels(labels)

plt.savefig('lpic_figs/cmp_var_wt.pdf')
