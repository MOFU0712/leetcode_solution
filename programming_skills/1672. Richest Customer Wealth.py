accounts = [[1,5],[7,3],[3,5]]

maximum = 0

for account in accounts:
    if sum(account) > maximum:
        maximum = sum(account)

print(maximum)