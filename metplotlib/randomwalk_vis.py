

import matplotlib.pyplot as plt
from  random_walk import RandomWalk
rw=RandomWalk(5000)
rw.fill_walk()
plt.style.use("classic")
pointn=range(rw.numpoints)
fig,ax=plt.subplots()
ax.scatter(rw.x_value,rw.y_value,c=pointn,cmap=plt.cm.Reds,edgecolor='none',s=15)
plt.show()