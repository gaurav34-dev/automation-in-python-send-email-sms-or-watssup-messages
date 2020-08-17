#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib


# In[2]:


sender_email="gauravbaser007@gmail.com"
rec_email=["gbaser1996@gmail.com","gauravbaser1011@gmail.com","ushakiranbaser@gmail.com","divbaser@gmail.com"]


# In[3]:


password=input(str("Please enter your password : "))


# In[4]:


subject="python email testing"


# In[5]:


body="this is a tutorial to sending email from one particular email to all other email-ids through automation of python "


# In[6]:


message="Subject:{}\n\n{}".format(subject,body)
print(message)


# In[7]:


server=smtplib.SMTP('smtp.gmail.com',587)


# In[8]:


server.starttls()


# In[9]:


server.login(sender_email,password)
print("Login success")


# In[10]:


server.sendmail(sender_email,rec_email,message)
print("Email has been sent to",rec_email)


# In[ ]:




