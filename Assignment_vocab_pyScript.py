#!/usr/bin/env python
# coding: utf-8

# #### Task for today :
#   dataset -   https://archive.ics.uci.edu/ml/datasets/Bag+of+Words
#     
# * q1 = try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count,sample example -  [('sudh', 6 ) , ('kumar',3)]
# * q2 = try to perform a reduce operation to get a count of all the word starting with same alphabet, sample examle =              [(a,56) , (b,34),...........]
# * q3 = Try to filter out all the words from dataset,e.g, .001.abstract = abstract,  =.002 = delete  
# 
# * q4 = create a tuple set of all the records avaialble in all the five file and then store it in sqllite DB, e.g.,       (aah,>=,354,fdsf,wer)
#        
#    
#     
#     
#     

# ##### Background & My approach:
# * There're a total of 5 text files that need to be downloaded. 
# * After downloading created a function to convert them into csv and another function to convert the rows into a list
# * Once the list is created, I have performed the above 4 tasks using the list
# 

# In[11]:


import logging as lg


# In[12]:


#Creating a log file named task

lg.basicConfig(filename='task.log', level=lg.INFO, format='%(asctime)s %(message)s %(levelname)s')


# In[64]:


#creating a function to convert txt to csv

import csv
def txt_csv_read(txt_file,csv_file):
    ''' This converts text files into csv file '''
    
    try:
        
        lg.info('the txt file converted to csv successfully')
        with open(txt_file, 'r', encoding='utf-8') as f:
            content = f.readlines()
            with open(csv_file, 'w+',  newline = '',encoding='utf-8') as csvFile:
                csvWriter = csv.writer(csvFile, delimiter = ' ')
                for elem in content:
                    csvWriter.writerow([elem.strip()])
    except Exception as e:
        lg.exception('An error have occured while converting into csv'+str(e))
            


# In[65]:


#creating a function to read the csv

import csv
def csv_read(csv_file):
    ''' This reads the csv files'''
    
    try:
        file=open(csv_file,'r',encoding='utf-8')
        data=csv.reader(file)
        rows=[]
        rows_list=[]
        for i in data:
            rows.append(i)
        for i in rows:
            if type(i)==list:
                for j in i:
                    rows_list.append(j)
        return rows_list
        lg.info('converting the rows in csv into a list')    
    except Exception as e:
        lg.exception('An error occurred' +str(e))


# #### Q1. Try to find out a count of each and every word in a respective file return a list of tuple with word and its respective count 
# ###### sample example -  [('sudh', 6 ) , ('kumar',3)]
# 
# ###### creating a tuple of words and count of words for the text files, vocab.enron, vocab.kros and vocab.nips

# In[66]:


#converting vocab.enron.txt into venron csv file

txt_csv_read('vocab.enron.txt','venron.csv')


# In[67]:


#converting the elements in venron.csv into a list
venron_list=csv_read('venron.csv')
venron_list


# #### count of each and every word in a respective file return a list of tuple with word and its respective count

# In[17]:


# count of each and every word in a respective file return a list of tuple with word and its respective count
try:
    def count_word_tuple(l):
        word=[]
        count_word=[]
        for i in l:
            word.append(i)
            count_word.append(l.count(i))
            
        return list(zip(word,count_word))
        
    lg.info('A tuple of words and number of counts is created')
        
except Exception as e:
    lg.exception('an error occurred'+str(e))


# In[25]:


count_word_tuple(venron_list)


# ##### Repeating the above excercise for another txt file, vocab.kos

# In[26]:


#converting vocab.kros.txt into venron csv file

txt_csv_read('vocab.kos.txt','vkos.csv')


# In[27]:


#converting the elements in vkos.csv into a list
vkos_list=csv_read('venron.csv')
vkos_list


# In[ ]:


# count of each and every word in a respective file return a list of tuple with word and its respective count


# In[28]:


count_word_tuple(vkos_list)


# #### q2. Try to perform a reduce operation to get a count of all the word starting with same alphabet sample examle = [(a,56) , (b,34),...........]

# In[ ]:


#### perform a reduce operation to get a count of all the word starting with same alphabet on vkos.csv 


# In[78]:


#converting the elements in vkos.csv into a list
vkos_list=csv_read('venron.csv')
vkos_list


# In[30]:


#Defining a function to count the number of words starting with the same alphabet
def count_starting_aplh(l):
    try:
        d={}
        for i in l:
            key=i[0].lower()
            if key in d:
                d[key]=d[key]+1
            else:
                d[key]=1
        for i in d.items():
            print(list(i))
        lg.info('A function to create reduce operation')
    except Exception as e:
        lg.exception('An error occureed'+str(e))
    


# In[32]:


count_starting_aplh(vkos_list)


# #### Repeating the same excercise for vocab.enron.txt

# In[31]:


#converting the elements in venron.csv into a list
venron_list=csv_read('venron.csv')
venron_list


# In[33]:


count_starting_aplh(venron_list)


# #### q3. Try to filter out all the words from dataset, e.g,.001.abstract = abstract, .002 = delete
# 

# In[ ]:


#### filtering out all words from vocab.pubmed.txt


# In[71]:


#converting vocab.pubmed.txt into vpubmed csv file

txt_csv_read('vocab.pubmed.txt','vpubmed.csv')


# In[72]:


#converting the elements in vkos.csv into a list
vpubmed_list=csv_read('vpubmed.csv')
vpubmed_list


# In[74]:


#Trying to filter out the all the words from the list, deleting numbers, special characters etc.
try:
    lst=[]
    lst_alpha=[]
    for i in vpub_list:
        new_string = ''.join(filter(str.isalpha, i))
        lst.append(new_string)
    for j in lst:
        if j.isalpha():
            lst_alpha.append(j)
    lg.info('Extracting the words from vocab.pubmed file')
except Exception as e:
    lg.exception('An error occurred' + str(e))

lst_alpha
    


# #### q4. Create a tuple set of all the records avaialble in all the five file and then store it in sqllite DB, e.g.(aah,>=,354,fdsf,wer) 
#     
#     

# In[79]:


#We converted al text files into csv, except vocab.nytimes. Converting it into csv

txt_csv_read('vocab.nytimes.txt','vnytimes.csv')


# In[81]:


#converting the elements in vnytimes.csv into a list
vnytimes_list=csv_read('vnytimes.csv')
vnytimes_list


# In[82]:


#converting the elements in vnips.csv into a list
vnips_list=csv_read('vnytimes.csv')
vnips_list


# In[108]:


#create a tuple set of all the records avaialble in all the five file
try:
    list_5files=list(zip(venron_list,vkos_list,vnytimes_list,vnips_list,vpubmed_list))
    lg.info('Creating a tuple of all 5 datasets')
except Exception as e:
    lg.exception('An error occurred'+str(e))


# In[109]:


list_5files


# In[90]:



import sqlite3


# In[92]:


db=sqlite3.connect('vocab')


# In[93]:


ls


# In[94]:


#creating cursor
c=db.cursor()


# #### creating a table vocab_tab with columns named by the these 5 datasets

# In[95]:



c.execute('create table vocab_tab(venron text, vkos text, vnytimes text,vnips text,vpubmed text)')


# #### Inserting the list of all files cpmbined, list_5files into sqlite3 db, vocab_tab

# In[111]:


try:
    sql_statement='insert into vocab_tab values(?,?,?,?,?)'
    c.executemany(sql_statement,list_5files)
    lg.info('Inserting all the rows of the combined list')
except Exception as e:
    lg.exception('An error occurred'+str(e))


# In[112]:


for i in c.execute('select * from vocab_tab'):
    print(i)


# In[ ]:




