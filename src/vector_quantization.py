import numpy as np 


def euclidean_distance(vector1, vector2):
    differences = vector1 - vector2
    squared_differences = differences ** 2
    sum_squared_differences = np.sum(squared_differences)
    distance = np.sqrt(sum_squared_differences)

    return distance


def assign_clusters(vectors, codebook):
    labels = []

    for vector in vectors:
        distances = []

        for centroid in codebook:
            distance = euclidean_distance(vector, centroid)
            distances.append(distance)

        closest_centroid = np.argmin(distances)
        labels.append(closest_centroid)

    return np.array(labels)  

def update_centroids(vectors, labels, k):
    new_centroids = []
    for i in range(k) :
        
        cluster_vectors = vectors[labels == i] 
        
        new_centroid = np.mean(cluster_vectors , axis = 0)
        
        new_centroids.append(new_centroid)
        
    return np.array(new_centroids)
        
    