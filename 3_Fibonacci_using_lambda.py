fibonacci_series = []
a,b = 0,1
while b <= 50:
    fibonacci_series.append(b)
    a, b = b, (lambda x,y: x+y) (a,b)
print(fibonacci_series)


