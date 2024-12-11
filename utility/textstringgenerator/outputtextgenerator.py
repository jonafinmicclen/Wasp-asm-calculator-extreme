# Generates wasp code for storing text into memory for display
# Example output text001: DC.W 'a'


def generate(text_to_generate, name):
    num = 0
    with open(f'{name}.txt', 'w') as file:
        for char in text_to_generate:
            file.write(f'{name}{num}: DC.W \'{char}\'\n')
            num+=1
            
# 'Please enter your expression in the format "a+b=" max input number is 65535:\n'

generate('You entered:\n', 'youentered')