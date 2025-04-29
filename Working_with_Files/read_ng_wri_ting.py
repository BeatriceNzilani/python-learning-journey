# opening, reading, writing, or editing files

""" 
r- read files 
w -overwrite and if the file doesn"t exist it creates the file
a -append ( used to write on the file without deleting theeisting data)
t-text format
b-binary format
x-create a file and returns an error if the file exists


"""
with open('C:/Users/Nzilani/Downloads/Salaries.csv','rt') as file:
    content=file.read()
    print(content)

with open('C:/Users/Nzilani/Downloads/Salaries.csv','rt') as file:
    line_one =file.readline()# reads line by line
    print(line_one)


with open('C:/Users/Nzilani/Downloads/Salaries.csv','rt') as file:
    data=file.readlines()# reads all the lines and returns them as a list
    print(data)

with open('C:/Users/Nzilani/Downloads/Salaries.csv','rb') as file:
    bin=file.read()
    print(bin)


# for write if the folder is not created it creates another folder
with open('C:/Users/Nzilani/Downloads/output.txt','w') as file:
    write_content=file.write("Hello world!")# this will display the number of characters in the and also write
    print(write_content) 

with open('C:/Users/Nzilani/Downloads/output.txt','w') as file:
    file.write("Hello ,world!")#this will write directly without displaying number of characters 

# for append it writed on the document without having to delete the previous text
with open('C:/Users/Nzilani/Downloads/output.txt','a') as file:
    file.write("Hello world!")

file =open('C:/Users/Nzilani/Downloads/output.txt','rt')
print(file.read())



file =open('C:/Users/Nzilani/Downloads/output.txt','w')
print(file.write("Hi!"))


# creating a new file
file =open('C:/Users/Nzilani/Downloads/out.txt','x')
