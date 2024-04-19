import time

def sum_of_squares(n):
    result = 0
    for i in range(1, n+1):
        result += i * i
    return result

def sum_of_squares_optimized(n):
    return (n * (n + 1) * (2 * n + 1)) // 6

# Test the original function
start_time = time.time()
result_original = sum_of_squares(10000)
end_time = time.time()
print(f"Original Function Result: {result_original}")
print(f"Time taken by original function: {end_time - start_time} seconds")

# Test the optimized function
start_time = time.time()
result_optimized = sum_of_squares_optimized(10000)
end_time = time.time()
print(f"Optimized Function Result: {result_optimized}")
print(f"Time taken by optimized function: {end_time - start_time} seconds")
