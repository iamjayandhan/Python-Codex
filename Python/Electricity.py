# default values 
#eb_number = 1234
consumed = 0 
bill_amount = 0

# get the input from user
eb_number = int(input("Enter the TNEB Consumer Number : "))
last_bill_units = int(input("Enter the Last Bill Meter Reading : "))
current_units = int(input("Enter Current Bill Meter Reading : "))

consumed = current_units - last_bill_units 

# Calculate the bill

# bill calculation default values 
s101_200_rate = 1.5
s201_500_rate = 3
fixed_charges = 0 
s101_200_charges = 0
s201_500_charges = 0 

# vary the default rates based on consumption
if consumed > 100: 
	fixed_charges = 20 
if consumed > 200: 
	fixed_charged = 30 
	s101_200_rate = 2

# divy up the units into various slabs
units_to_charge = consumed

print("---Slab Calculations---")

s201_500U = units_to_charge - 200
if s201_500U > 0: 
	s201_500_charges = s201_500U * s201_500_rate
	print("%20s" % "slab 201-500 charges:", s201_500_charges)
	units_to_charge -= s201_500U
	
units_to_charge = units_to_charge - 100
if units_to_charge > 0:
	s101_200U = units_to_charge 
	s101_200_charges = s101_200U * s101_200_rate 

	fixed_charges = 20 

	print("%20s" % "slab 101-200 charges:", s101_200_charges)
	print("%20s " % "fixed charges:", fixed_charges)

bill_amount = fixed_charges + \
	s101_200_charges + \
	s201_500_charges 

# print a summary bill amount

print("\nTamilnadu Electricity Board")
print("------------------------------")
print("EB Number         : ", eb_number)
print("Units Consumption : ", consumed)
print("Bill Amount       : Rs.", bill_amount)
print("------------------------------")
