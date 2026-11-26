import numpy as np 

def manhattan_distance(vector1, vector2):
    return np.sum(np.abs(vector1 - vector2))


def assign_clusters(vectors, codebook):
    labels = []

    for vector in vectors:
        distances = []

        for centroid in codebook:
            distance = manhattan_distance(vector, centroid)
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
        
def split_centroid(centroid):
    c0 = np.floor(centroid)
    c1 = np.ceil(centroid)

    return c0, c1


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