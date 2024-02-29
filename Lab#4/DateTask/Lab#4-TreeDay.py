from datetime import *

today = datetime.now().date()
yesterday = today - timedelta(days=1)
tommorow = today + timedelta(days=1)



print(yesterday.strftime("%d.%m.%Y"), 
      today.strftime("%d.%m.%Y"), 
      tommorow.strftime("%d.%m.%Y"))