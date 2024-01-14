import doctest


class Plant:
    def __init__(self, number_of_workers: int, number_of_production: int):
        """
        Создание и подготовка к работе объекта "Завод"

        :param number_of_workers: Количество рабочих
        :param number_of_production: Количество продукции

        Примеры:
        >>> plant = Plant(45, 5000)  # инициализация экземпляра класса
        """
        if not isinstance(number_of_workers, int):
            raise TypeError("Количество рабочих должно быть целым числом")
        if number_of_workers <= 0:
            raise ValueError("Количество рабочих должно быть больше нуля")
        self.number_of_workers = number_of_workers

        if not isinstance(number_of_production, int):
            raise TypeError("Количество продукции должно быть целым числом")
        if number_of_production <= 0:
            raise ValueError("Количество продукции должно быть больше нуля")
        self.number_of_production = number_of_production

    def increase_number_of_workers(self, additional_workers: int) -> None:
        """
        Добавление количества рабочих.
        :param additional_workers: Количество новых рабочих

        :raise TypeError: Если количество рабочих не является целым, то вызываем ошибку
        :raise ValueError: Если количество рабочих не является числом больше нуля, то вызываем ошибку

        Примеры:
        >>> plant = Plant(45, 5000)
        >>> plant.increase_number_of_workers(23)
        """
        if not isinstance(additional_workers, int):
            raise TypeError("Добавленное количество рабочих должно быть типа int")
        if additional_workers <= 0:
            raise ValueError("Добавленное количество рабочих должно быть больше нуля")
        ...

    def production_rate(self) -> float:
        """
        Подсчет нормы производства. Сколько продукции приходится на одного рабочего.

        :return: Норма производства завода

        Примеры:
        >>> plant = Plant(200, 10000)
        >>> plant.production_rate()
        """
        ...


class Weight:
    def __init__(self, normal_weight: float, actual_weight: float):
        """
        Создание и подготовка к работе объекта "Вес"

        :param normal_weight: Норма веса
        :param actual_weight: Текущий вес

        Примеры:
        >>> weight = Weight(75.6, 80.4)  # инициализация экземпляра класса
        """
        if not isinstance(normal_weight, float):
            raise TypeError("Норма веса должна быть числом с плавающей запятой")
        if normal_weight <= 0:
            raise ValueError("Норма веса должна быть больше нуля")
        self.normal_weight = normal_weight

        if not isinstance(actual_weight, float):
            raise TypeError("Текущий вес должен быть числом с плавающей запятой")
        if actual_weight <= 0:
            raise ValueError("Текущий вес должен быть больше нуля")
        self.actual_weight = actual_weight

    def weight_checking(self) -> bool:
        """
        Проверяет превышает ли текущий вес норму.

        :return: Является ли вес в норме

        Примеры:
        >>> weight = Weight(75.6, 80.4)
        >>> weight.weight_checking()
        """
        ...

    def body_mass_index(self, height: int) -> float:
        """
        Подсчет индекса массы тела.
        :param height: Рост

        :raise TypeError: Если рост не является целым, то вызываем ошибку
        :raise ValueError: Если рост не является числом больше нуля, то вызываем ошибку

        :return: Индекс массы тела

        Примеры:
        >>> weight = Weight(75.6, 80.4)
        >>> weight.body_mass_index(189)
        """
        if not isinstance(height, int):
            raise TypeError("Рост должен быть типа int")
        if height <= 0:
            raise ValueError("Рост должен быть больше нуля")
        ...


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass


class Temperature:
    def __init__(self, night_temperature: float, day_temperature: float):
        """
        Создание и подготовка к работе объекта "Температура"

        :param night_temperature: Ночная температура
        :param day_temperature: Дневная температура

        Примеры:
        >>> temperature = Temperature(-1.2, 12.5)  # инициализация экземпляра класса
        """
        if not isinstance(night_temperature, float):
            raise TypeError("Ночная температура должна быть числом с плавающей запятой")
        self.night_temperature = night_temperature

        if not isinstance(day_temperature, float):
            raise TypeError("Дневная температура должна быть числом с плавающей запятой")
        self.day_temperature = day_temperature

    def average_temperature(self) -> float:
        """
        Высчитывает среднюю температуру в сутках.

        :return: Средняя температура

        Примеры:
        >>> temperature = Temperature(-1.2, 12.5)
        >>> temperature.average_temperature()
        """
        ...

    def will_puddles_be_frozen(self) -> bool:
        """
        Проверяет замерзнут ли лужи.

        :return: Замерзнут ли лужи

        Примеры:
        >>> temperature = Temperature(-1.2, 12.5)
        >>> temperature.will_puddles_be_frozen()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass