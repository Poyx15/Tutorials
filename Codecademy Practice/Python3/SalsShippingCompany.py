premium_ground_shipping = 125

def ground_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50 + 20.00
  elif weight <= 6:
    cost = weight * 3.00 + 20.00
  elif weight <= 10:
    cost = weight * 4.00 + 20.00
  else:
    cost = weight * 4.75 + 20.00
  return cost


def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 1.50
  elif weight <= 6:
    cost = weight * 3.00
  elif weight <= 10:
    cost = weight * 4.00
  else:
    cost = weight * 4.75
  return cost * 3


def check_cheapest(weight):
  if ground_shipping(weight) <= drone_shipping(weight) and ground_shipping(weight) <= premium_ground_shipping:
    return "Ground Shipping = " + str(ground_shipping(weight))
  elif drone_shipping(weight) <= ground_shipping(weight) and drone_shipping(weight) <= premium_ground_shipping:
    return "Drone Shipping = " + str(drone_shipping(weight))
  elif premium_ground_shipping <= drone_shipping(weight) and premium_ground_shipping <= ground_shipping(weight):
    return "Premium Shipping = " + str(premium_ground_shipping)
  else:
    return "Same Prices"

weight = 3.2
print(check_cheapest(weight))