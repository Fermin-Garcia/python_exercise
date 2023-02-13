

def is_vowl(word):
    word = input('enter your string here \n').lower()
    
    if any(letters in word for letters in 'aeiou'):
            return True
    else:
        return False

