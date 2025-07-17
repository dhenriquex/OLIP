n = int(input())

zeros = 0
divisor = 5
while divisor <= n:
    zeros += n // divisor
    divisor *= 5

print(zeros)
