# bastract_classes

from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport):
    def start_engine(self):
        print("Катер громко затарохтел")

    def stop_engine(self):
        print("Двигатель катера чихнул и заглох")

    def move(self):
        print("Катер быстро набирает скорость")

    def stop(self):
        print("Катер остановился")


class Car(Transport):
    def start_engine(self):
        print("Машина заурчала двигателем")

    def stop_engine(self):
        print("Машина стоит с заглушенным двигателем")

    def move(self):
        print("Машина едет к цели назначения")

    def stop(self):
        print("Машина остановилась")


class Electroscooter(Transport):
    def start_engine(self):
        print("Мигнул светодиодом")

    def stop_engine(self):
        print("Мигнул светодиодом дважды")

    def move(self):
        print("Прохожие в ужасе разбегаются от очередного камикадзе")

    def stop(self):
        print("Торможение об стену прошло успешно")


class Person:
    def use_transport(self, transport: Transport):
        transport.stop_engine()
        transport.start_engine()
        transport.move()
        transport.stop()


if __name__ == "__main__":
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print("=" * 10)
    person.use_transport(car)
    print("=" * 10)
    person.use_transport(kamikadze)


# bad_smell_big_class


class Warrior:
    def attack(self):
        pass

    def move(self):
        pass

    def defense(self):
        pass


class Healer:
    def healer_defense(self):
        pass

    def healer_move(self):
        pass

    def heal(self):
        pass


class Tree:
    def tree_defense(self):
        pass

    def on_fire(self):
        pass


class Trap:
    def trap_attack(self):
        print("It's a trap!")


if __name__ == "__main__":
    unit = Warrior()
    healer = Healer()
    trap = Trap()


# bad_smell_call_chain


class Room:
    def get_name(self):
        return 42


class Street:
    def get_room(self) -> Room:
        return Room()


class City:
    def get_street(self) -> Street:
        return Street()

    def population(self):
        return 100500


class Country:
    def get_city(self) -> City:
        return City()


class Planet:
    def get_contry(self) -> Country:
        return Country()


class Person:
    def __init__(self, city_population, room_num):
        self.city_population = city_population
        self.room_num = room_num

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.city_population


# bad_smell_comment


class Unit:
    def move(self, field, x_coord, y_coord, direction, fly, crawl, speed=1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита,
        направление его движения, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с
        которым двигается юнит
        :param field: поле по которому перемещается юнит
        :param x_coord: x-координата юнита
        :param y_coord: у- координата юнита
        :param direction: направление перемещения
        :param fly: летит ли юнит
        :param crawl: крадется ли юнит
        :param speed: базовый параметр скорости
        """
        if fly and crawl:
            raise ValueError("Рожденный ползать летать не должен!")

        if fly:
            speed *= 1.2
            if direction == "UP":
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == "DOWN":
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == "LEFT":
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == "RIGHT":
                new_y = y_coord
                new_x = x_coord + speed
        if crawl:
            speed *= 0.5
            if direction == "UP":
                new_y = y_coord + speed
                new_x = x_coord
            elif direction == "DOWN":
                new_y = y_coord - speed
                new_x = x_coord
            elif direction == "LEFT":
                new_y = y_coord
                new_x = x_coord - speed
            elif direction == "RIGHT":
                new_y = y_coord
                new_x = x_coord + speed

            field.set_unit(x=new_x, y=new_y, unit=self)


# bad_smell_dead_code


class Unit:
    def __init__(self):
        self.x = 0
        self.y = 0

    def attack(self):
        pass

    def defense(self):
        pass

    def move(self, field):
        field.set_unit(x=self.x, y=self.y, unit=self)


class Field:
    def set_unit(self, x, y, unit: Unit):
        pass


class Main:
    def __init__(self):
        self.field = Field()
        self.unit = Unit()
        self.unit.move(field=self.field)


if __name__ == "__main__":
    main = Main()

# bad_smell_doubles


class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def asc_sorting(self):
        return sorted(self.lst, reverse=False)


# bad_smell_envious_func


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return self.x * self.y * self.z


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.get_volume()


# bad_smell_lazy_class


class Unit:
    def __init__(self):
        self.x = 0
        self.y = 0

    def attack(self):
        pass

    def defense(self):
        pass

    def move(self, field_adapter):
        field_adapter.set_unit(x=self.x, y=self.y, unit=self)


class Field:
    def set_unit(self, x, y, unit: Unit):
        pass


class Main:
    def __init__(self):
        self.field = Field()
        self.unit = Unit()
        self.unit.move(self.field)


# bad_smell_long_method

csv = """Вася;39\nПетя;26\nВасилий Петрович;9"""


def get_users_list() -> list:
    data = _read(csv)
    sorted_data = _sort(data)
    filtered_data = _filter(sorted_data)
    return filtered_data


def _read(csv) -> list:
    return [x.split(";") for x in csv.split("\n")]


def _sort(data):
    return sorted(data, key=lambda x: int(x[1]))


def _filter(sorted_data):
    return [x for x in sorted_data if int(x[1]) > 10]


if __name__ == "__main__":
    print(get_users_list())

# bad_smell_long_parametr_list


class Unit:
    def __init__(self):
        pass

    def move(self, direction):
        speed = self._get_speed()

        if direction == "UP":
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == "DOWN":
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == "LEFT":
            self.field.set_union(y=self.y, x=self - speed, unit=self)
        elif direction == "RIGHT":
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        if self.state == "fly":
            return self.speed * 1.2
        elif self.state * 0.5:
            return self.speed * 0.5
        else:
            raise ValueError("Эк тебя раскорячило")
