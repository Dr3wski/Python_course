lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""
lovely_loveseat_price = 254.00
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

stylish_settee_price = 180.50
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""
luxurious_lamp_price = 52.15
sales_tax = .088

customer_one_total = 0
customer_one_itemization = ""
customer_one_total += lovely_loveseat_price
customer_one_itemization = lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
print(customer_one_total)
print(customer_one_itemization)
customer_one_tax = (customer_one_total*sales_tax)
customer_one_total += customer_one_tax
print(customer_one_tax)

print("Customer One Items:")
print(customer_one_itemization)
print("Customer One Total:")
print(customer_one_total)


customer_two_total = 0
customer_two_itemization = ""
customer_two_total += stylish_settee_price
customer_two_itemization += stylish_settee_description
customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description
customer_two_tax = (customer_two_total*sales_tax)

customer_two_total += customer_two_tax
print("Customer Two Items:")
print(customer_two_itemization)
print("Customer Two Total:")
print(customer_two_total)


##Functions: 
  def create_spreadsheet(title, row_count=1000):
  print("Creating a spreadsheet called "+ title+" with "+str(row_count)+" rows")
create_spreadsheet("Downloads")
create_spreadsheet("Applications",row_count=10)


## functions definition and calc section week 2
train_mass = 22680
train_acceleration = 10
train_distance = 100


bomb_mass = 1

def f_to_c(f_temp):
	c_temp = ((f_temp - 32) * 5/9)
	return c_temp
	
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
	f_temp = (c_temp * (9/5) +32)
	return f_temp

c0_in_farenheit = c_to_f(0)
print(c0_in_farenheit)

def get_force(mass, acceleration):
  return(mass*acceleration)

train_force = get_force(train_mass, train_acceleration)
print(train_force)

print("The GE train supplies " + str(train_force) + " Newtons of force")

def get_energy(mass, c = None):
  if c is None: 
     c = 3*10**8
  return (mass * (c**2))
  
bomb_energy = get_energy(bomb_mass)

print(bomb_energy)

print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  force = get_force(mass, acceleration)
  return (force * distance)

train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters.")



#Wins calculation
# Write your win_percentage function here:
def win_percentage(wins, losses):
  total = wins + losses
  return (wins/total)*100
# Uncomment these function calls to test your win_percentage function:
#print(win_percentage(5, 5))
# should print 50
#print(win_percentage(10, 0))
# should print 100
print(win_percentage(5, 5))
print(win_percentage(10, 0))



# Shipping task

def ground_shipping(weight):
  flat_charge = 20
  if (weight <= 2):
    return (weight*1.5) + (flat_charge)
  elif (weight > 2) and (weight <= 6): 
    return(weight*3) + (flat_charge)
  elif (weight > 6) and (weight <= 10): 
    return (weight*4) + (flat_charge)
  else:
    return (weight*4.75) + (flat_charge)
  
print(ground_shipping(8.4))

premium_ground_shipping = 125

def drone_shipping(weight): 
  flat_charge = 0
  if (weight <= 2):
    return (weight*4.5) + (flat_charge)
  elif (weight > 2) and (weight <= 6): 
    return(weight*9) + (flat_charge)
  elif (weight > 6) and (weight <= 10): 
    return (weight*12) + (flat_charge)
  else:
    return (weight*14.25) + (flat_charge)
  
  
print(drone_shipping(1.5))

def best_method(weight):
  if (ground_shipping(weight)) < (premium_ground_shipping) and (ground_shipping(weight)) < (drone_shipping(weight)): 
    print("Ground shipping is your cheapest option, it will cost $"+ str(ground_shipping(weight)))
  elif (drone_shipping(weight)) < (premium_ground_shipping) and (drone_shipping(weight)) < (ground_shipping(weight)):
    print("Drone Shipping is your cheapest option, it will cost $" +str(drone_shipping(weight)))
  else: 
    print("Premium Delivery is your best option")



best_method(4.8)
best_method(41.5)


      
      
      
