# #steps of Tower of Hanoi
# def moveDisk(fp,tp):
#     print("moving disk from",fp,"to",tp)

# def moveTower(n,fromPole, toPole, withPole):
#     if n >= 1:
#         moveTower(n-1,fromPole,withPole,toPole)
#         moveDisk(fromPole,toPole)
#         moveTower(n-1,withPole,toPole,fromPole)


# moveTower(4,"A","B","C")

def moveDisk(fp,tp):
    print("Moving disk from", fp, "to", tp)

def moveTower(n, fromPole, toPole, withPole):
    if n >= 1:
        moveTower(n-1, fromPole, withPole,  toPole)
        moveDisk(fromPole, toPole)
        moveTower(n-1, withPole, toPole, fromPole)

moveTower(4,"A","B","C")


