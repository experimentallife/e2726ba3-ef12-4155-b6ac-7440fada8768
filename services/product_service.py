
from injector import inject

from repositories import ProductRepository
class ProductService:
    @inject
    def __init__(self, product_respository: ProductRepository):
        self.__product_respository = product_respository

    def print(self):
        self.__product_respository.print()