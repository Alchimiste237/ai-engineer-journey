import numpy as np

class VectorOps:
    """Collection of vector operations used throughout AI/ML."""

    @staticmethod
    def dot_product(a, b):
        """Manual dot product without np.dot."""
        return sum(ai * bi for ai, bi in zip(a, b))

    @staticmethod
    def cosine_similarity(a, b):
        """Similarity between -1 and 1."""
        a, b = np.array(a), np.array(b)
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    @staticmethod
    def euclidean_distance(a, b):
        """
        Straight-line distance between two points.
        Used in KNN algorithm and clustering.
        """
        a, b = np.array(a), np.array(b)
        return np.linalg.norm(a - b)

    @staticmethod
    def normalize(v):
        """Scale vector to unit length."""
        norm = np.linalg.norm(v)
        return v / norm if norm != 0 else v


class MatrixOps:
    """Matrix operations used in ML."""

    @staticmethod
    def multiply(A, B):
        """Matrix multiplication from scratch ."""
        A, B = np.array(A), np.array(B)
        rows_A, cols_A = A.shape
        rows_B, cols_B = B.shape
        assert cols_A == rows_B, f"Shape mismatch: {A.shape} @ {B.shape}"

        C = np.zeros((rows_A, cols_B))
        for i in range(rows_A):
            for j in range(cols_B):
                for k in range(cols_A):
                    C[i][j] += A[i][k] * B[k][j]
        return C

    @staticmethod
    def softmax(v):
        """
        Converts raw scores to probabilities (sum = 1).
        Used in classification output layers and attention mechanisms.
        """
        exp_v = np.exp(v - np.max(v))   # subtract max for numerical stability
        return exp_v / exp_v.sum()


# Test
ops = VectorOps()
print(ops.cosine_similarity([1,0,0], [1,0,0]))    # 1.0 (identical)
print(ops.cosine_similarity([1,0,0], [0,1,0]))    # 0.0 (perpendicular)
print(ops.euclidean_distance([0,0], [3,4]))        # 5.0 (3-4-5 triangle)

scores = np.array([2.0, 1.0, 0.5])
print(MatrixOps.softmax(scores))  # [0.626, 0.230, 0.144] — sums to 1.0
