import matplotlib.pyplot as plt
x=range(1,5000)
y=[y**3 for y in x]
plt.style.use("ggplot")
fig,ax=plt.subplots()
ax.scatter(x,y,s=50,c='purple')
ax.set_title("Sześciany")
ax.set_ylabel("kwadraty wartości f(x)=y")
ax.set_xlabel("wartości x ")




plt.show()
