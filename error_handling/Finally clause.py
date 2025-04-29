try:
    with open('C:/Users/Nzilani/Downloads/output.txt','r') as file:
        data=file.read() 
        print(data)
except FileNotFoundError:
    print("File not found")
finally:
   print("nice  to see you")




