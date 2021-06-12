#!/usr/bin/env python
# coding: utf-8

# In[1]:


#DATA HANDLING AND WORKING WITH FILES
#Python too supports file handling and allows users to handle files i.e.,
#to read and write files, along with many other file handling options, to operate on files.
#Files are named locations on disk to store related information. 
#They are used to permanently store data in a non-volatile memory (e.g. hard disk).

#When we want to read from or write to a file, we need to open it first.
#When we are done, it needs to be closed so that the resources that are tied with the file are freed.


# In[2]:


#The key function for working with files in Python is the open() function.

#The open() function takes two parameters; filename, and mode.

#There are four different methods (modes) for opening a file:


# In[3]:


#Hence, in Python, a file operation takes place in the following order:

#Open a file
#Read or write (perform operation)
#Close the file


# In[6]:


# r , for reading.
# w , for writing.
# a , for appending.
# r+ , for both reading and writing


# In[18]:


#program to create,read and write:

def main():
    f= open("Internity.txt","w+")
    #f=open("Internity.txt","a+")
    for i in range(10):
         f.write("This is line %d\r\n" % (i+1))
    f.close()
    
if __name__== "__main__":
  main()


# In[19]:


file = open('Internity.txt', 'r')

print (file.read())


# In[20]:


file = open('Internity.txt','w')
file.write("This is the write command")
file.write("It allows us to write in a particular file")
file.close()


# In[21]:


f=open("Internity.txt", "a+")
for i in range(2):
     f.write("Appended line %d\r\n" % (i+1))


# In[22]:


file = open('Internity.txt', 'r')

print (file.read())


# In[ ]:


#Database connectivity
#1. 
#There are the following steps to connect a python application to our database.

Import mysql.connector module
Create the connection object.
Create the cursor object
Execute the query


# In[4]:


#2.Creating the connection
To create a connection between the MySQL database and the python application, the connect() method of 
mysql.connector module is used.


# In[5]:


#3.syntax to use connect()
Connection-Object= mysql.connector.connect(host = <host-name> , user = <username> , passwd = <password> )  


# In[6]:


#4.Creating a cursor object
The cursor object can be defined as an abstraction specified in the Python DB-API 2.0. 
<my_cur>  = conn.cursor()  


# In[ ]:


#How to connect to a remote MySQL database using python?

Before we start you should know the basics of SQL,the methods used in this code: 

connect(): This method is used for creating a connection to our database it has four arguments: 
1.Server Name
2.Database User Name
3.Database Provider
4.Database Name
cursor(): This method creates a cursor object that is capable of executing SQL queries on the database.
execute(): This method is used for executing SQL queries on the database. It takes a sql query( as string) as an argument.
fetchone(): This method retrieves the next row of a query result set and returns a single sequence, or None if no more rows are available.
close() : This method close the database connection.
 

