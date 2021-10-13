"""
 Quadratic equation
 By: M.Yekmaz
 Date: 1400/07/21
"""
print("For a quadratic equation like ax^2+bx+c=0")
a=int(input("Please enter a: "))
b=int(input("Please enter b: "))
c=int(input("Please enter c: "))

if a>=0:
    if a==0:
        fs=""
    elif a==1:
        fs = "x^2"
    else:
        fs = f"{a}x^2"
else:
    if a==-1:
        fs = f"-x^2"
    else:
        fs = f"{a}x^2"

if b>=0:
    if b==0:
        ss=""
    elif b==1:
        ss = "+x"
    else:
        ss = f"+{b}x"
else:
    if b==-1:
        ss = "-x"
    else:
        ss = f"{b}x"

if c>=0:
    if c==0:
        ts=""
    else:
        ts = f"+{c}"
else:
    ts = f"{c}"

print(f"You entered {fs}{ss}{ts}")

delta=b**2-4*a*c

if delta<0:
    print(f"This equation has no root.")
elif delta == 0:
    root = (-b)/(2*a)
    print(f"This equation has a root that is {root}.")
else:
    root1=(-b+delta**0.05)/(2*a)
    root2=(-b-delta**0.05)/(2*a)
    print(f"This equation has two root that are {root1} and {root2}.")
