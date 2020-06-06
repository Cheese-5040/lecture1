def computepay(h,r):
    total=(h-40)*1.5*r+40*r
    return total

h = int(input("Enter Hours:"))
r = float(input("Enter rate:"))
p = computepay(h,r)
print("Pay",p)