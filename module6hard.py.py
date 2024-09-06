class Figure:
    sides_count = 0
    def __init__(self, __color, filled=False, *__sides):

        self.color = __color
        self.filled = filled
        self.sides = []
        if self.is_valid_sides(*__sides):
            for i in range(0, self.sides_count):
                self.sides.append(__sides[i])
        elif len(__sides) == 1:
            for i in range(0, self.sides_count):
                self.sides.append(*__sides)
        elif len(__sides) == self.sides_count:
            for i in range(0, self.sides_count):
                self.sides.append(1)
        elif len(__sides) != self.sides_count:
            for i in range(0, self.sides_count):
                self.sides.append(1)

    def get_color(self):
        return self.color

    def is_valid_color(self, color):
        if isinstance(color, tuple) and len(color) == 3:
            for i in color:
                if isinstance(i, int) and i < 0 or i > 255:
                    return False
                return True
        else:
            return False

    def set_color(self, *color):
        if self.is_valid_color(color):
            self.color = color

    def is_valid_sides(self, *args):
        if len(args) == self.sides_count and self.is_valid_figure(*args):
            for i in args:
                if isinstance(i, int) and i < 0:
                    return False
                return True
        else:
            return False
    def is_valid_figure(self, *args):
        if len(args) == 3:
            max_side = max(args)
            if args.count(max_side) == 1:
                sum_min_side = 0
                for i in args:
                    if max_side != i:
                        sum_min_side += args[i]
                if max_side > sum_min_side:
                    return False
            else:
               return True
        else:
           return True
    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.is_valid_sides(*new_sides) and self.is_valid_figure(*new_sides):
            if len(new_sides) == 1:
                self.sides[0] = new_sides[0]
            else:
                self.sides = new_sides
    def get_sides(self):
        return self.sides

    def __len__(self):
        sum_sides = 0
        if self.sides_count == 1:
            return self.sides[0]
        else:
            for i in range(0, self.sides_count):
                sum_sides += self.sides[i]
            return sum_sides

    def __str__(self):
        return f'Цвет: {self.color}, Стороны: {self.sides}'

class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides, filled=False):
        super().__init__(color,  filled, *sides)

    def get_square(self):
        import math
        self.radius = self.sides[0] / (2 * math.pi)
        return 2 * math.pi * self.radius * self.radius


class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides, filled=False):
        super().__init__(color, filled, *sides)

    def get_square(self):
        p = len(self) / 2
        return (p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2])) ** 0.5
    def get_angl(self):
        import math
        side_a = self.sides[0]
        side_b = self.sides[1]
        side_c = self.sides[2]
        a = int(math.acos((side_b ** 2 + side_c ** 2 - side_a ** 2) / (2 * side_b * side_c)) * 180 / math.pi)
        b = int(math.acos((side_a ** 2 + side_c ** 2 - side_b ** 2) / (2 * side_a * side_c)) * 180 / math.pi)
        c = 180 - a - b
        return f'Угол альфа -  {a} угол бетта - {b} угол гамма - {c}'

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, sides, filled=False):
        super().__init__(color, filled, sides)

    def get_volume(self):
        return self.sides[0] ** 3
    def get_square(self):
        return 6 * self.sides[0] ** 2

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

