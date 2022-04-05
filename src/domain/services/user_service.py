import requests
import json
from src.config import environment
from src.domain.models.qrcode_model import CreateQrcodeModel

from src.domain.models.user_model import CreateUserModel, UserModel
from src.domain.repositories import UserRepository
from src.shared.services.instance import Instance

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class UserService:
    
    def __init__(self, instance: Instance, repository: UserRepository):
        self.repository = repository
        self.instance = instance

    def get_qrcode(self):
        browser = self.instance.get_driver
        browser.get("https://web.whatsapp.com/send/?phone=996061956")
        return self._get_qrcode()
    
    def create_qrcode(self, create_qrcode_model: CreateQrcodeModel):
        return self.repository.create_qrcode(create_qrcode_model)
    
    def send_web_hook(self, url, data):
        requests.post(url = url, data = json.dumps(data))
        self.instance.kill
    
    def _get_qrcode(self):

        browser = self.instance.get_driver
        found = False
        val = None
        while(found != True):
            try:
                WebDriverWait(browser, 120).until(EC.presence_of_element_located((By.CLASS_NAME, environment.get_item("QRCODE_WP_ELEMENT"))))
                element = browser.find_element_by_class_name(environment.get_item("QRCODE_WP_ELEMENT"))
                val = element.get_attribute("data-ref")

                self.qrcode = val
                if(self.qrcode == None):
                    self._get_qrcode()
                
                found = True
            except KeyboardInterrupt:
                quit()
            except Exception as e:
                print("Falha no erro: (qr)\n\n")
                print(e)
                found = False
        
        return found, self.qrcode
    
    
    
    def get_user(self, user_id = None,**kwargs) -> UserModel:
        return self.repository.get_user(user_id,**kwargs)
    
    def create(self, user_model: CreateUserModel):
        return self.repository.create(user_model)