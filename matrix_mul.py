import threading

A = [[1, 2], [3, 4]]
B = [[2, 0], [1, 2]]
result = [[0]*len(B[0]) for _ in range(len(A))]

def multiply(i, j):
    result[i][j] = sum(A[i][k]*B[k][j] for k in range(len(B)))

threads = []
for i in range(len(A)):
    for j in range(len(B[0])):
        t = threading.Thread(target=multiply, args=(i, j))
        threads.append(t)
        t.start()

for t in threads:
    t.join()

print("Result:")
for row in result:
    print(row)
