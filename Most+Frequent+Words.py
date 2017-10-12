
# coding: utf-8

# 
# 
# 
#                                             Mounib Ismail - Data Science Pipeline 
# ______________________________________________________________________________________________________________________
# 
# 
# 
# 
# 
# 
# 
# 

# In[41]:


#store book link 
link='https://www.gutenberg.org/files/1342/1342-h/1342-h.htm'


# In[42]:


#import requests package
import requests

#make request and use get function
req=requests.get(link)
print("req type:") 
type(req)


# In[43]:


# Response is an object that has an attribute " text "
# create HTML from attribute text 
html=req.text
#print (html)


# In[35]:


#parse HTML to extract Text #We use a package called BeautifulSoup 
from bs4 import BeautifulSoup
soup=BeautifulSoup(html, "html5lib")
#print (soup)
type(soup)


# In[36]:


#get title ; use the beautiful soup functions
soup.title


# In[37]:


soup.title.string


# In[40]:


#extract text only from HTML "soup"
textonly= soup.get_text()
#print (textonly)


# In[57]:


#Import re package 
import re 
#create sentence
#sentence="peter and ben are extremely paranoid ; paul is p op punctual "
#create the reg you want to search for
ps='\w+'
#re.findall(ps,sentence)


# In[61]:


allwords=re.findall(ps,textonly)
allwords[:8]


# In[63]:


# Import RegexpTokenizer from nltk.tokenize
from nltk.tokenize import RegexpTokenizer

# Create tokenizer
tokenizer = RegexpTokenizer('\w+')

# Create tokens
tokens = tokenizer.tokenize(textonly)
#check first 10 
#tokens[:10]


# In[64]:


# Initialize new list
words = []

# Loop through list tokens and make lower case
for word in tokens:
    words.append(word.lower())

# Print several items from list as sanity check
words[:8]


# In[68]:


nltk.download('stopwords')


# In[69]:


# Import nltk
import nltk

# Get English stopwords and print some of them
sw = nltk.corpus.stopwords.words('english')
sw[:5]


# In[70]:


# Initialize new list
words_ns = []

# Add to words_ns all words that are in words but not in sw
for word in words:
    if word not in sw:
        words_ns.append(word)

# Print several list items as sanity check
words_ns[:5]


# In[71]:


#Import datavis libraries
import matplotlib.pyplot as plt
import seaborn as sns

# Figures inline and set visualization style
get_ipython().magic('matplotlib inline')
sns.set()

# Create freq dist and plot
freqdist1 = nltk.FreqDist(words_ns)
freqdist1.plot(25)


# In[72]:


# Import stopwords from sklearn
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS

# Add sklearn stopwords to words_sw
sw = set(sw + list(ENGLISH_STOP_WORDS))

# Initialize new list
words_ns = []


# Add to words_ns all words that are in words but not in sw
for word in words:
    if word not in sw:
        words_ns.append(word)


# Create freq dist and plot
freqdist2 = nltk.FreqDist(words_ns)
freqdist2.plot(25)


#                                                 
#                                                 
#                                                 
#                                                 
#                                                 
#                                                 
#                                                 
#                                                 
#                                                 END
#                                                 
#                                                 
#                                                 
#                                                 
#                                                 
#                                                 
#                                                 
#                                                 
# 
