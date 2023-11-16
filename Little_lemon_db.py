#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector 

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    user="root",
    password="myNewPass",
    database="little_lemons_db"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the insert query
insert_employees = """
INSERT INTO employees (EmployeeID, Name, Role, Address, Contact_Number, Email, Annual_Salary)
VALUES
    (01, 'Mario Gollini', 'Manager', '724, Parsley Lane, Old Town, Chicago, IL', 351258074, 'Mario.g@littlelemon.com', '$70,000'),
    (02, 'Adrian Gollini', 'Assistant Manager', '334, Dill Square, Lincoln Park, Chicago, IL', 351474048, 'Adrian.g@littlelemon.com', '$65,000'),
    (03, 'Giorgos Dioudis', 'Head Chef', '879 Sage Street, West Loop, Chicago, IL', 351970582, 'Giorgos.d@littlelemon.com', '$50,000'),
    (04, 'Fatma Kaya', 'Assistant Chef', '132 Bay Lane, Chicago, IL', 351963569, 'Fatma.k@littlelemon.com', '$45,000'),
    (05, 'Elena Salvai', 'Head Waiter', '989 Thyme Square, EdgeWater, Chicago, IL', 351074198, 'Elena.s@littlelemon.com', '$40,000'),
    (06, 'John Millar', 'Receptionist', '245 Dill Square, Lincoln Park, Chicago, IL', 351584508, 'John.m@littlelemon.com', '$35,000');
"""

# Execute the insert query
cursor.execute(insert_employees)

# Commit the transaction and close the connection
connection.commit()
connection.close()


# In[8]:


import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    user="root",
    password="myNewPass",
    database="little_lemons_db"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the SQL query to retrieve data from the table
select_query = "SELECT * FROM bookings"

# Execute the select query
cursor.execute(select_query)

# Fetch all rows of data
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)



# In[1]:


import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    user="root",
    password="myNewPass",
    database="little_lemons_db"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the SQL query to retrieve data from the table
select_query = "SELECT * FROM menus"

# Execute the select query
cursor.execute(select_query)

# Fetch all rows of data
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)


# In[2]:


import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    user="root",
    password="myNewPass",
    database="little_lemons_db"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the SQL query to retrieve data from the table
select_query = "SELECT * FROM orders"

# Execute the select query
cursor.execute(select_query)

# Fetch all rows of data
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)


# In[4]:


import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    user="root",
    password="myNewPass",
    database="little_lemons_db"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the SQL query to retrieve data from the table
select_query = "SELECT * FROM MenuItems"

# Execute the select query
cursor.execute(select_query)

# Fetch all rows of data
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)


# In[5]:


import mysql.connector

# Establish a connection to the MySQL database
connection = mysql.connector.connect(
    user="root",
    password="myNewPass",
    database="little_lemons_db"
)

# Create a cursor object to interact with the database
cursor = connection.cursor()

# Define the SQL query to retrieve data from the table
select_query = "SELECT * FROM Employees"

# Execute the select query
cursor.execute(select_query)

# Fetch all rows of data
rows = cursor.fetchall()

# Display the data
for row in rows:
    print(row)


# In[ ]:




