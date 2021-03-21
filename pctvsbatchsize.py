#pct_iqr vs ratio batchsize to Ne

from upgrade import *
from analysis import *
from distributions import *
from scipy.stats import iqr

L = 160000
B = [1,2,3,4,5,7,8,9,10,13,15,18,20]
Nt =100
print(B)
w = 2
wd = 2

# for b in B:
#      upgrade_network(L,Nt,b,w=w,save = True)

data = []
for b in B:
    filename = 'Graphmls/Graphpostupgrade' + '_' + str(L)+ '_' + str(Nt) + '_' + str(b) + '_' + str(wd)
    G = ox.io.load_graphml(filename)

    data.append(find_total_cycle_length(G))

fig, ax = plt.subplots()



ax.scatter(B,data)

ind = np.arange(21)
ax.set_xticks(ind)
labels = np.arange(21)
# for label in B:
#     labels.append(str(label))
ax.set_xticklabels(labels)

plt.savefig('lpic_figs/scatter_totallen_nbatches.pdf')
