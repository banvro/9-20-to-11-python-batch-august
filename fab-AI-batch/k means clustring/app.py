# from sklearn.datasets import make_blobs
# import matplotlib.pyplot as plt
# from new_algo import KMeans

# centriod = [(-5, -5), (5, 5), (10, -8)]

# centriod_sdd = (1,1, 1)

# x, y = make_blobs(n_samples = 500, centers = centriod, cluster_std = centriod_sdd, n_features = 2)

# # print(x)
# # plt.scatter(x[:, 0], x[:, 1])
# # plt.show()
# # KMeans
# mymodel = KMeans(n_cluster = 3, max_iter = 1000)

# y_pred = mymodel.fit_predict(x)


# # print(y_pred)

# plt.scatter(x[y_pred == 0, 0], x[y_pred == 0, 1], color = "red")
# plt.scatter(x[y_pred == 1, 0], x[y_pred == 1, 1], color = "blue")
# plt.scatter(x[y_pred == 2, 0], x[y_pred == 2, 1], color = "green")

# plt.show()


from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from new_algo import KMeans
import pandas as pd

#centroids = [(-5,-5),(5,5),(-2.5,2.5),(2.5,-2.5)]
#cluster_std = [1,1,1,1]

#X,y = make_blobs(n_samples=100,cluster_std=cluster_std,centers=centroids,n_features=2,random_state=2)

#plt.scatter(X[:,0],X[:,1])

df = pd.read_csv('student_clustering.csv')

X = df.iloc[:,:].values

km = KMeans(n_clusters=4,max_iter=500)
y_means = km.fit_predict(X)

plt.scatter(X[y_means == 0,0],X[y_means == 0,1],color='red')
plt.scatter(X[y_means == 1,0],X[y_means == 1,1],color='blue')
plt.scatter(X[y_means == 2,0],X[y_means == 2,1],color='green')
plt.scatter(X[y_means == 3,0],X[y_means == 3,1],color='yellow')
plt.show()