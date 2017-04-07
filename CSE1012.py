def drawLSystem(string,angle,distance):
    import turtle
    turtle.pencolor('black')
    turtle.pensize(1)
    for n in string:
        if n=='F':
            turtle.forward(distance)
        elif n=='+':
            turtle.right(angle)
           # turtle.forward(distance)
        elif n=='-':
            turtle.left(angle)
            #turtle.forward(distance)
    turtle.done()

def deriveLSystem(seed,productions,depth):
    if depth==0:
        a=seed
        for n in productions:
            a=a.replace(n,productions[n])
        return a
    else:
        a=deriveLSystem(seed, productions, depth - 1)
        for n in productions:
            a=a.replace(n,productions[n])
        return a

a={'X':'X-YF','Y':'FX+Y'}
b=deriveLSystem("FX",a,10)
a='F-F++F-F'
drawLSystem(b,60,10)
