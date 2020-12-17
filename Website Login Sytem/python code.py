#!/usr/bin/env python
# coding: utf-8

# # Computing 5 Assignment
# 
# 

# ---
# ## Background
# 
# In this assignment you will be implementing a set of functions used in conjunction to form a website login system. Your system will utilize a text file for storing, retrieving, and verifying user credentials. We identify users based on their **username** and **password**. For simplicity we assume that usernames and passwords only contain alphanumeric characters. Alphanumeric characters represent the numbers **0-9** and the letters **A-Z** (both uppercase and lowercase). Usernames and passwords are case sensitive and must contain **at least 6** characters. Usernames must be unique.
# 
# Each username and password combination will be stored on its own line in the text file. Each line in the text file has the following format:
# 
# 
# <br>
# \begin{align}
#   \texttt{username\tpassword\n}\tag{1}
# \end{align}
# <br>
# 
# More explicitly, each line in the text file will contain a user’s username, a tab character, and that user’s password followed by the newline character. Please note that when opening the text file for viewing you will not explicitly see the **\t** and **\n** characters.
# 
# 
# In your implementation, usernames and passwords will be stored as plain text. This means that all usernames and passwords can easily be compromised if access to the text file is provided. This is extremely dangerous in the real world and poses huge security issues. In practicality, passwords are encrypted before stored so that they are not easily identifiable in the event of a data breach. Thus, please do not use any real passwords when developing and testing your program. 
# 
# The following section contains additional information that will assist in implementing your login system.

# ---
# ## Additional Information
# 
# There are two functionalities built into python that will assist in implementing your system.
# 
# At this point you should be familiar with python's **in** keyword. You have used it to iterate through a sequence in a for loop. For example **for i in range(10):** will iterate through the numbers 0-9. The **in** keyword can also be used to identify if a value is present in a sequence. This is achieved using the following expression:
# 
# <br>
# \begin{align}
#   \texttt{<value> in <sequence>}
# \end{align}
# <br>
# 
# The expression will return **True** if the value is present in the list, otherwise **False**. Consider the following example: 
# 

# In[ ]:


x = ["a","b","c","d"]
result1 = "d" in x
result2 = "OKAY" in x
result3 = 5 in x
result4 = "b" in x
print(result1, result2, result3, result4)


# Run the code to see which expressions result to True and which result to False!
# 
# Secondly, the **index** method can be used to find the index of a given value in a sequence. This is achieved using the following expression:
# 
# <br>
# \begin{align}
#   \texttt{<sequence>.index(<value>)}
# \end{align}
# <br>
# 
# Consider the following example:
# 

# In[ ]:


x = ["a","b","c","d"]
i1 = x.index("a")
i2 = x.index("b")
i3 = x.index("f")
print(i1,i2,i3)


# Run the code to verify that i1, i2, and i3 contain the index of “a”, “b”, and “d” in the list x, respectively. Note that the command will provide an error if the value does not exist in the sequence. In addition, the command will return the index of the first occurrence of a value if duplicated values exist in a given list. For the purposes of this assignment, you do not have to worry about these cases!
# 
# You now have all the information necessary to begin implementing the login system!

# ---
# ## NOTE: YOU WILL BE MARKED ON MULTIPLE ITEMS IN THIS LAB IN ADDITION TO THE FUNCTIONALITY OF YOUR CODE
#  - Variable Names
#  - Commenting
#  - General Legibility
#  - Reflective Questions

# ---
# ## Program Requirements (12 Marks)
# 
# Your task is to implement a set of functions that will be used in conjunction to form a website login system. Your system will read and write user credentials from a text file that emulates a database. The requirements of the system are given below. Please ensure that your functions have the EXACT naming as specified! Failure to do so will result in lost marks.
# 
# 
# 1. Define a function **getUserData**(*filename*):
#   - ***filename***: A *string* representing the name of the text file (ex. “database.txt”) that stores user login credentials in the form of (1).
#   - **Function Description**: The function performs the following actions:
#     - Opens a file with the name *filename* for reading.
#     - Initializes two empty lists: **usernames**, and **passwords**
#     - Iterates through each line in the file and extracts the username and password in each line. On each iteration, the username is appended as a string to **usernames** and the password is appended as a string to **passwords**. Thus, after each line in the file has been iterated, **usernames[i]** and **passwords[i]** will contain the username and password for a given user at a given index i
#     - Closes the file with *filename*<br>*(Note that it is assumed that the file associated with filename exists before the function is called)*
#   - **Return**: A *list* of length 2 where the first element is the **usernames** list and the second element is the **passwords** list populated with the data from *filename* as described above. <br>*(Hint: You can split at tabs by providing "\t" as the argument, similar to "\n" for new lines)*
#   
# 
# 2. Define a function **exists**(*username*, *filename*):
#   - ***username***: A *string* representing a username.
#   - ***filename***: A *string* representing the name of the text file (ex. “database.txt”) that stores user login credentials in the form of (1).
#   - **Return**: *True* if *username* exists in *filename*, otherwise *False*.<br>*(Hint: User your getUserData function and the **in** keyword. Refer to the additinal information section*
# 
# 
# 3. Define a function **createUser**(*username*, *password*, *filename*):
#   - ***username***: A *string* representing a username.
#   - ***password***: A *string* representing a password.
#   - ***filename***: A *string* representing the name of the text file (ex. “database.txt”) that stores user login credentials in the form of (1).
#   - **Function Description**: The function performs the following actions:
#     - If *username* **does not** exist in *filename*, open *filename* in append mode, write the username and password in the form (1), and close the file.
#     - If *username* **does** exist in *filename*, do nothing.
#   - **Return**: *True* if *username* and *password* were added to *filename*, otherwise *False*
# 
# 
# 4. Define a function **login**(*username*, *password*, *filename*):
#   - ***username***: A *string* representing a username.
#   - ***password***: A *string* representing a password.
#   - ***filename***: A *string* representing the name
#   - **Function Description**: The function performs the following actions:
#     - If *username* **does** exist in *filename*, find the password associated with *username* in *filename* and check if *password* is equal to the expected password.<br> *(Hint: Use your **getUserData** function and the **index** method. Refer to the additional information section)*
#     - If the username **does not** exist in *filename*, do nothing.
#   - **Return**: *True* if *password* matches the password associated with *username* in *filename*. *False* if the passwords do not match or *username* does not exist in *filename*.

