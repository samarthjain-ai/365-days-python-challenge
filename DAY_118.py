#pip install matplotlib
import matplotlib.pyplot as plt
import numpy as np

# 1) Line Graph
# Use: Shows trend / change over time

# 2) Bar Chart
# Use: Compares categories

# 3) Histogram
# Use: Shows frequency distribution of data

# 4) Pie Chart
# Use: Shows percentage / proportion

# 5) Heatmap
# Use: Shows data intensity using colors

# 6) Scatter Plot / Bubble Plot
# Use: Shows relationship between variables


# 1 Line Graph
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, color='lightgreen', linewidth=5, linestyle='-', marker='o', label='my Line')
# colour , line size , point where x and y meet denoted by , this line name
plt.title('Line Graph') # Graph name
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend() # box at the top and show label
plt.grid(False)   # defult True
plt.show()

# 2 Bar Chart

categories = ['A', 'B', 'C', 'D'] # x-axis
values     = [10, 25, 15, 30] # y-axis

plt.bar(categories, values, color=['red','blue','green','orange'],) 
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.show()

# 3 Histogram

data = np.random.randint(1,100,1000)  # 1000 random normal values
plt.hist(data, bins=30, color='lightblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()

# 4 Pie Chart
labels  = ['Python', 'Java', 'C++', 'JS']
sizes   = [40, 25, 20, 15]
explode = (0.1, 0, 0, 0)   # "pop out" first slice

plt.pie(sizes, labels=labels, explode=explode , shadow=True)  #startangle=90
plt.title('Language Popularity')
plt.show()

# 5  Heatmap
data = np.random.rand(8, 8)

plt.imshow(data, cmap='hot', interpolation='nearest') #interpolation='nearest' Keep blocks sharp.
# theme cmap='hot'  it can be
plt.colorbar()  # add side bar
plt.title('Heatmap')
plt.show() 
# Theme	Color Combo
# hot	    Black → Red → Orange → Yellow → White 
# viridis	Dark Purple → Blue → Green → Yellow
# plasma	Purple → Pink → Orange → Yellow
# inferno	Dark Purple → Red → Orange → Yellow
# magma	    Black → Purple → Red → Orange → Yellow
# cividis	Blue → Gray → Yellow
# cool	    Cyan → Pink
# spring	Magenta → Yellow
# summer	Green → Yellow
# autumn	Red → Yellow
# winter	Blue → Green
# gray	    Black → White
# bone	    Dark Gray → Light Blue → White
# pink	    Dark Pink → Light Pink → White
# jet	    Blue → Cyan → Yellow → Red 🌈
# rainbow	Violet → Blue → Green → Yellow → Orange → Red 🌈
# hsv	    Full rainbow circle
# Greys	    Light Gray → Dark Gray
# Blues	    Light Blue → Dark Blue
# Greens	Light Green → Dark Green
# Reds	    Light Red → Dark Red
# Purples	Light Purple → Dark Purple
# Oranges	Light Orange → Dark Orange

#  Scatter Plot / Bubble Plot
x = np.random.rand(50)
y = np.random.rand(50)
sizes = np.random.rand(50) * 200   # bubble size Creates 50 random sizes *200 makes circles bigger.

colors = np.random.rand(50)        # color intensity

plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.7)
plt.colorbar()   # adds color scale bar
plt.title('Scatter Plot')
plt.show()  

# Example
# Marks analysis  
# Sales report  
# AI model accuracy graph  
# Weather trend  
# Population comparison
# define--> Matplotlib is a Python library used for data visualization.
# It helps convert numbers/data into graphs and charts.