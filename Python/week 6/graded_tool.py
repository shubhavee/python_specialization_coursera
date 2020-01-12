def computepay(h,r):
    total=0

    if(h<=40):
        total=h*r
        return total
    elif(h>40):
        total=40*r
        total=total+(h-40)*1.5*r
        return total


hrs = input()
h=float(hrs)
rate=input()
r=float(rate)

p = computepay(h,r)
print(p)
