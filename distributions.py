from analysis import *

network = init_graph('Graphall')

adjusted_network = adjust_weights(network[0])

d =[]
for i in range(500):

    path, ecpath, pct_cycle = random_shortest_path(adjusted_network)
    d.append(pct_cycle)
    print(pct_cycle)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.hist(d,bins=25)
ax.set_title('Percentage of edges in cycle network',fontsize=18)
ax.set_xlabel('Percentage',fontsize=16)
ax.set_ylabel('Frequency',fontsize=16)
plt.show()
