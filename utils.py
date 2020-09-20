import string 

def clean_string(text):
    text = " ".join(text.split())
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.lower().title().strip() 

if __name__ == '__main__':
    print(clean_string(text))