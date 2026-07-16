import matplotlib.pylab as plt 
import numpy as np
data = [5,10,15,20,25,30,35,40,50]
minimun=min(data)
maximun = max(data)

range=maximun-minimun

print(f"RANGE : {range}")
print(f"MAXiMUN : {maximun}")
print(f"MINIMUN : {minimun}")

plt.scatter(data ,[1]*len(data))

plt.scatter(minimun,1,s=24,label="MINIMUM")
plt.scatter(maximun,1,s=24,label="MAXIMUN")

plt.hlines(y=1,xmin=minimun,xmax=maximun)

plt.title("Visualization of Range")
plt.xlabel("DATA Values")
plt.yticks([])
plt.legend()
plt.show()

