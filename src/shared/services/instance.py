from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager

class Instance:
    
    def __init__(self, proxy = False):
        self.need_proxy = proxy
        self.driver = False
    
    def create_browser(self):
        try:
            options = webdriver.ChromeOptions()
            prefs = {'profile.default_content_setting_values': {'images': 2, 
                        'plugins': 2, 'popups': 2, 'geolocation': 2, 
                        'notifications': 2, 'auto_select_certificate': 2, 'fullscreen': 2, 
                        'mouselock': 2, 'media_stream': 2, 
                        'media_stream_mic': 2, 'media_stream_camera': 2, 'protocol_handlers': 2, 
                        'ppapi_broker': 2, 'automatic_downloads': 2, 'midi_sysex': 2, 
                        'push_messaging': 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop': 2, 
                        'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement': 2, 
                        'durable_storage': 2}
                    }
            options.add_experimental_option('prefs',prefs)
            options.add_experimental_option("detach", True)
            options.add_argument("start-maximized")
            # options.add_argument(f"user-data-dir=sessions/{folder}") 
            options.add_argument("disable-infobars")
            options.add_argument("user-agent==Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3312.0 Safari/537.36")
            options.add_argument("--headless")

            caps = DesiredCapabilities().CHROME
            
            if self.need_proxy:
                PROXY_HOST = "177.19.251.218"
                PROXY_PORT = "3130"
                PROXY = F"{PROXY_HOST}:{PROXY_PORT}"
                options.add_argument('--proxy-server=%s' % PROXY)
            
            self.driver = webdriver.Chrome(ChromeDriverManager().install(),options=options,desired_capabilities=caps)
            
            return True
        except Exception as e:
            print(e)
            return False
    
    @property
    def get_driver(self):
        if self.driver:
            return self.driver
        else:
            self.create_browser()
            return self.driver
    
    @property
    def kill(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            return True
        else:
            return True