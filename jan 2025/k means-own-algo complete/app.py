from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt 
from kmeanss import myKmeans

x, y = make_blobs(n_samples = 200, n_features = 2, centers = [(-5, -5), (5, 5), (-4, 8)], cluster_std = [2, 2, 2], random_state = 2)

# print(x)
 
obj = myKmeans(n_cluster = 3)
ct, cluster = obj.fit(x)

print(ct)

print(cluster)


c1 = x[cluster == 0]

c1x = c1[:, 0 : 1]
c1y = c1[:, -1]

c2 = x[cluster == 1]

c2x = c2[:, 0 : 1]
c2y = c2[:, -1]

# x[cluster == 0]


# x1 = x[:, 0:1]
# x2 = x[:, -1]

# # print(x[cluster == 0], "euuuuuuu")
# [[c1, c1], [c2, c2], [c3, c2]]

# # plt.scatter(x1, x2)

totl_sentriods = len(ct)

for i in range(totl_sentriods):
    plt.scatter(ct[i][0], ct[i][1], s = 300)
# plt.scatter(ct[1][0], ct[1][1], s = 300)

plt.scatter(c1x, c1y, label = "first cluster")
plt.scatter(c2x, c2y, label = "second cluster")

plt.show()