import numpy as np

m_5x5=np.random.randint(0,1999,(5,5))
print("Mean ==>\n",m_5x5.mean())
print("Sum ==>\n",m_5x5.sum())
print("Transpose ==>\n",m_5x5.T)
print("Values > 500",m_5x5>500)
print("Flatten ==>\n",m_5x5.flatten())
import pandas as pd
data={
    "Name":["samarth","Bob","jhon","subh","jewal"],
    "Department":["AI","IT","HR","AI","HR"],
    "Marks":[90,56,45,78,67],
    "City":["Indore","Bhopal","Indore","Bhopal","Mumbai"]
}
df=pd.DataFrame(data)
print("Top 5 ==>\n",df.head())
print("Last 5 ==>\n",df.tail())
print("Sort_values ==>\n",df["Marks"].sort_values())
print("Value_count ==>\n",df["City"].value_counts())
print("Group by ==>\n",df.groupby("City")["Marks"].mean())

import matplotlib.pyplot as plt
city_avg=df.groupby("City")["Marks"].mean()
plt.bar(city_avg.index,city_avg.values,color=["Lightgreen","Lightblue","Yellow"])
plt.title("City vs Average Marks")
plt.xlabel("City")
plt.ylabel("Average Marks")
plt.show()