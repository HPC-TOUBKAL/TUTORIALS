import numpy as np

def main():
    array_size_gb = 10  # Adjust as needed
    array_size_bytes = array_size_gb * 1024**3
    A = np.zeros(array_size_bytes, dtype=np.float64)
    B = np.zeros(array_size_bytes, dtype=np.float64)

    C = A + B 

if __name__ == "__main__":
    main()
