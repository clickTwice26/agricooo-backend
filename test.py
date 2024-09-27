

def multiplcation(x, startPoint):
    if startPoint > 10:
        return None
    print(f"{x} x {startPoint} = {int(x * startPoint)}")
    multiplcation(x, startPoint+1)



multiplcation(3, 1)


