#!/usr/bin/env python
# coding: utf-8

# In[15]:


###Concatenating strings


from sample_madlibs import arcade, park, snoopy, zoo
import random
if __name__ == '__main__':
     m = random.choice([arcade, park, snoopy, zoo])
     m.madlib()
