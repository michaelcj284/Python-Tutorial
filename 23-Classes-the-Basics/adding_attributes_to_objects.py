def root_sum(n):
    x = sum(int(i) for i in str(n))
    if x > 9:
       return root_sum(x)
    return x

print(root_sum(942))