import math

def min_wins_to_qualify(test_cases):
    results = []
    for x, y in test_cases:
        if x <= y:
            results.append(0)
        else:
            # Calculate the minimum wins needed
            min_wins = math.ceil((x - y) / 1)
            results.append(max(min_wins, 0))
    return results

# Read input
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = min_wins_to_qualify(test_cases)

# Output results
for res in results:
    print(res)
