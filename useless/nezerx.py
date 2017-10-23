from random import randint

r1 = random.uniform(0, 9999)
r2 = random.uniform (0, 9999)
t = random.randint(1, 4)
if t == 1:
    a = eval(r1+r2)
    anc = input(r1, "+", r2, "=")
    if int(anc) == r1+r2:
        print("True")
    else:
        print("False")
