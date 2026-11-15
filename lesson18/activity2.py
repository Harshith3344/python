def palind(r):
    e = len(r) - 1
    s = 0
    while(s < e):
        if r[s] != r[e]:
            return False
        s += 1
        e -= 1
    return True


r = (7,8,9,9,8,7)

if(palind(r)):
    print("The tuple is flip-flop")
else:
    print("the tuple is not flip-flop")