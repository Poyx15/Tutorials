def update_order(new_item, current_order=None):  # parameters cant be a group of list or dictionaries
  if current_order is None:
    current_order = []
  current_order.append(new_item)
  return current_order

# First order, burger and a soda
order1 = update_order({'item': 'burger', 'cost': '3.50'})
order1 = update_order({'item': 'soda', 'cost': '1.50'}, order1)

# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})

# What's in that second order again?
print(order2)


# def update_order(new_item, current_order=[]):  # This will result in a repeated value list
#   current_order.append(new_item)
#   return current_order