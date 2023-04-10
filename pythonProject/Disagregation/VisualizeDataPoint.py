import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class KMeans:
    def __init__(self, k=2, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations

    def fit(self, X):
        # Initialize the centroids randomly
        self.centroids = X[np.random.choice(X.shape[0], self.k, replace=False)]

        for i in range(self.max_iterations):
            # Calculate the distances between the data points and the centroids
            distances = np.array([np.linalg.norm(X - centroid, axis=1) for centroid in self.centroids])

            # Assign each data point to the nearest centroid
            self.labels = np.argmin(distances, axis=0)

            # Update the centroids by taking the mean of all the data points assigned to each centroid
            new_centroids = np.array([X[self.labels == j].mean(axis=0) for j in range(self.k)])

            # If the centroids did not change, stop the iterations
            if np.allclose(new_centroids, self.centroids):
                break

            self.centroids = new_centroids

    def predict(self, X):
        distances = np.array([np.linalg.norm(X - centroid, axis=1) for centroid in self.centroids])
        return np.argmin(distances, axis=0)

################################################################


# Charger les données depuis le fichier CSV
data = pd.read_csv("CSVfiles/df2-2.csv")

data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d %H:%M:%S")

# Filtrer les données pour ne garder que celles qui correspondent à votre plage horaire
start_time = pd.Timestamp("2022-02-23 06:00:00")
end_time = pd.Timestamp("2022-02-23 20:00:00")

# Convert the date column to a scalar value representing the number of seconds since the start of the time period
data["seconds"] = (data["date"] - start_time).dt.total_seconds()

# Filter the data to keep only the data within the specified time range
data = data[(data["seconds"] >= 0) & (data["seconds"] <= (end_time - start_time).total_seconds()) & (data["debit"] != 0)]

# Convert the data to a numpy array
X = data[["seconds", "debit"]].values


# Create an instance of the KMeans class
kmeans = KMeans(k=4)

# Fit the KMeans model to the data
kmeans.fit(X)

# Get the centroids and the labels
centroids = kmeans.centroids

labels = kmeans.predict(X)

# Visualiser les données
plt.figure(figsize=(100, 10))
plt.scatter(X[labels==0,0], X[labels==0,1], color='blue', label='Cluster 1')
plt.scatter(X[labels==1,0], X[labels==1,1], color='red', label='Cluster 2')
plt.scatter(X[labels==2,0], X[labels==2,1], color='green', label='Cluster 3')
plt.scatter(X[labels==3,0], X[labels==3,1], color='orange', label='Cluster 4')
plt.scatter(centroids[:,0], centroids[:,1], color='black', label='Centroids')
plt.xlabel("Date")
plt.ylabel("Débit")
plt.legend()
plt.show()



# Add the cluster id as a new column in the dataframe
data["Cluster ID"] = labels

# Count the number of data points in each cluster
cluster_counts = np.unique(labels, return_counts=True)[1]

# Print the count for each cluster
for i, count in enumerate(cluster_counts):
    print(f"Cluster {i} has {count} data points")


# Save the updated dataframe to a new CSV file
#data.to_csv("data_with_cluster_id.csv", index=False)

