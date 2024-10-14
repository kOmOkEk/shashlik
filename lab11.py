def f1():
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print('Имя ресторана: ', self.restaurant_name)
            print('Тип кухни: ', self.cuisine_type)

        def open_restaurant(self):
            print('Ресторан открыт')

    newRestaurant = Restaurant('ДакМак', 'Фаст-фуд')
    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

def f2():
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print('Имя ресторана: ', self.restaurant_name)
            print('Тип кухни: ', self.cuisine_type)

        def open_restaurant(self):
            print('Ресторан открыт')

    restaurant1 = Restaurant('ПепеКарня', "Выпечка")
    restaurant2 = Restaurant("Куассо", "Французская")
    restaurant3 = Restaurant('ДакМак', "ФастФуд")

    restaurant1.describe_restaurant()
    print('\n')
    restaurant2.describe_restaurant()
    print('\n')
    restaurant3.describe_restaurant()

def f3():
    class Restaurant():
        def __init__(self, restaurant_name, cuisine_type, rating):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.rating = rating

        def describe_restaurant(self):
            print('Имя ресторана: ', self.restaurant_name)
            print('Тип кухни: ', self.cuisine_type)
            print('Рейтинг ', self.rating)

        def open_restaurant(self):
            print('Ресторан открыт')

        def rating(self,new_rating):
            self.rating = new_rating

    restaurant1 = Restaurant('ПепеКарня', "Выпечка", 4.7)
    restaurant2 = Restaurant("Куассо", "Французская", 5)
    restaurant3 = Restaurant('ДакМак', "ФастФуд", 3.9)

    restaurant1.describe_restaurant()
    print('\n')
    restaurant2.describe_restaurant()
    print('\n')
    restaurant3.describe_restaurant()
    print('\n')
