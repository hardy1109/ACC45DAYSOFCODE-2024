import math

def minimum_total_cost(N, X):
    # Calculate the number of subscriptions needed
    subscriptions_needed = math.ceil(N / 6)
    # Calculate the total cost
    total_cost = subscriptions_needed * X
    return total_cost

def main():
    T = int(input())  # Number of test cases
    results = []
    for _ in range(T):
        N, X = map(int, input().split())
        results.append(minimum_total_cost(N, X))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
