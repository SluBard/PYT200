# Setup
def multiply(x,y):
    return x*y

def is_odd(num):
    return num % 2

nums1 = range(0,10)
nums2 = range(10,0,-1)

# map()
for i in map(multiply, nums1, nums2):
    print(i)

# filter
for i in filter(is_odd,nums1):
    print(i)