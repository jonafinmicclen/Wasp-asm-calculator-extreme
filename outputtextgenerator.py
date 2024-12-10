# Generates wasp code for storing text into memory for display
# Example output text001: DC.W 'a'

num = 0

with open('generatedoutputtext.txt', 'w') as file:
    text_to_generate = 'Please enter your expression in the format "a+b=" max input number is 65535:\n'
    for char in text_to_generate:
        file.write(f'text{num}: DC.W \'{char}\'\n')
        num+=1