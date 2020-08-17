#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Your new Phone Number is +12018904454
import twilio


# In[2]:


from twilio.rest import Client
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'yyyyyyyyyyyyyyyyyyyyyyyy'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='hi mummy this gaurav urrf govinda',
         from_='+12018904454',
         to='+918989807743'
     )

print(message.sid)


# In[3]:


from twilio.rest import Client
account_sid = 'ACa1cb7a5d118701df3f4c0ffc53b7c42f'
auth_token = 'e6921c51150461fc1dcae06526cfd4dc'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='hi mummy this gaurav urrf govinda',
         from_='+12018904454',
         to='+xxxxxxxxxxxxxxxxx'
     )

print(message.sid)


# In[4]:


from twilio.rest import Client
account_sid = 'ACa1cb7a5d118701df3f4c0ffc53b7c42f'
auth_token = 'e6921c51150461fc1dcae06526cfd4dc'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='hi mummy this gaurav urrf govinda',
         from_='+12018904454',
         to='+xxxxxxxxxxxxxxxxx'       #my mobile number
     )

print(message.sid)


# In[ ]:



