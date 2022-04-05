from dependency_injector import containers, providers
from src.config.database import DB

from src.infra.containers import (
    RepositoryContainer,
    UserServiceContainer,
    QrcodeServiceContainer,
    WhatsappServiceContainer
)
from src.shared.services.instance import Instance
#     CommerceContainer,
#     PosContainer,
#     PlatformCatalogContainer,
#     WhiteLabelCatalogContainer,
#     ProjectCatalogContainer,
#     ProjectContainer,
#     EndClientCatalogContainer
# )

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()
    db = providers.Singleton(DB)
    instance = providers.Singleton(Instance)
    repository_container = providers.Container(RepositoryContainer,db=db)
    user_service_container = providers.Container(UserServiceContainer,repository=repository_container.repository, instance=instance)
    qrcode_service_container = providers.Container(QrcodeServiceContainer, instance=instance)
    whatsapp_service_container = providers.Container(WhatsappServiceContainer, qrcode_service=qrcode_service_container.qrcode_service, instance=instance)
    
    
    # order_container = providers.Container(OrderContainer,db=db,user_service=user_service_container.service)
    # scrap_container = providers.Container(ScrapContainer,instance=instance,order_service=order_container.order_service)

    # banking_container = providers.Container(BankingContainer)
    # platform_catalog_container = providers.Container(PlatformCatalogContainer)
    # white_label_catalog_container = providers.Container(WhiteLabelCatalogContainer)
    # project_catalog_container = providers.Container(ProjectCatalogContainer)
    # project_container = providers.Container(ProjectContainer)
    # commerce_container = providers.Container(CommerceContainer)
    # pos_container = providers.Container(PosContainer)
    # end_client_catalog_container = providers.Container(EndClientCatalogContainer)


def init_app() -> Container:
    return Container()
