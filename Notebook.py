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


# In[12]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# Creamos una función para generar el gráfico
def plot_cloud(wordcloud):
    # fijamos el tamaño
    plt.figure(figsize=(40, 30))
    # plotde la imagen
    plt.imshow(wordcloud)
    # sin ejes
    plt.axis("off")


# In[ ]:


# Importamos el paquete para hacer la nube de palabras
from wordcloud import WordCloud

# Genaramosla nube
wordcloud= WordCloud(width= 3000, height= 2000, random_state=1,
                     background_color='white',colormap='viridis',
                     collocations=False, stopwords= stop_words + ["Python", "puede", "pueden"]).generate(text)
plot_cloud(wordcloud)

