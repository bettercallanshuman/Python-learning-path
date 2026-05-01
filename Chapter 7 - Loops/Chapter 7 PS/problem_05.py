#Write a program to find the sum of first n natural numbers using while loop.

n = int(input("Enter the number: "))
sum_total = 0 # Your "bucket"
i = 1         # Your "counter" (starting natural number)

while(i <= n):
    sum_total += i  # Add the current number to the bucket
    i += 1          # Move to the next number

print(f"The sum of first {n} natural numbers is {sum_total}")