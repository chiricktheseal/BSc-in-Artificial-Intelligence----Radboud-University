class Field: # представляет одну ячейку судоку и содержит информацию о значении ячейки, допустимых значениях (домене) и соседних ячейках, с которыми она связана
    # region constructors

    def __init__(self, *args):

        self.value = 0 # сначала знач ячейки = 0,=  ячейка пустая.
        self.domain = [] #  пустой список, будет содержать допустимые значения для этой ячейки
        # A list of all the fields that this field is constrained by
        self.neighbours = [] # пустой список для хранения соседей ячейки(других ячеек, связанных с ней по правилам судоку)

        # Constructor in case the field is unknown
        if len(args) == 0: # не передан аргумент = знач ячейки не известно
            for i in range(1, 10):  # 1 до 9 ддопустимы
                self.domain.append(i)

        # Constructor in case the field is known, i.e., it contains a value
        if len(args) == 1: # передан один аргумент
            self.value = args[0]  # это аргумент = знач яч
            self.domain = [] #домэйн пустой, знач уже известно , других вариков нема

    # endregion

    # region value functions

    def is_finalized(self): #проверка есть ли знач в яч
        """
        Has this field been set to a non-zero value? If so then it is finalized.
        :return: Boolean indicating if the field is finalized.
        """
        return self.value != 0 #тру -если вал не равно 0 (пустая яч= вал=0)

    def get_value(self): #возвращает текущ знач яч
        return self.value

    def set_value(self, value): #установить новое знач яч (назначение определенного числа в ячейку)
        self.value = value

    # endregion

    # region neighbor functions

    def set_neighbours(self, neighbours): # список соседей данной яч
        self.neighbours = neighbours

    def get_neighbours(self): #возвращает список соседей данной яч
        return self.neighbours

    def get_other_neighbours(self, b): #возвр список всех соседей, кроме указанного соседа б
        """
        Return all neighbours of this field except neighbour b
        @param b:
        @return: All neighbors of this Field except b
        """
        new_neighbours = self.neighbours.copy() #копия, чтоб исходный не менялся
        new_neighbours.remove(b) # из копии удаляется яч б, резулт возврат
        return new_neighbours

    # endregion

    # region domain functions

    def get_domain(self): #возвр список возможн знач (домен) для данной яч
        return self.domain

    def get_domain_size(self):
        return len(self.domain)

    def remove_from_domain(self, value): #удаляет знач вал из домена ячейки
        """
        Removes the given value from the domain, and possibly assigns the last value to the field
        :param value: value to remove
        :return: true if the value was removed
        """
        value_removed = self.domain.remove(value) # пытается удалить вал из селф.домен
        if len(self.domain) == 1: #если в домене 1 знач, оно будет вал ячейки (единственное возможн решений для яч)
            self.set_value(self.domain[0])
        return value_removed #было ли удаление успешным

    # endregion

    # region Misc Functions

    def __str__(self):
        """
        Displays non-finalized fields with a period, otherwise displays the finalized value
        :return:
        """
        return "." if self.value == 0 else str(self.value) # если вал=0, то .=яч пустая, иначе строка=числов знач в яч

    # endregion
