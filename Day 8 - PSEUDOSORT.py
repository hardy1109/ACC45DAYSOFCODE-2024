def is_pseudo_sorted(arr):
    n = len(arr)
    
    # Check if the array is already sorted
    if all(arr[i] <= arr[i + 1] for i in range(n - 1)):
        return True
    
    # Find the first pair that is out of order
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # Try swapping arr[i] and arr[i + 1]
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            
            # Check if the array is sorted after the swap
            if all(arr[j] <= arr[j + 1] for j in range(n - 1)):
                return True
            
            # Swap back to original order
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            break
    
    return False

def process_test_cases(test_cases):
    results = []
    for case in test_cases:
        n, arr = case
        if is_pseudo_sorted(arr):
            results.append("YES")
        else:
            results.append("NO")
    return results

# Example usage
T = int(input())
test_cases = []
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    test_cases.append((N, A))

results = process_test_cases(test_cases)
for result in results:
    print(result)

