M = int(input("Enter the starting number (M): "))
N = int(input("Enter the ending number (N): "))
K = int(input("Enter the number to skip (K): "))

for i in range(M, N + 1, K):
    print(i)
