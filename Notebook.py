#!/usr/bin/env python
# coding: utf-8

# In[6]:


import wikipedia
import re
from stop_words import get_stop_words


# In[ ]:


stop_words= get_stop_words('es')
len(stop_words)
print(wikipedia.languages())
                           
#fijamos el idioma a español
wikipedia.set_lang("es")
print(wikipedia.search("Python"))
print(wikipedia.search("Python", results = 3))
print(wikipedia.suggest("Madriz"))


# In[8]:


# Que página queremos descargar
wiki = wikipedia.page('Python')

# Sacamos el texto de la página
text= wiki.content

# Sacamos el texto de la página
text= wiki.content

# Cleantext
text= re.sub(r'==.*?==+', '', text) # eliminamos los headers
text= text.replace('\n', '') # eliminamos los saltos de línea

