def hash_calculator():
    n = int(input())
    t = tuple(list(map(int, input().split()))[:n])
    # t=(1,2)
    print(t)
    return hash(t)

print(hash_calculator())

# var = ('G','E','E','K')
 
# print(hash(var))
