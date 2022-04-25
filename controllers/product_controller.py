import datetime

from dependency_injector.providers import Factory
# from dependency_injector.wiring import inject, Provide
import dependency_injector.injections as injections

from connexion import NoContent
from flask import request
from flask.views import MethodView

from ioc.container import Container
from services.product_service import ProductService

@injections.inject(product_service=Container.product_service)
def get(id, product_service: ProductService):
    product_service.get()
    return NoContent

# @inject
# def get():
#     return { a: 'bbb' }

@inject
def find(dto):
    pass

@inject
def find_one(query):
    pass

@inject
def find_many(query):
    pass

@inject
def create(dto):
    pass
@inject
def update(dto):
    pass

@inject
def delete(id):
    pass