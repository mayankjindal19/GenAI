import numpy as np

def main():
    print("Hello from myproject!")

    # Sample numpy code
    arr = np.array([1, 2, 3, 4, 5])
    print("Array:", arr)
    print("Mean:", np.mean(arr))
    print("Sum:", np.sum(arr))

    # Matrix operations
    matrix = np.array([[1, 2], [3, 4]])
    print("Matrix:\n", matrix)
    print("Transpose:\n", np.transpose(matrix))


if __name__ == "__main__":
    main()
