day =2
match day:
    case 1:
        print("Moday")
    case 2:
        print("Tuesday")
    case _:
        print("Guess the day")        

month =9
day =3
match day:
    case 1|2|3|4|5 if month== 4:
        print ("a week day in April")
    case 6|7  if month ==5:
        print(" a weekend in March")  
    case _:
        print("Guess the day")     