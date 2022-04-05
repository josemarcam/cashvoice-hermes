from dependency_injector import containers, providers
from src.domain.repositories.user_repository import UserRepository
class RepositoryContainer(containers.DeclarativeContainer):
    
    db = providers.Dependency()

    repository = providers.Factory(
        UserRepository,
        db=db
    )
