from src.shared.services.instance import Instance
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from src.shared.services.instance import Instance
from src.domain.services.qrcode_service import QrcodeService

from src.config import environment

class WhatsAppService:
    
    def __init__(self, instance: Instance, qrcode_service: QrcodeService):
        self.instance = instance
        self.qrcode_service = qrcode_service
    
    def access_whatsapp_url(self):
        browser = self.instance.get_driver
        browser.get("https://web.whatsapp.com/send/?phone=996061956")
    
    def make_login(self, user_id:int):
        self.access_whatsapp_url()
        _, first_qr = self.qrcode_service.get_qrcode()
        self.qrcode_service.send_kafka_qrcode(first_qr, user_id)
        if self.wait_wp_web(user_id):
            return True
        return False

    
    def wait_wp_web(self, user_id:int):

        found = False
        while(found != True):
            browser = self.instance.get_driver
            try:
                WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CLASS_NAME, environment.get_item("LOGGED_WP_ELEMENT"))))
                found = True
            
            except KeyboardInterrupt:
                quit()
            
            except Exception as e:
                print(f"Falha no erro: (falha ao identificar escaneamento do qrcode) {e}")
                print(f"Reenviando Qrcode")
                _, qrcode = self.qrcode_service.get_qrcode()
                self.qrcode_service.send_kafka_qrcode(qrcode, user_id)

                found = False
        return found
    
    def _get_message(self):
        with open(self.msg_path,encoding="utf-8") as f:
            lines = f.readlines()
        return lines

    def _compare_message(self,file_msg):
        with open(self.msg_path,encoding="utf-8") as f:
            lines = f.read()
        return lines.replace("\n","") == file_msg.replace("\n","")

    def make_contact(self,phone):
        browser = self.instance.get_driver
        
        try:
            contact_link = self.create_wp_url(self.wp_link,phone)
            browser.get(contact_link)
        
        except KeyboardInterrupt:
                quit()
        
        except:
            print("Falha no erro: (002)")
        try:
            WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, "_2A8P4")))
            typed = False
            chat = browser.find_elements_by_class_name("_2_1wd")[1]
            while(typed == False):
                try:
                    WebDriverWait(browser, 0.3).until(EC.presence_of_element_located((By.CLASS_NAME, "_1E0Oz")))
                    typed = True
                
                except KeyboardInterrupt:
                    quit()
                
                except:
                    chat.click()
                    chat.send_keys(".")
                
            sleep(0.3)
            lines = self._get_message()
            ret = False
            while (ret == False):
                chat.send_keys(Keys.CONTROL,"a")
                chat.send_keys(Keys.BACKSPACE)

                for line in lines:
                    line = line.replace("\n","")
                    print(line)
                    chat.send_keys(line,Keys.SHIFT,Keys.ENTER)

                value_input = chat.get_attribute('innerHTML')
                ret = self._compare_message(value_input)                

            send_btn = browser.find_element_by_class_name("_1E0Oz")
            send_btn.click()
            print(f"mensagem enviada para {phone}")
        
        except KeyboardInterrupt:
            quit()
        
        except:
            print(f"Falha no erro: (004 -> {phone})")