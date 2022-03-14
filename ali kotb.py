#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hellow from jupyter")


# In[2]:


myStr = 'Ali'
myInt = 20
print(myStr)
print(myInt)


# In[3]:


myStr


# In[6]:


grade=65
if grade<45:
    print("fail")
else:
    print("pass")


# In[7]:


student_names=['Ali','Ahmed','Ossman','Omar']
student_names[2]


# In[8]:


student_names[-2]


# In[9]:


student_names[0:2]


# In[10]:


student_names.append('mohamed')
student_names


# In[11]:


student_names.append('mohamed')
student_names.append('mohamed')
student_names


# In[15]:


del student_names[5:6]
student_names


# In[21]:


for s_name in student_names:
    print('welcome '+s_name+'!')


# In[22]:


long_names = []
for student_name in student_names:
    if len(student_name) > 4:
        long_names.append(student_name)

long_names


# In[23]:


student_pairs = []
for student_name_0 in student_names:
    for student_name_1 in student_names:
        student_pairs.append(
            (student_name_0, student_name_1)
        )

student_pairs


# In[24]:


student_grade=['Ali','EA','A']
student_grade


# In[26]:


student_grade[1]


# In[28]:


student_name, subject, grade = student_grade
print(student_name)
print(subject)
print(grade)


# In[33]:


student_grade=[
    ('Ali','EA','A'),
    ('Ali','web2','B'),
    ('mostafa','EA','A'),
    ('ossman','gp','A'),
]
for s_name,subject,grade in student_grade:
    if grade=='A':
        print('congratulations '+s_name+' for getting '+grade+' in '+subject)
        


# In[34]:


foreign_languages = {
    'Ali': 'Spanish',
    'Bassel': 'French',
    'saad': 'Italian',
    'mohamed': 'Italian',
}
foreign_languages


# In[35]:


'hassan' in foreign_languages


# In[36]:


'mohamed' in foreign_languages


# In[40]:


foreign_languages['Ali'] = 'English'
foreign_languages


# In[41]:


for key in foreign_languages:
    value = foreign_languages[key]
    print(key, 'is taking', value)


# In[43]:


record={
    'name':'Ali',
    'subject':'DM',
    'grade':'B+'
}
print(record['name']+' got '+record['grade']+' in '+record['subject'])


# In[44]:


print(record[0]+' got '+record[2]+' in '+record[1])


# In[46]:


student_grade_records = []
for student_name, subject, grade in student_grade:
    record = {
        'name': student_name,
        'subject': subject,
        'grade': grade,
    }
    student_grade_records.append(record)
    
student_grade_records


# In[ ]:




