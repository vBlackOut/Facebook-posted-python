# -*- coding: Utf-8 -*-
from pyFacebook import Facebook
from fbchat import Chat
from secure import *

import asyncio
import time

# start time execuion
start_time = time.time()

"""  call class for back Facebook and Chat
     get show for display of hidden broswer  """

crawler_facebook = Facebook(show=0)
chat_facebook = Chat(crawler_facebook)

# login on facebook call function
crawler_facebook.login("your_email", decode(None, "your_hash_secure"))

# get list of friend on my profile
crawler_facebook.get_friend()

# post message on my wall
crawler_facebook.create_post("Great vBlackOut")

# create the infinit loop for wait action
loop = asyncio.get_event_loop()
chat_open = loop.run_until_complete(chat_facebook.detect_chat_online(loop, "detect"))
loop.run_forever()
print (chat_open)


# logout function
crawler_facebook.logout()


# print time execution
interval = time.time() - start_time
print('Total time in seconds:', interval)