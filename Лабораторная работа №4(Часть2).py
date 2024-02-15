if __name__ == "__main__":
    class Car:
        """ Базовый класс машины.

        :param brand: Марка машины - непубличный атрибут
        :param speed: Скорость машины - непубличный атрибут
        :param price: Стоимость машины - непубличный атрибут
        Причина инкапсуляции - возможное переименования,
        для сохранности кода других пользователей
        """

        FIRST_SPEED = 150  # Постоянная переменная класса - первая скорость
        SECOND_SPEED = 60  # Постоянная переменная класса - вторая скорость
        THIRD_SPEED = 40  # Постоянная переменная класса - третья скорость

        def __init__(self, brand: str, speed: int, price: int):
            self._brand = brand
            self._speed = speed
            self._price = price

        def __str__(self) -> str:
            return f"Машина {self.brand!r}, стоимостью {self.price}, максимальная скорость {self.speed}"

        def __repr__(self) -> str:
            return f"{self.__class__.__name__}(brand={self.brand!r}, speed={self.speed}, price={self.price})"

        @property
        def brand(self):
            return self._brand

        @brand.setter
        def brand(self, new_brand):
            if not isinstance(new_brand, str):
                raise TypeError("Марка должна быть типа str")
            self._brand = new_brand

        @property
        def speed(self):
            return self._speed

        @speed.setter
        def speed(self, new_speed):
            if not isinstance(new_speed, int):
                raise TypeError("Скорость машины должна быть типа int")
            if new_speed <= 0:
                raise ValueError("Скорость машины должна быть положительным числом")
            self._speed = new_speed

        @property
        def price(self):
            return self._price

        @price.setter
        def price(self, new_price):
            if not isinstance(new_price, int):
                raise TypeError("Стоимость машины должна быть типа int")
            if new_price <= 0:
                raise ValueError("Стоимость машины должна быть положительным числом")
            self._price = new_price

        def cost_increasing(self, inflation: float) -> float:
            """
            Метод, который считает стоимость машины с учетом инфляции

            :param inflation: Значение инфляции в процентах

            :return: Актуальная стоимость машины
            """
            return self._price * (1 + inflation)

        def optimal_speed(self, high_speed_car: bool) -> int:
            """
            Метод, который высчитывает оптимальную скорость движения машины

            :param high_speed_car: Является ли машина скоростной или нет

            :return: Оптимальная скорость движения машины
            """
            if high_speed_car and self._speed > self.FIRST_SPEED:
                return self.FIRST_SPEED
            return self.SECOND_SPEED

    class PassengerCar(Car):
        """ Дочерний класс машины.

        :param brand: Марка машины - непубличный атрибут
        :param speed: Скорость машины - непубличный атрибут
        :param price: Стоимость машины - непубличный атрибут
        :param passengers_number: Количество пассажиров - публичный атрибут
        Причина инкапсуляции - возможное переименования,
        для сохранности кода других пользователей
        """
        def __init__(self, brand: str, speed: int, price: int, passengers_number: int):
            super().__init__(brand, speed, price)
            self.passengers_number = passengers_number

        def __str__(self) -> str:
            return f"Легковая машина {self.brand!r}, стоимостью {self.price}, максимальная скорость {self.speed}"

        @property
        def passengers_number(self):
            return self._passengers_number

        @passengers_number.setter
        def passengers_number(self, new_passengers_number):
            if not isinstance(new_passengers_number, int):
                raise TypeError("Количество пассажиров должно быть типа int")
            if new_passengers_number <= 0:
                raise ValueError("Количество пассажиров должно быть положительным числом")
            self._passengers_number = new_passengers_number

        def optimal_speed(self, high_speed_car: bool) -> int:
            """
            Метод, который высчитывает оптимальную скорость движения машины.
            Причина перезагрузки метода - влияния аргументов дочернего класса на итоговый результат.
            Оптимальная скорость для легковой машины будет зависеть от количества пассажиров.

            :param high_speed_car: Является ли машина скоростной или нет

            :return: Оптимальная скорость движения машины
            """
            if self.passengers_number > 4:
                return self.THIRD_SPEED
            elif self.passengers_number > 1:
                return self.SECOND_SPEED
            elif high_speed_car and self._speed > self.FIRST_SPEED:
                return self.FIRST_SPEED
            return self.SECOND_SPEED

    class Truck(Car):
        """ Дочерний класс машины.

        :param brand: Марка машины - непубличный атрибут
        :param speed: Скорость машины - непубличный атрибут
        :param price: Стоимость машины - непубличный атрибут
        :param basket_capacity: Вместимость кузова - публичный атрибут
        Причина инкапсуляции - возможное переименования,
        для сохранности кода других пользователей
        """
        def __init__(self, brand: str, speed: int, price: int, basket_capacity: int):
            super().__init__(brand, speed, price)
            self.basket_capacity = basket_capacity

        def __str__(self) -> str:
            return f"Грузовая машина {self.brand!r}, стоимостью {self.price}, максимальная скорость {self.speed}"

        @property
        def basket_capacity(self):
            return self._basket_capacity

        @basket_capacity.setter
        def basket_capacity(self, new_basket_capacity):
            if not isinstance(new_basket_capacity, int):
                raise TypeError("Вместимость кузова должна быть типа int")
            if new_basket_capacity <= 0:
                raise ValueError("Вместимость кузова должна быть положительным числом")
            self._basket_capacity = new_basket_capacity

        def optimal_speed(self, high_speed_car: bool) -> int:
            """
            Метод, который высчитывает оптимальную скорость движения машины.
            Причина перезагрузки метода - влияния аргументов дочернего класса на итоговый результат.
            Оптимальная скорость для грузовой машины будет зависеть от вместимости кузова.

            :param high_speed_car: Является ли машина скоростной или нет

            :return: Оптимальная скорость движения машины
            """
            if self.basket_capacity > 100:
                return self.THIRD_SPEED
            elif self.basket_capacity > 50:
                return self.SECOND_SPEED
            return self.FIRST_SPEED

    pass
