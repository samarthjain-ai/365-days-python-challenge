import numpy as np
import statistics as st 
import matplotlib.pylab as plt 

data =  np.random.randint(1,50,20)

print(data)

mean=st.mean(data)
mode=st.mode(data)
median=st.median(data)

print(f"MEAN : {mean}")
print(f"MODE : {mode}")
print(f"MEDIAN : {median}")

name=["MEAN","MODE","MEDIAN"]
Values=[mean,mode,median]

plt.bar(name,Values,width=0.10)

plt.title("MEAN MODE MEDIAN")
plt.xlabel("NAME")
plt.ylabel("Values")

plt.show()