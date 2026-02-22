🎯 Project Objective

To perform exploratory data analysis on Zomato sales data and extract meaningful business insights that help improve revenue, customer satisfaction, and operational efficiency

📊 Zomato Sales Data Analysis – Project Workflow
🔹 Step 1: Project Setup & Library Import
Imported essential Python libraries such as NumPy, Pandas for data handling.
Used Matplotlib and Seaborn for data visualization.
Set working directory to load dataset properly.
🔹 Step 2: Data Collection
Loaded dataset from Excel file (Zomato.xlsx) using pandas.read_excel().
Verified dataset structure using:
.head() → Preview first 5 records
.columns → Inspect column names
.describe() → Statistical summary of numerical features
🔹 Step 3: Data Preprocessing
✅ 3.1 Handling Missing Values
Checked null values using .isnull().sum()
Filled:
Rating & Delivery Time → Mode (most frequent value)
Sales → Mean value
✅ 3.2 Removing Duplicates
Removed duplicate records using .drop_duplicates()
Checked data types using .info()
🔹 Step 4: Exploratory Data Analysis (EDA)
📌 4.1 Sales vs Rating Analysis
Used scatter plot to analyze relationship between revenue and customer ratings.
Objective: Understand if higher ratings influence sales.
📌 4.2 City-wise Customer Loyalty Analysis
Grouped data by City.
Counted number of customers per city.
Visualized using bar chart.
Objective: Identify city with highest repeat customers.
📌 4.3 Order Frequency Analysis
Converted order date into datetime format.
Extracted day of week.
Analyzed order count per day.
Used line plot to identify peak ordering days.
📌 4.4 Restaurant Performance Analysis
Calculated average rating per restaurant.
Compared restaurant performance using bar chart.
Objective: Identify top-performing restaurants.
📌 4.5 Correlation Analysis
Computed correlation between numerical variables.
Visualized correlation matrix using heatmap.
Objective: Identify relationships between delivery time, sales, and rating.
🔹 Step 5: Business Insights Derived
Identified relationship between customer rating and sales performance.
Determined peak order days for operational planning.
Found most loyal customer city.
Evaluated restaurant performance based on ratings.
Analyzed impact of delivery time on sales.
📈 Tools & Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Excel Dataset
