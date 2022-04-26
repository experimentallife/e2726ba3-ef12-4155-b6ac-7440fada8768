from injector import singleton

from repositories import ProductRepository
from services import ProductService
# from controllers import ProductView

def configure(binder):
    binder.bind(ProductRepository, to=ProductRepository, scope=singleton)
    binder.bind(ProductService, to=ProductService, scope=singleton)
    # binder.bind(ProductView, to=ProductView, scope=singleton)