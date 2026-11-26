import numpy as np
from src.vector_quantization import train_codebook, assign_clusters


def test_train_codebook():
    vectors = np.array([
        [2, 4],
        [3, 5],
        [8, 10],
        [9, 11]
    ])

    codebook = train_codebook(vectors, 2)

    print("Codebook:")
    print(codebook)

    print("Labels:")
    print(assign_clusters(vectors, codebook))

    assert codebook.shape == (2, 2)
    assert np.allclose(codebook, [[2.5, 4.5], [8.5, 10.5]])