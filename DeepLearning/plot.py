import matplotlib.pyplot as plt
import numpy

cost=[1.0144926, 0.96602422, 0.024328001, 0.084135853, 0.016160158, 0.025197307, 0.009908339, 0.01657806, 0.0081786923, 0.013121139, 0.0070881136, 0.011028621, 0.0063030426, 0.0096297041, 0.0056963619, 0.0085926503, 0.005211385, 0.0077778683, 0.0048120469, 0.0071275895, 0.0044746906, 0.006589605, 0.004183189, 0.006135819, 0.0039332267, 0.0057431147, 0.0037121987, 0.0054046381, 0.0035161029, 0.0051041786, 0.0033395544, 0.0048419037, 0.0031820005, 0.0046072733, 0.0030369759, 0.0043934993, 0.0029067376, 0.0042033275, 0.0027854857, 0.0040287729]



x = range(0,len(cost),1)

plt.plot(x,cost)
plt.show()


# pred=[ 0,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,
#   0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,
#   0,1,0,0,0,0,1,0,0,0,0,0,0,0]
#
# act=[ 1,0,1,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,
#   0,0,1,1,1,1,1,0,0,0,0,0,0,1,0,1,1,0,
#   0,0,1,0,0,0,1,0,0,1,1,0,1,0]
#
# normal=0
# nodule=0
# nod_nor=0
# nor_nod=0
# for i,j in zip(pred,act):
#     if i==j and j==0:
#         normal+=1
#     elif i==j and j==1:
#         nodule+=1
#     elif i!=j and j==0:
#         nor_nod+=1
#     elif i!=j and j==1:
#         nod_nor+=1
#
# print normal
# print nodule
# print nod_nor
# print nor_nod
