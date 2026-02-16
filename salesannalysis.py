#Importing required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os 
os.chdir("D:/Myprojects/ZomatosalesDataanalysisbypython")

##Data collection and Basic inspection about sales 
sales=pd.read_excel('Zomato.xlsx')
print(sales.head(5))
print(sales.columns)
print(sales.describe())

##Data preprocessing
#Missing values
sales.isnull().sum()
sales.fillna({'Rating':sales['Rating'].mode(),'Delivery_Time(mins)':sales['Delivery_Time(mins)'].mode(),'Sales':sales['Sales'].mean()},inplace=True)
#Handling duplicates
sales.drop_duplicates(inplace=True)
sales.info()


##Price vs rating Relationships
my_colors = ["#FF6347", "#4682B4", "#8A2BE2", "#FFD700"]
sns.scatterplot(x="Sales",y='Rating',data=sales,hue='Rating')
plt.title("Price vs Rating Relationship")
plt.xticks(rotation =20,ha = 'right')
plt.savefig('pricevsrating.jpg')
plt.show()
##Which city has the most loyal customers?
cityloyality=sales.groupby('City')['Customer_Name'].count()
sns.barplot(x=cityloyality.index,y=cityloyality.values,palette = my_colors)
plt.xticks(rotation =20,ha = 'right')
plt.title("Which city has the most loyal customers")
plt.xlabel("City")
plt.ylabel("Customers Count")
plt.savefig('loyalcustomers.jpg')

plt.show()
##Order Frequency
sales['Day']=pd.to_datetime(sales['Order_Date'])
sales['Day']=sales['Day'].dt.day_of_week
Daysorders=sales.groupby('Day')['Customer_Name'].count()
sns.lineplot(x=Daysorders.index,y=Daysorders.values,color='red')
plt.xlabel("DayOrders")
plt.ylabel("No,of sales ")
plt.xticks(rotation =20,ha = 'right')
plt.tight_layout(pad=2.0)
plt.title("Order frequency")
plt.savefig('orderfrequwncy.jpg')
plt.show()

##Restaurant Performance
rtrrating=sales.groupby('Restaurant_Name')['Rating'].mean()
sns.barplot(x=rtrrating.index,y=rtrrating.values,hue  = rtrrating.index)
plt.title('Restaurant vs Rating Performance')
plt.ylabel('Rating Count')
plt.xticks(rotation =20,ha = 'right')
plt.savefig('restaurantperformance.jpg')
plt.show()

#correlations between numarical columns
corr = sales.corr(numeric_only = True)
sns.heatmap(corr,cmap = 'coolwarm')
plt.savefig('correlations.jpg')

plt.show()

