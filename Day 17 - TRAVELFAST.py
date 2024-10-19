# Function to determine the faster mode of transport
def faster_transport(test_cases):
    results = []
    for x, y in test_cases:
        if x < y:
            results.append("BIKE")
        elif x > y:
            results.append("CAR")
        else:
            results.append("SAME")
    return results

# Input number of test cases
T = int(input("Enter number of test cases: "))

# Input each test case
test_cases = []
for _ in range(T):
    X, Y = map(int, input().split())
    test_cases.append((X, Y))

# Get results
results = faster_transport(test_cases)

# Output results
for result in results:
    print(result)
