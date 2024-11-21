def fibonacci_series(n):
  
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]
    
    # Initialize the series with the first two numbers
    series = [0,1]
    for i in range(2, n):
        
        series.append(series[-1]+series[-2])
    return series

# Input: Number of terms
num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
print("Fibonacci Series:", fibonacci_series(num_terms))