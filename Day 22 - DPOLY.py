def find_polynomial_degree(test_cases):
    results = []
    for case in test_cases:
        N = case[0]
        coefficients = case[1]
        
        # Find the highest non-zero coefficient
        degree = -1
        for i in range(N-1, -1, -1):
            if coefficients[i] != 0:
                degree = i
                break
        
        results.append(degree)
    
    return results

# Read input
T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    coefficients = list(map(int, input().split()))
    test_cases.append((N, coefficients))

# Find degrees
degrees = find_polynomial_degree(test_cases)

# Print results
for degree in degrees:
    print(degree)
