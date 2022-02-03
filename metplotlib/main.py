import matplotlib.pyplot as plt
input=[1,2,3,4,5,6,7,8,9]
list=[1,4,9,16,25,36,49,64,81]
plt.style.use('ggplot')
fig,ax=plt.subplots()

ax.plot(input,list,linewidth=4,c)
ax.set_title("kwadraty",fontsize=30)
ax.set_xlabel("Wartości",fontsize=20)
ax.set_ylabel("Kwadraty wartości",fontsize=18)
ax.tick_params(axis='both',labelsize=10)

plt.show()