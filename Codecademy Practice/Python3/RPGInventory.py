available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points = health_points + available_items.get("stamina grains", 0)
available_items.pop("stamina grains")

health_points = health_points + available_items.get("power stew", 0)
available_items.pop("power stew")

health_points = health_points + available_items.get("mystic bread", 0)
available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)


class Circle:
    def area(self, radius):
        pi = 3.14
        return pi * radius ** 2


circle = Circle()

pizza_area = circle.area(12)
teaching_table_area = circle.area(36)
round_room_area = circle.area(11460)