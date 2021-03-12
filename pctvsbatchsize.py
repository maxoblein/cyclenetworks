#pct_iqr vs ratio batchsize to Ne

from upgrade import *
from analysis import *
from distributions import *
from scipy.stats import iqr

E = 2000
B = np.arange(5,25,5)
Nt =100
print(B)
w = 2

# for b in B:
#     upgrade_network(E,Nt,b,w=w)

data = []
for b in B:
    filename = 'Graphmls/Graphpostupgrade' + '_' + str(E)+ '_' + str(Nt) + '_' + str(b) + '_' + str(w)
    data.append(get_pcts(filename,500))

fig, ax = plt.subplots()



ax.boxplot(data)

ind = np.arange(len(B)+1)
ax.set_xticks(ind)
labels = [' ']
for label in B:
    labels.append(str(label))
ax.set_xticklabels(labels)

plt.savefig('lpic_figs/cmp_var_b.pdf')
