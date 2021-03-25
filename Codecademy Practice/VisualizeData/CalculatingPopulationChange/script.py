# https://www.codecademy.com/paths/visualize-data-with-python/tracks/introduction-to-python-dvp/modules/python-functions-dvp/projects/population-project

def population_growth(year_one, year_two, population_1, population_2):
  time_elapsed = year_two - year_one
  pop_change = population_2 - population_1
  percentage_gr = (pop_change/population_1)*100
  annual_gr = percentage_gr/time_elapsed
  return annual_gr

year = [1927, 1950, 2000, 2017]
population = [691000, 983000, 8831800, 15029231]
year_pop_dict = dict(zip(year, population))

city_name = "Istanbul, Turkey"
pop_1927 = 691000
pop_2017 = 15029231
x = 0
y = -1
# print(population_growth(year[x], year[y], population[x], population[y]))
set_one = population_growth(year[x], year[y], population[x], population[y])
print(set_one)
x = 1
y = -2
set_two = population_growth(year[x], year[y], population[x], population[y])
print(set_two)
