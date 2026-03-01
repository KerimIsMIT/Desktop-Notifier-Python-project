import time
import notify2
from topnews import topStories 


ICON_PATH = "/full/path/to/icon.png" 

newsitems = topStories()

notify2.init("News Notifier")

n = notify2.Notification(None, icon=ICON_PATH)
n.set_urgency(notify2.URGENCY_NORMAL)  # Normal urgency
n.set_timeout(10000)  


for newsitem in newsitems:
    n.update(newsitem['title'].decode('utf8'), newsitem['description'].decode('utf8'))
    n.show()
    time.sleep(15)  

print("All notifications displayed!")
