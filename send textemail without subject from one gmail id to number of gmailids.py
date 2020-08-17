#!/usr/bin/env python
# coding: utf-8

# In[25]:


import smtplib


# In[26]:


sender_email="gauravbaser007@gmail.com"
rec_email=["gbaser1996@gmail.com","gauravbaser1011@gmail.com"]


# In[18]:


password=input(str("Please enter your password : "))


# In[19]:


message="subject-testing through python body-hey this message is send my python"


# In[20]:


server=smtplib.SMTP('smtp.gmail.com',587)


# In[21]:


server.starttls()


# In[22]:


server.login(sender_email,password)
print("Login success")


# In[24]:


server.sendmail(sender_email,rec_email,message)
print("Email has been sent to",rec_email)


# In[ ]:




