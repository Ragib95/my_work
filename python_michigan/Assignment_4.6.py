#Define function computepay
def computepay(h,r):
	if h <= 40:
		pay = h * r
	else:
	    pay = 40 * r +	(h-40) * r * 1.5
	return pay    

hrs = raw_input("Enter Hours:")
hrs = float(hrs)
rph = raw_input("Enter Rate:")
rate = float(rph)

p = computepay(hrs,rate)
print "Pay",p