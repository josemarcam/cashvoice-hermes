from dependency_injector import containers, providers
from src.domain.services.whatsapp_service import WhatsAppService

class WhatsappServiceContainer(containers.DeclarativeContainer):
    
    instance = providers.Dependency()
    qrcode_service = providers.Dependency()
    whatsapp_service = providers.Factory(WhatsAppService, qrcode_service=qrcode_service, instance=instance)


