def maximize_tastiness(a, b, c, d):
    return max(a + c, a + d, b + c, b + d)

# Reading input
T = int(input())
results = []

for _ in range(T):
    a, b, c, d = map(int, input().split())
    results.append(maximize_tastiness(a, b, c, d))

# Printing the results
for result in results:
    print(result)

