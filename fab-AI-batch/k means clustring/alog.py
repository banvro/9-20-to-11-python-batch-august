import random
import numpy as np

class MyKMeanssAlgo:
    def __init__(self, n_cluster = 2, max_iter = 100):
        self.n_cluster = n_cluster
        self.max_iter = max_iter    
        self.centriod = None
    
    def fit_predict(self, x):
        # 1) decide n cluster
        # 2) init centriod 
        # print(x)
        for _ in range(self.max_iter):
            centriod_index = random.sample(range(0, x.shape[0]), self.n_cluster)

            self.centriod = x[centriod_index]
            
            # 3) assign cluster 
            cluster_group = self.calculate_distance(x)

            # 4) move centriod 

            old_centriod = self.centriod

            self.centriod = self.move_centriod(x, cluster_group)

            print("goooooo")
            print(type(self.centriod))
            print(type(old_centriod))
            # 5) finish
            # if (old_centriod == self.centriod).all():
            if np.allclose(old_centriod, self.centriod):
                print("heyyyyyy")
                break
        
        return cluster_group

        # print(cluster_group)
    
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

        return np.array(cluster_group)


    def move_centriod(self, x, cluster_group):
        new_centriod = []
        my_clusters = np.unique(cluster_group)

        for cluster in my_clusters:
            new_centriod.append(x[cluster_group == cluster].mean(axis = 0))

        return np.array(new_centriod)