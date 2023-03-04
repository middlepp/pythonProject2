# numbers = [1, 2, 3, 4, 5, 6, 7]
# count_odd = []
# count_even = []
# for x in numbers:
#     if x / 2 == 0:
#         count_even.append(x)
#     else:
#         count_odd.append(x)
# print('number of even numbers :', count_even)
# print('number of odd numbers:', count_odd)

# dict1 = {1:'zippo', 4:'magnolia', 2:'meh', 5:'meme'}
# new_dict = sorted(dict1, key=lambda k: int(k))
# new_dict1 = sorted(dict1.items(), key=lambda kv_pair:[0])
# new_dict2 = sorted(dict1.items(), key=lambda kv_pair:[2])
# print(new_dict)
# print(new_dict1)
# print(new_dict2)

#
# b_dictionary = {'c': 2, 'n': 2, 28:17}
# print(b_dictionary)
# reversed_dictionary = {}
# for j, i in b_dictionary.items():
#     reversed_dictionary[i] = j
# print(reversed_dictionary)


# a_dictionary = {2:'ca', 'ca': 2, 28:17}
# looking_for = 'ca'
# for k, v in a_dictionary.items():
#     if v == looking_for:
#         print(k)


#functions
# def number_of_digits_in_list():
#     l = [4, 10, 25, 44, 54]
#     return len(l)
#
# n = number_of_digits_in_list()
# print(n)
#
# def n_in_use_after_return(x):
#     print(x + 5)
#
# n_in_use_after_return(n)

# def number_of_digits_in_the_insert(value):
#     return len(str(value))
#
# print(number_of_digits_in_the_insert(62545))


# def digits(value):
#     result = 0
#     while value >= 1:
#         result += 1
#         value = value / 10
#     return result
# print(digits(516251651))

class Car:
    wheels = 4

    def __init__(self, brand, color):
        self.color = color
        self.brand = brand

    def print_car_color(self):
        print(self.color)

    def print_car_brand(self):
        print(self.brand)

    def print_wheels(self):
        print(Car.wheels)

    def print_all(self):
        print(f'{self.color} {self.brand} has{Car.wheels} wheels')

    @staticmethod
    def print_cls_wheels():
        print(Car.wheels)
Car.print_cls_wheels()


my_car = Car('jeep', 'white')
your_car = Car('toyota', 'brown')

my_car.print_car_color()
my_car.print_car_brand()
my_car.print_wheels()
my_car.print_all()

your_car.print_car_color()
your_car.print_car_brand()
your_car.print_wheels()
your_car.print_all()

