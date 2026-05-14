s=int(input("Please enter the number of stairs"))
def num_stairs(s):
    if s==0:
        return 1
    if s<0:
        return 0
    return num_stairs (s-1)+num_stairs(s-2)
print(num_stairs(s))
print(num_stairs(s)*2)