def donut_costs(num_donuts, member):
  price_per_donut = 90
  
  if num_donuts > 1 and num_donuts < 10:
    price_per_donut = 80
  
  if num_donuts >= 10:
    price_per_donut = 70

  if member:
    price_per_donut -= 5

  return num_donuts * price_per_donut


if __name__ == "__main__":
  print(donut_costs(1, False))
  print(donut_costs(6, True))
  print(donut_costs(15, False))