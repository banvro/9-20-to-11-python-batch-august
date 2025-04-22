# import numpy as np
# import matplotlib.pyplot as plt

# zx = np.array([12, 34])

# pq = np.array([10, 20])

# di = np.sqrt(np.dot(zx-pq, zx-pq))
# print(di)

# plt.scatter(zx, pq)

# plt.show()


# import numpy as np 

# # zx = np.array([12, 3])

# # print(np.min(zx))
# import pandas as pd

# zx = np.array([0, 1, 0, 1, 1, 1, 0, 0])

# data = np.random.randint(10, 30, size = (8, 2))
# print(data, "eeeeeeeee")
# print(data[zx == 0])

# # data = np.array([[28 21], [14 18], [19 28], [19 15], [28 21], [14 18], [19 28], [19 15], [27 25], [11 21]])

# # df = pd.DataFrame({
# #     "x1" : data[:, 0 : 1],
# #     "x2" : data[:, -1]
# # })

# # print(df.loc[zx == 0])



import numpy as np 


zx = np.array([1, 2, 1, 1, 1, 0, 0, 0, 1, 2, 1])

print(np.unique(zx))


