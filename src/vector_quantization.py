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
        
def split_centroid(centroid , elipson = 0.01) :
    c0 = centroid * (1 - elipson) 
    c1 = centroid * (1 + elipson)
    
    return c0 , c1  


def train_codebook(vectors, k, max_iterations=100):
    initial_centroid = np.mean(vectors , axis = 0)
    codebook = np.array([initial_centroid])
    while len(codebook) < k:

        new_codebook = []
        for centroid in codebook:
            c0, c1 = split_centroid(centroid)

            new_codebook.append(c0)
            new_codebook.append(c1)
            
        codebook = np.array(new_codebook)
        
    for i in range(max_iterations) :
        labels = assign_clusters(vectors , codebook)
        new_codebook = update_centroids(vectors , labels , k)
        
        if np.allclose(codebook, new_codebook):
            codebook = new_codebook
            break
        
        codebook = new_codebook 
        
    return codebook 