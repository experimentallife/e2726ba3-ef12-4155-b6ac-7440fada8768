from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

# from services import ProductService
from repositories import ProductRepository

class Container(containers.DeclarativeContainer):
    
    config = providers.Configuration()

    product_repository = providers.Singleton()

    product_service = providers.Factory(
        ProductRepository
    )
