from datetime import *

currentDate = datetime.now()
delta = timedelta(days=5)
fiveDays = currentDate - delta
print(fiveDays.strftime("%d.%m.%Y"))