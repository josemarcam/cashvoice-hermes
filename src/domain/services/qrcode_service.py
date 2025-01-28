from injector import inject
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from src.domain.models.qrcode_model import QrcodeKafkaModel
from src.shared.services.instance import Instance
from src.shared.services.lib.kafka.kafka_models import KafkaHeader, KafkaModel
from src.shared.services.lib.kafka.kafka_service import CoreKafka

from src.config import environment

class QrcodeService:
    
    @inject
    def __init__(self, instance: Instance):
        self.instance = instance

    def get_qrcode(self):
        browser = self.instance.get_driver

        found = False
        val = None
        while(found != True):
            try:
                WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.CLASS_NAME, environment.get_item("QRCODE_WP_ELEMENT"))))
                element = browser.find_element(By.CLASS_NAME, environment.get_item("QRCODE_WP_ELEMENT"))
                val = element.get_attribute("data-ref")

                self.qrcode = val
                if(self.qrcode == None):
                    return self.get_qrcode()
                
                found = True
            except KeyboardInterrupt:
                quit()
            except Exception as e:
                print("Falha no erro: (qr)\n\n")
                print(e)
                found = False
        
        return found, self.qrcode
    
    def send_kafka_qrcode(self, qrcode:str, user_id: int):
        
        print("Enviando qrcode para kafka")
        core_kafka = CoreKafka()
        qrcode_kafka_model = QrcodeKafkaModel(user_id = user_id,qrcode = qrcode)
        kafka_header = KafkaHeader(id = "1", label_code = "32", application = "alguma", type = "sei la")
        kafka_model = KafkaModel(header = kafka_header,payload=qrcode_kafka_model.dict())
        core_kafka.publish(environment.get_item("KAFKA_TOPIC_CLIENT_QRCODE"),kafka_model)
