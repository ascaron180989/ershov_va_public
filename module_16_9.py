########################################################################################################################
#                                                16.9.1                                                                #
########################################################################################################################


# class Figures:
#     def __init__(self, type: str, x: int, y: int, width: int = 0, height: int = 0, rad: int = 0):
#         self.type = type
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.rad = rad
#
#     def get_figure(self):
#         if self.type == 'rectangle':
#             return f'Прямоугольник: x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height}'
#         if self.type == 'square':
#             self.height = self.width
#             return f'Квадрат: x = {self.x}, y = {self.y}, width = {self.width}, height = {self.height}'
#         if self.type == 'circle':
#             return f'Круг: x = {self.x}, y = {self.y}, rad = {self.rad}'
#
#
# rec = Figures('rectangle', 1, 1, width=5, height=10)
# print(rec.get_figure())
#
# squ = Figures('square', 2, 2, width=15)
# print((squ.get_figure()))
#
# cir = Figures('circle', 3, 3, rad=20)
# print(cir.get_figure())


########################################################################################################################
#                                                16.9.2                                                                #
########################################################################################################################


# class Rectangle:
#     def __init__(self, w: int = 0, h: int = 0):
#         self.width = w
#         self.height = h
#
#     def get_area(self):
#         S = self.width * self.height
#         return S
#
#
# width = int(input('Введите ширину прямоугольника: '))
# height = int(input('Введите высоту прямоугольника: '))
#
# rec = Rectangle(width, height)
#
# print(f'Прямоугольник: w =  {rec.width}, h = {rec.height}, S = {rec.get_area()}')


########################################################################################################################
#                                                16.9.3                                                                #
########################################################################################################################


# class Clients:
#     def __init__(self, name: str = '', credits: int = 0):
#         self.name = name
#         self.credits = credits
#
#     def __add__(self, client_dict: dict):
#         self.name = client_dict.get('name')
#         self.credits = client_dict.get('credits')
#
#
# clients = [{'name': 'Anna', 'credits': 50}, {'name': 'John', 'credits': 20}, {'name': 'Mark', 'credits': 100}]
#
# for c in clients:
#     client = Clients()
#     client.__add__(c)
#     print(f'Клиент "{client.name}". Баланс: {client.credits} руб')


########################################################################################################################
#                                                16.9.4                                                                #
########################################################################################################################


# class People:
#     def __init__(self, name: str = None, city: str = None):
#         self.name = name
#         self.city = city
# 
# 
# class Role(People):
#     def __init__(self, role: str, name: str, city: str):
#         super(Role, self).__init__(name, city)
#         self.role = role
# 
#     def get_info(self):
#         return print(f'"{self.name}, city: {self.city}, status: {self.role}"')
# 
# 
# anna = Role('Mentor', 'Anna Smith', 'New York')
# 
# anna.get_info()
