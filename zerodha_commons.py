import math
from dotenv import load_dotenv
from stock_jugaad import CommonUtils

class ZerodhaCommons:
    
    def __init__(self):
        # This method is intentionally left empty.
        self.common_utils = CommonUtils()
        pass

    def send_message(self, message):
        self.common_utils.send_message(message=message)
               
    def at_percentage(self, percentage):
        return (1 + percentage/100)
    
    def quote(self, nse_instruments):
            return self.common_utils.quote(nse_instruments=nse_instruments)

    def send_whatsapp_message(self, phone_number, message):
        self.common_utils.send_whatsapp_message(phone_number=phone_number, message=message)
        
    def roundoff(self, value):
        return math.ceil(value * 20) / 20