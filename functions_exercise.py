def is_two():
    
    x = input('what is your number\n')
    if x == 2 or x =="2":
        return True
    else:
        return False 

is_two()

def is_vowl(word):
    word = input('enter your string here \n').lower()
    
    if any(letters in word for letters in 'aeiou'):
            return True
    else:
        return False
    
    
    
    
   

is_vowl()

def is_consonat():
    string = input('Enter a string value \n').lower()
    
    if any(letters in string for letters in 'aeiou'):
            return False
    else:
        return True
    

is_consonat()

def auto_caps_con():
    word = input('what is your word \n').lower()
    vowls = ()
    for letters in word:
       pass
    
#     if any(letters in word for letters in 'aeiou'):
    if letters[0]== 'a' or 'e' or 'i' or 'u': 
        print('the first letter is a vowl')
    else:
        print('first letter is a constant')
      
    

auto_caps_con()

