import random
import numpy as np

class MyKMeanssAlgo:
    def __init__(self, n_cluster = 2, max_iter = 100):
        self.n_cluster = n_cluster
        self.max_iter = max_iter    
        self.centriod = None
    
    def fit_predict(self, x):
        # print(x.shape[0])
        # random(range, number of values)
        # print(random.sample(range(0, x.shape[0]), self.n_cluster))
        centriod_index = random.sample(range(0, x.shape[0]), self.n_cluster)

        self.centriod = x[centriod_index]
        # print(self.centriod)

        cluster_group = self.calculate_distance(x)

        print(cluster_group)
    
    def calculate_distance(self, x):
        distance = []
        cluster_group = []

        for rows in x:
            for i in self.centriod:
                distance.append(np.sqrt(np.dot(rows - i, rows - i)))
            # print(distance)
            # print(min(distance))
            # print(distance.index(min(distance)))
            cluster_group.append(distance.index(min(distance)))
            distance.clear()

        return cluster_group
