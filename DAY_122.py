# pie chart and scatter plot
import numpy as np
import matplotlib.pyplot as plt

marks =np.array([30,20,25,25])
subject =np.array(["CE","CLT","DAUP","ML"])
plt.pie(marks,labels=subject,explode=(0.1,0,0,0),colors=("r","b","g","y"),
        autopct="%1.2f%%",shadow=True,radius=1.0,labeldistance=1.1,
        pctdistance=0.5,startangle=90,counterclock=True,
        textprops={
            "fontsize" :15
        },
        wedgeprops={
            "linewidth":5,
            # "width":2
            "edgecolor":"black"
        },
        # center=(0,0),
        rotatelabels=True,
        )
plt.title("STUDENT MARKS")
plt.legend()
plt.show()


#dot pie chart 
plt.pie([1],colors="green")
plt.title("DOT pie chart")
plt.show()

#
marks =np.array([30,20,25,25])
mark1=np.array([10,20,30,40])

subject =np.array(["CE","CLT","DAUP","ML"])
plt.pie(marks,labels=subject,radius=1.1,autopct="%1.2f%%")
plt.pie(mark1,radius=0.5,colors=("r","g","c","b"),autopct="%1.2f%%")
plt.show()

# donat pie chart -1
marks =np.array([30,20,25,25])

subject =np.array(["CE","CLT","DAUP","ML"])
plt.pie(marks,labels=subject,radius=1.6,autopct="%1.2f%%",pctdistance=0.5)
plt.pie([1],colors="white")
plt.show()

# 2

marks =np.array([30,20,25,25])

subject =np.array(["CE","CLT","DAUP","ML"])
plt.pie(marks,labels=subject,radius=1.6,autopct="%1.2f%%",pctdistance=0.5)
cr =plt.Circle(xy=(0,0),radius=1,facecolor="w")
plt.gca().add_artist(cr)
plt.show()

day=[1,2,3,4,5,6,7,8]
number=[2,4,5,7,8,9,0,4]
# SAME COLOR
plt.scatter(day,number,color="g")
plt.title("Sactter plot",fontsize=15)
plt.xlabel("DAY",fontsize=15)
plt.ylabel("NUMBER",fontsize=15)
plt.show()

day=[1,2,3,4,5,6,7,8]
number=[2,4,5,7,8,9,0,4]
# differnt COLOR
#alpha= 0-1
plt.scatter(day,number,c=["r","g","b","c","b","c","y","g"],s=[400,500,273,465,576,687,748,1300],alpha=0.4,
            marker="*",edgecolors="blue",linewidths=3) 

plt.title("Sactter plot",fontsize=15)
plt.xlabel("DAY",fontsize=15)
plt.ylabel("NUMBER",fontsize=15)
plt.show()

day=[1,2,3,4,5,6,7,8]
number=[2,4,5,7,8,9,0,4]
number2=[12,32,4,5,6,7,8,9]
number3=[34,45,7,8,13,11,17,18]
# cmap
colors=[1,22,45,65,45,23,12,32]
plt.scatter(day,number,c=colors,cmap="viridis") 

plt.scatter(day,number2,c=colors,cmap="viridis") 
plt.scatter(day,number3,c=colors,cmap="viridis") 

t=plt.colorbar()
t.set_label("Color bar",fontsize=15)
plt.title("Sactter plot",fontsize=15)
plt.xlabel("DAY",fontsize=15)
plt.ylabel("NUMBER",fontsize=15)
plt.show()         