# ---
# ## Implementation
# Please define all functions in the cell below

# In[ ]:


# YOUR CODE HERE
def getUserData(filename):
    data=open(filename, "r") #opens file                                                       
    usernames=[]                                                                    
    passwords=[]
    while True:
        d=data.readline()  #reads file                                                 
        if(d==""): #check if there are spaces                                                                
            break
        usernames.append(d.split("\t")[0].strip()) #adds usernames and passwords to respective lists                          
        passwords.append(d.split("\t")[1].strip())                            
    data.close() #closes file                                                                   
    return [usernames, passwords]                                                   

def exists(username, filename): 
    g=getUserData(filename)                                                         
    result=username in g[0] #see if the username exists                                          
    return result
    
def createUser(username, password, filename):
    e=exists(username, filename)                                                   
    if e == False: #adds username and password to the list                                                          
        with open(filename, "a") as file:
            file.write(username+'\t'+password+'\n')
        return True
    return False

def login(username, password, filename):
    e=exists(username, filename)
    if e==True:
        if password==getUserData(filename)[1][getUserData(filename)[0].index(username)]: #makes sure they're pairs
            return True
    return False

# Testing
def main():

    database = "database.txt"
    while True:
        ans = input("Press [q] to quit, [l] to login, [c] to create an account: ")
        if ans == "q":
            # Break if the user quits
            break
        elif ans == "l":
            # Login if the user types in "l"
            uname = input("Please enter your username: ")
            password = input("Please enter your password: ")
            if login(uname, password, database):
                print("Login sucessful!\n")
            else:
                print("Sorry, login unsucessful :(\n")
        elif ans == "c":
            # Create an account if the user types in c
            uname = input("Please create a username: ")
            password = input("Please create a password: ")
            # Check if username exists
            if createUser(uname, password, database):
                    print("Account creation sucessful for user,",uname,"\n")
            else:
                    print("Sorry,",uname,"is already taken!\n")
        else:
            print("Please enter a valid character")
main()


# The main function above utilizes the functions you have created to simulate the login system environment. Inspect the code and play around with the funtionality to test out all of your functions. A file has already been created for you called "database.txt". This file contains one user with the following credentials:
# 
# Username: iLoveMac
# Password: iamthebeststudent123
# 
# Use the credentials to log into the system or create your own using the main function!

# ----------
# ## Code Legibility (6 Marks)
# Your code will be marked on commenting and code legibility.<br>
# The mark breakdown is as follows:<br>
# 2 marks for using appropriate variable names that indicate what is being stored in that variable<br>
# 2 marks for leaving comments on major parts of your code such as where you read the file or calculate a summation<br>
# 2 marks for general legibility. The TA's should be able to understand your code without spending hours reading it. For example do not put your code in one very long line as this is hard for someone else reading your code to understand

# ---
# ## Reflective Questions (6 Marks)
# 
# 1. The createUser function requires that filename is opened in append mode in order to add a username/password combinations to filename. What will happen if filename is instead opened in write mode? Assume you are forced to use any access mode other append. Is it possible to re-write the function such that the functionality does not change? Please explain.
# 
# 
# 2. Assume you have to write a function **validLength** that would check if the *username* and *password* are greater than 6 characters. How would you implement this function?
# 
# 
# 3. Assume you have two functions **encrypt(password)** and **decrypt(encoded_password)**. The function **encrypt** takes a password string and returns an encoded version of the password as a string. The function **decrypt** decodes  the encoded_password string and returns the decoded password as a string. Where would you use these functions in your code if you wanted your login system to store encoded user passwords rather than raw text passwords?
# 
# Please answer all questions in the cell below!

# ```
# 1.if the file was opened in write mode it would overwrite the entire file instead of adding to it like in append mode. I think it is possible, but it would be super complicated. To do this you could write something and save it to a variable, then write something else ontop of that variable and write the varible back into the file again. To elaborate, if we need to erase the file every time you would need to save it, and then write something and add the old file back into the new one. This is exactly like what you would do if you were to transfer a old word file to a newer word file, same concept.
# 2.To check if your username and password are greater than 6 characters you could use if statments and the len() function to see how many characters are in the password and username. To implement this you would need to put it in the createUser function and make if statements to make sure username and password are greater than 6 characters (including or excluding spaces/special characters).
# 3.The encrypt function would go into the createUser and decrypt would go into the login. This is because when the user creates a password it would encrypt the password and save that in a file/database and then when the user logs in the program will decrypt that password for them to use to log in.
# ```

# ---
# ## Submission
# 
# Please download this notebook as a .py file (*File* > *Download as* > *Python (.py)*) and submit it to the Computing Lab 5 dropbox on avenue with the naming convention: macID_CL5.py
# 
# **Make sure the final version of your lab runs without errors, otherwise, you will likely recieve zero.**
# 
# This assignment is due the day after your Lab A section at 11:59 PM EST
# 
# Late labs will not be accepted
