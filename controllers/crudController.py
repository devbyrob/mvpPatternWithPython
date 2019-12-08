from views.crudView import CRUDVIEW
from models.crudModel import CRUB


class CRUDCONTROLLER:

    def __init__(self):
        self.__model = CRUB()
        self.__view = CRUDVIEW(self)

    def create_registry(self, name, price):
        self.__model.reg_product(name, price)

    def find_registry(self, code):
        product_found = self.__model.search_product(code)
        return product_found

    def update_registry(self, code, name, price):
        self.__model.update_product(code, name, price)

    def delete_registry(self, code):
        self.__model.delete_product(code)
