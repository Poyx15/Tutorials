# def greet_user():
#     print('Hi there!')
#     print('Welcome aboard')
#
#
# print("Start")
# greet_user()
# print("Finish")


def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')


greet_user(last_name="Jamoralin", first_name="Emmanuel")    # Keyword arguments
greet_user("Emmanuel", "Jamoralin")                         # Positional arguments
