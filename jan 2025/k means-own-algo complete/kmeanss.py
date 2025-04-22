import random
import numpy as np
class myKmeans:

    def __init__(self, n_cluster = 2, max_itr = 200):
        self.n_cluster = n_cluster
        self.max_itr = max_itr
        self.centriods = None

    def fit(self, mydata):
        
        ran_indx = random.sample(range(0, mydata.shape[0]), self.n_cluster)

        # print(ran_indx)

        self.centriods = mydata[ran_indx]

        for i in range(self.max_itr):
            clusters = self.assign_cluster(mydata)

            moving_centridos = self.move_centriods(clusters, mydata)

            if (self.centriods == moving_centridos).all():
                break

        # print(self.centriods)

        return self.centriods, clusters
    

    def assign_cluster(self, mydata):

        clusters = []
        distances = []

        for row in mydata:
            # print("----------------")
            for centriods in self.centriods:
                distance = np.sqrt(np.dot(row-centriods, row-centriods))
                distances.append(distance)

            min_di = np.min(distances)

            clusters.append(distances.index(min_di))

            # print(distances)
            # print("eeeeeeeeeeeeeeeeeee")
            distances = []

            # print(clusters)

        return np.array(clusters)


    def move_centriods(self, clusters, mydata):
        
        new_centriods = []

        clss = np.unique(clusters)

        for x in clss:
            meann = mydata[clusters == x].mean(axis = 0)
            # print(meann, "xxxxxxxxxxxxxxxxx")
            new_centriods.append(meann)
        
        return np.array(new_centriods)
