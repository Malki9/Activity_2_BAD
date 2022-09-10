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


def insert_at_end(self,dataval)
    new_node = Node(dataval)     
    if self.head is None:     #Check whether the Linkedlist is empty or not
        self.head = new_node
    else:                     #If it is not empty   
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = new_node     #Change the n.next of the last node to new_node

class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def top(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
 def are_Parantheses_Valid(expr):
    p_stack = Stack()
    
    for para in expr:
        if para in ["(", "{"]:
            p_stack.push(para)    
        if para in [")", "}"]:
            x = p_stack.pop()
        
            
            if para == '(' and x == ')':
                    return "Valid"
                
            if para == '{' and x == '}':
                    return "Valid"
                
    
    if not p_stack.isEmpty():
        return "Invalid"
    else:
        return "Valid"
