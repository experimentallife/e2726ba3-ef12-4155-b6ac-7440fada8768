import datetime

from injector import inject

from connexion import NoContent
from flask import request
from flask.views import MethodView

from services import ProductService

@inject
def get(id, product_service: ProductService):
    product_service.print()
    return NoContent

# class ProductControllerView(MethodView):
#     @inject
#     def __init__(self, product_service: ProductService):
#         self.__product_service = product_service

#     def get(self, id):
#         self.__product_service.print()
#         return NoContent

#     # @inject
#     # def get():
#     #     return { a: 'bbb' }

#     def find(self, dto):
#         pass

#     def find_one(self, query):
#         pass

#     def find_many(self, query):
#         pass

#     def create(self, dto):
#         pass

#     def update(self, dto):
#         pass

#     def delete(self, id):
#         pass