def fibonacci(n):
    if n <= 1:
        return n
    else:
        return ((n-1) + (n-2))


n = int(input("Введите последовательность:"))
print("Последовательность Фибоначчи:")
for i in range(n):
    print(fibonacci(i))
