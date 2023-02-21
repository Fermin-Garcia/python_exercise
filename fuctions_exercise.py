#!/usr/bin/env python
# coding: utf-8

# # is_two Function
# - It should accept one input and return True 
# - if the passed input is either the number or the string 2, False otherwise.

# In[89]:


def is_two():
    
    x = input('what is your number\n')
    if x == 2 or x =="2":
        return True
    else:
        return False 


# In[90]:





# # is_vowel function
# - It should return True if the passed string is a vowel, False otherwise.

# In[91]:


def is_vowl():
    word = input('enter your string here \n').lower()
    
    if any(letters in word for letters in 'aeiou'):
        return True
    else:
        return False
    
    
    
    
   


# In[94]:





# # is_consonant function
# - It should return True if the passed string is a consonant, False otherwise. 
# - Use your is_vowel function to accomplish this.

# In[95]:


def is_consonant():
    x = is_vowl()
    if x == False:
        return True
    else:
        return False


# In[96]:





# ## Define a function that accepts a string that is a word. 
# - The function should capitalize the first letter of the word if the word starts with a consonant.

# In[97]:


def is_vowl_1():
    word = input('enter your string here \n').lower()
    letter_one = word[0].lower()
    if letter_one == 'a':
        print(letter_one.upper() + word[1:])
        
    elif letter_one == 'e':
        print(letter_one.upper() + word[1:])
        
    elif letter_one == 'i':
        print(letter_one.upper() + word[1:])
        print('you see this? ')
        
    elif letter_one == 'o':
        print(letter_one.upper() + word[1:])
        
    elif letter_one == 'u':
        print(letter_one.upper() + word[1:])
    else:
        print(word)

    


# In[99]:





# ## Define a function named calculate_tip
# - It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[100]:


def calculate_tip():
    percent = int(input('What percent do you want to leave \n '+' %'))
    total = float(input('what is your total $'))
    total_tip = (percent / 100) * total
    print("your recommended tip amount is $", total_tip)
    print('Your total with the tip is ', (total + total_tip))


# In[101]:





# ### Define a function named apply_discount. 
# - It should accept a original price, and a discount percentage and return the price after the discount is applied.

# In[102]:


def apply_discount():
    og_amount = float(input('what is the original amount \n $'))
    discount_percent = int(input("what is the discount amount \n %"))
    discount_dec = (discount_percent / 100)
    discount_amount = discount_dec * og_amount
    
    print(f' You have ${discount_amount:.2f} off, which should bring your total to about ${(og_amount - discount_amount):.2f} total.')


# In[103]:




# In[104]:


def handle_commas():
    num_str = input("Enter a number as a string with commas: ")
    cleaned_str = num_str.replace(',', '')
    return (cleaned_str)


# In[105]:
def get_letter_grade():
    num_grade = float(input('Enter the number grade! '))
    if num_grade <= 69.99:
        print('This is a F!')
    elif num_grade <= 79.99:
        print('This is a C!')
    elif num_grade <= 89.99:
        print('This is a B!')
    elif num_grade > 89.99:
        print('This is a A!')
    else:
        pass
    
def remove_vowels():
    vowels = ['a', 'e', 'i', 'o', 'u']
    word = input('What is the string? ')
    no_vowels = [letter for letter in word if letter not in vowels]
    print(''.join(no_vowels))

    
def cumulative_sum(numbers):
    cumulative_sum_list = []
    cumulative_sum = 0
    for num in numbers:
        cumulative_sum += num
        cumulative_sum_list.append(cumulative_sum)
    return cumulative_sum_list




