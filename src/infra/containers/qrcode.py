from dependency_injector import containers, providers
from src.domain.services.qrcode_service import QrcodeService

class QrcodeServiceContainer(containers.DeclarativeContainer):
    
    instance = providers.Dependency()
    qrcode_service = providers.Factory(QrcodeService, instance=instance)


