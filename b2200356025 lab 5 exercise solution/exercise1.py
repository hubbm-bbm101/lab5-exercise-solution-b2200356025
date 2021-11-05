n = int(input("Please enter a positive integer"))
odd_sum = 0
even_sum = 0
even_number = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
        even_number += 1
    else:
        odd_sum += i
even_avg = even_sum / even_number
print("sum of odd numbers:", str(odd_sum))
print("average of even numbers:", str(even_avg))
