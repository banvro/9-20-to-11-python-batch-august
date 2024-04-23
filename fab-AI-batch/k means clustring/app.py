from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from alog import MyKMeanssAlgo

centriod = [(-5, -5), (5, 5)]

centriod_sdd = (1,1)

x, y = make_blobs(n_samples = 100, centers = centriod, cluster_std = centriod_sdd, n_features = 2)

# print(x)
# plt.scatter(x[:, 0], x[:, 1])
# plt.show()

mymodel = MyKMeanssAlgo(n_cluster = 2, max_iter = 100)

mymodel.fit_predict(x)