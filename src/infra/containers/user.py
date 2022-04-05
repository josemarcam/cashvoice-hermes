from dependency_injector import containers, providers
from src.domain.services.user_service import UserService

class UserServiceContainer(containers.DeclarativeContainer):
    
    repository = providers.Dependency()
    instance = providers.Dependency()
    user_service = providers.Factory(UserService, repository=repository, instance=instance)
