from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt 
from kmeanss import myKmeans

x, y = make_blobs(n_samples = 200, n_features = 2, centers = [(-5, -5), (5, 5)], cluster_std = [2, 2], random_state = 2)

print(x)

obj = myKmeans()
ct, cluster = obj.fit(x)

print(ct)

# x[cluster == 0]


x1 = x[:, 0:1]
x2 = x[:, -1]

print(x[cluster == 0], "euuuuuuu")

# plt.scatter(x1, x2)
plt.scatter(ct[0][0], ct[0][1], s = 300)
plt.scatter(ct[1][0], ct[1][1], s = 300)

# plt.scatter(x[cluster == 0][0], x[cluster == 0][1], label = "first cluster")
# plt.scatter(x[cluster == 1][0], x[cluster == 1][1], label = "second cluster")

plt.show()