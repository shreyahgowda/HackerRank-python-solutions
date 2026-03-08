from collections import Counter

# number of shoes
X = int(input())

# list of shoe sizes
sizes = list(map(int, input().split()))

# count shoes
shoe_count = Counter(sizes)

# number of customers
N = int(input())

total_money = 0

for i in range(N):
    size, price = map(int, input().split())

    if shoe_count[size] > 0:
        total_money += price
        shoe_count[size] -= 1

print(total_money)