#temp
from analysis import *


network_pre = ox.io.load_graphml('Graphmls\Graphall')
network_post = ox.io.load_graphml('Graphmls\Graphpostupgrade_160000_100_20_2')
network_rand = ox.io.load_graphml('Graphmls\Graphpostupgrade_random')
ids, centroids, normed_matrix = initialiselsoa()
G_adj_pre,cycmat = adjust_weights(network_pre,2)
G_adj_post, cycmat = adjust_weights(network_post,2)
G_adj_rand, cycmat = adjust_weights(network_rand,2)



d_pre = []
d_post = []
d_rand = []
for i in range(500):
    print(i)
    path_pre, ecpath_pre, pct_cycle_pre, length_pre = random_shortest_path(G_adj_pre,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_pre)
    path_post, ecpath_post, pct_cycle_post, length_post = random_shortest_path(G_adj_post,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_post)
    path_rand, ecpath_rand, pct_cycle_rand, length_rand = random_shortest_path(G_adj_rand,ODoption = 'lsoa', ids=ids, centroids=centroids, normed_matrix=normed_matrix,G_true = network_rand)

    if len(path_pre) > 50:
        d_pre.append(pct_cycle_pre)

    if len(path_post) > 50:
        d_post.append(pct_cycle_post)

    if len(path_rand) > 50:
        d_rand.append(pct_cycle_rand)


data = [d_pre, d_rand, d_post]
fig, ax = plt.subplots()



ax.boxplot(data)

ind = np.arange(4)
ax.set_xticks(ind)
labels = [' ','pre-upgrade', 'random','heuristic']
ax.set_xticklabels(labels)

print('mean pre = ',np.mean(data[0]))
print('mean post = ',np.mean(data[1]))
plt.show()
