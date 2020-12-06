from analysis import *


network = init_graph('Graphdam')

adjusted_network = adjust_weights(network[0],25)

print(len(list(adjusted_network.edges)))
d =[]
l = []
for i in range(700):

    path, ecpath, pct_cycle, length = random_shortest_path(adjusted_network)

    if len(path) > 50:
        d.append(pct_cycle)
        l.append(len(path))
        print(len(path))

print('mean = ',np.mean(l))

fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.hist(d,bins=25)


plt.savefig('lpic_figs/uni_hist_dam_o25.pdf')
'''
fig2 = plt.figure()
ax2 = fig2.add_subplot(111)

ax2.hist(l,bins=25)
ax2.set_title('Number of edges in shortest paths between OD pairs',fontsize=18)
ax2.set_xlabel('Length',fontsize=16)
ax2.set_ylabel('Frequency',fontsize=16)
plt.show()
'''
