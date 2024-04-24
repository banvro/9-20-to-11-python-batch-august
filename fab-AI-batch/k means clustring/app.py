from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from alog import MyKMeanssAlgo

centriod = [(-5, -5), (5, 5)]

centriod_sdd = (1,1)

x, y = make_blobs(n_samples = 500, centers = centriod, cluster_std = centriod_sdd, n_features = 2)

# print(x)
# plt.scatter(x[:, 0], x[:, 1])
# plt.show()

mymodel = MyKMeanssAlgo(n_cluster = 2, max_iter = 1000)

y_pred = mymodel.fit_predict(x)


# print(y_pred)

plt.scatter(x[y_pred == 0, 0], x[y_pred == 0, 1], color = "red")
plt.scatter(x[y_pred == 1, 0], x[y_pred == 1, 1], color = "blue")
# plt.scatter(x[y_pred == 2, 0], x[y_pred == 2, 1], color = "green")

plt.show()