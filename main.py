import pandas as pd

# Load dataset
df = pd.read_csv("Mall_Customers.csv")

# Show first 5 rows
print("First 5 rows:")
print(df.head())

# Dataset info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())
# Select required features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]
print("\nSelected Features:")
print(X.head())

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print("\nScaled Data:")
print(X_scaled[:5])


from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=5, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

print("\nCluster Labels:")
print(clusters[:10])

df['Cluster'] = clusters
print("\nData with Clusters:")
print(df.head())

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(8,6))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df)

plt.title('Customer Segments')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')

plt.show()

df.to_csv("clustered_customers.csv", index=False)