"""

📌 Task Requirements:
Create a file called input.txt and write at least five lines of text into it.
Write a Python script to:
Read the contents of input.txt.
Count the number of words in the file.
Convert all text to uppercase.
Write the processed text and the word count to a new file called outputs.txt.
Print a success message once the new file is created.

"""
with open('C:/Users/Nzilani/Downloads/Task1.txt','w') as file:
    data =file.write("Hello, friend!\n")
    data=file.write("Hello, Python!\n")
    data=file.write("Hello, Java!\n")
    data=file.write("Hello, JS!\n")
    data=file.write("Hello, SQL!\n")
    print(data)

with open('C:/Users/Nzilani/Downloads/Task1.txt','rt') as file:
    content=file.read()
    print(content)


count_words=len(content.split())

upper_case=content.upper()   
print(upper_case)

try:
  with open('C:/Users/Nzilani/Downloads/outputs.txt.txt','w') as file:
    file.write(upper_case)
    file.write(f"\nTotal number of words: {count_words}")

    
except:
   print("well,not found")
finally:
   print("Congratulations! You have created the new file.")   