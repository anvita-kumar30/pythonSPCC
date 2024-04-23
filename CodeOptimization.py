# import time
# def sum_of_squares_original(n):
#     """Original function using iterative summation."""
#     total = 0
#     for i in range(1, n + 1):
#         total += i ** 2
#     return total
# def sum_of_squares_optimized(n):
#     """Optimized function using a direct formula."""
#     return (n * (n + 1) * (2 * n + 1)) // 6
# def measure_execution_time(func, *args):
#     """Measure execution time of a function."""
#     start_time = time.time()
#     result = func(*args)
#     execution_time = time.time() - start_time
#     return result, execution_time
# if __name__ == "__main__":
#     n = 10000
#     # Measure execution time for the original function
#     original_result, original_time = measure_execution_time(sum_of_squares_original, n)
#     # Measure execution time for the optimized function
#     optimized_result, optimized_time = measure_execution_time(sum_of_squares_optimized, n)
#     # Print results
#     print(f"Original: Sum of squares from 1 to {n}: {original_result}")
#     print(f"Optimized: Sum of squares from 1 to {n}: {optimized_result}")
#     # Print execution times
#     print(f"Execution time (original): {original_time:.6f} seconds")
#     print(f"Execution time (optimized): {optimized_time:.6f} seconds")
