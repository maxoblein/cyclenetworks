#plotting variation from batch to batch#
from upgrade import *

from upgrade import *
from analysis import *
from distributions import *
from scipy.stats import iqr

E = 2000
Batchnum = range(20)
Nt =100
print(Batchnum)
w = 2



data = []
for b in Batchnum:
    filename = 'Graphmls/batches_2000_w2/batch_' + str(b)
    data.append(get_pcts(filename,500))

fig, ax = plt.subplots()



ax.boxplot(data)

ind = np.arange(len(Batchnum)+1)
ax.set_xticks(ind)
labels = [' ']
for label in Batchnum:
    labels.append(str(label+1))
ax.set_xticklabels(labels)

plt.savefig('lpic_figs/cmp_batchbybatch.pdf')
