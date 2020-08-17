#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Your new Phone Number is +xxxxxxxxxxxxxxxxx
import twilio


# In[2]:


from twilio.rest import Client
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'yyyyyyyyyyyyyyyyyyyyyyyy'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='hi mummy this gaurav urrf govinda',
         from_='zzzzzzzzzzzzzz',
         to='xxxxxxxxxxxxxxxxxx'
     )

print(message.sid)


# In[3]:


from twilio.rest import Client
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='hi mummy this gaurav urrf govinda',
         from_='zzzzzzzzzzzzzzzz',
         to='+xxxxxxxxxxxxxxxxx'
     )

print(message.sid)


# In[4]:


from twilio.rest import Client
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='hi mummy this gaurav urrf govinda',
         from_='zzzzzzzzzzzzzzz',
         to='+xxxxxxxxxxxxxxxxx'       #my mobile number
     )

print(message.sid)


# In[ ]:



