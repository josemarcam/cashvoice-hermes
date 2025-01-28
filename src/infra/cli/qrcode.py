import typer
from src.config.containers import Container
from src.domain.services.qrcode_service import QrcodeService
from src.domain.services.user_service import UserService
from src.domain.models.user_model import CreateUserModel
from src.domain.services.whatsapp_service import WhatsAppService
from src.shared.services.lib.kafka.kafka_service import CoreKafka

app = typer.Typer()

container = Container()

@app.command()
def main():
    service : UserService  = container.user_service_container.user_service()
    create_user_model = CreateUserModel(name="teste",mac="123qw23e2",email="kkj@q23we.com2",key="kk23j2",teste="não é te23st2e",validity="vali23d1ity legla")
    user_model = service.create(user_model=create_user_model)
    # user_model = service.get_user(user_id=1)
    print(user_model)

@app.command()
def wp_login():
    
    # kafka_service = CoreKafka()
    # consumer = kafka_service.consumer(kafka_service.get_client_topic(), mode='latest')
    # consumer.subscribe(kafka_service.get_client_topic())
    # typer.echo(f'Kafka topic {kafka_service.get_client_topic()}')
    # for msg in consumer:
    #     data = msg.value['payload']

    service : UserService  = container.user_service_container.user_service()
    whatsapp_service : WhatsAppService = container.whatsapp_service_container.whatsapp_service()
    qrcode_service : QrcodeService = container.qrcode_service_container.qrcode_service()
    
    logged = whatsapp_service.make_login()
    if logged:
        print("logou!!!!!!")
                
        # json_qrcode = {"qrcode":qrcode}

        # print(f"O qr code -> {qrcode}")
        # webhook_url = "https://webhook.site/c5b4a5e0-ea11-41b9-b9a4-9fada3e69073"
        # service.send_web_hook(webhook_url,json_qrcode)
# @app.command()
# def scrap_orders():
#     service : ScrapService  = container.scrap_container.scrap_service()
#     service.get_orders()
#     service.kill_instance()

# @app.command()
# def get_stores_cacau_show():
#     service : ScrapService  = container.scrap_container.scrap_service()
#     service.get_cs_stores()
