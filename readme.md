# Customer Segmentation using K-Means Clustering

##  Project Overview

This project uses **K-Means Clustering** to group customers of a retail store based on their purchasing behavior.
The goal is to identify different customer segments to help businesses make better marketing decisions.

---

##  Dataset

* Dataset: Mall Customers Dataset
* Features used:

  * Annual Income (k$)
  * Spending Score (1–100)

---

##  Objective

To segment customers into different groups based on:

* Income
* Spending habits

This helps businesses:

* Target the right customers
* Improve marketing strategies
* Increase revenue

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn

---

##  Steps Performed

1. **Data Loading**

   * Loaded dataset using Pandas

2. **Data Exploration**

   * Checked structure using `.head()`, `.info()`
   * Verified missing values

3. **Feature Selection**

   * Selected relevant features:

     * Annual Income
     * Spending Score

4. **Data Preprocessing**

   * Applied StandardScaler for normalization

5. **Model Training**

   * Used K-Means clustering algorithm
   * Number of clusters: 5

6. **Cluster Assignment**

   * Assigned cluster labels to each customer

7. **Visualization**

   * Plotted clusters using Seaborn scatter plot

---

## 📈 Output

* Customers grouped into 5 clusters
* Visualization showing different customer segments
* New dataset with cluster labels: `clustered_customers.csv`

---



## 📂 Project Structure

```
├── main.py
├── Mall_Customers.csv
├── clustered_customers.csv
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run

1. Clone the repository
2. Create virtual environment
3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the project:

```
python main.py
```

---

## 💡 Key Insights

* Customers can be grouped into distinct segments
* High-income & high-spending customers are most valuable

---



## ⭐ Conclusion

This project demonstrates how machine learning can be used to understand customer behavior and improve business decisions.
