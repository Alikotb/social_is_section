#!/usr/bin/env python
# coding: utf-8

# In[1]:


import networkx as nx


# In[2]:


g=nx.Graph()


# In[3]:


g.add_nodes_from(['a','b','c','d'])


# In[4]:


g.add_edges_from([('a','b'),('a','c'),('b','c'),('c','d')])


# In[7]:


nx.draw(g,with_labels=True,
        node_color='blue',
        node_size=1600,
        font_color='white',
        font_size=16,
       )


# In[9]:


for node in g.nodes:
    print(node)
for edge in g.edges:
    print(edge)    


# In[11]:


g.neighbors('b')


# In[13]:


nx.is_tree(g)


# In[14]:


len(list(g.neighbors('a')))


# In[15]:


#>>>>>>>>>>>>> EXERCISE 1<<<<<<<<<<<<<<<<<<<<<<<<<<#


# In[31]:


def get_leaves(G):
    x=''
    for i in G.nodes:
        if G.degree(i)==1:
            x+=i
    return list(x)        
        
    
G = nx.Graph()
G.add_edges_from([
        ('a', 'b'),
        ('a', 'd'),
        ('c', 'd'),
    ])
print(get_leaves(G))
    


# In[25]:


print(G.nodes())
print([G.degree(n) for n in G.nodes()])


# In[34]:


print(open('friends.adjlist').read())


# In[36]:


SG = nx.read_adjlist('friends.adjlist')
nx.draw(SG,with_labels=True,
        node_color='blue',
        node_size=1200,
        font_color='white',
        font_size=16,
       )


# In[77]:


#>>>>>>>>>>>>> EXERCISE 2<<<<<<<<<<<<<<<<<<<<<<<<<<#

def max_degree(SG):
    x=''
    max(len(node) for node in G.nodes())
   # max(SG.degree(n) for n in SG.nodes())
    x=node
    return x

    


# In[78]:


SG = nx.read_adjlist('friends.adjlist')
print(max_degree(SG))
#max_degree(SG)


# In[ ]:


#>>>>>>>>>>>>> EXERCISE 3<<<<<<<<<<<<<<<<<<<<<<<<<<#

def mutual_friends(G, node_1, node_2):
    ds
    dsfgfg
    hg

