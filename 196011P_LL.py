#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node:
    def __init__(self, dataval):
        self.dataval = dataval
        self.next = None


# In[3]:


class LinkedList:
    def __init__(self):
        self.head = None
        
def insert_at_head(self, dataval):
    new_node = Node(dataval)
    new_node.next = self.head
    self.head= new_node
    
def traverse(self):
    n = self.head
    while n is not None:
        print(n.dataval, end=' ')
        n = n.next


# In[4]:


def insert_at_end(self,dataval):
    new_node = Node(dataval)     
    if self.head is None:     #Check whether the Linkedlist is empty or not
        self.head = new_node
    else:                     #If it is not empty   
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node     #Change the n.next of the last node to new_node

