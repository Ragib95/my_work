#Calculate total pay

hrs = raw_input("Enter hours:")
hrs = float(hrs)
rate = raw_input("Enter pay hourly rate:")
rate = float(rate)

if hrs <=40:
	pay = hrs * rate
else:
    pay = 40 * rate + (hrs-40) * rate * 1.5

print pay
