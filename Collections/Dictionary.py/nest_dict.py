myfamily= {
     
     "baby1":{
         "name":"yuo",
         "age":20
     },

     "baby2":{
         "name":"yu",
         "age":19
     },
     "baby3":{
         "name":"y",
         "age":18
     }
     
    
}
print(myfamily)


myfriends ={
    "friend_1":{
        "Name":"Morris",
        "Age":20,
        "favourite-color":"Grey"
    },

    "friend_2":{
        "Name":"Brenda",
        "Age":21,
        "favourite-color":"Pink"
    },
    "friend_3":{
        "Name":"Beatrice",
        "Age":20,
        "favourite-color":"Blue"
    },
    "friend_4":{
        "Name":"Peace",
        "Age":20,
        "favourite-color":"Pink"

    }
    
}

for x,obj in myfriends.items():
    print(x)
    for y in obj:
        print(y,":",obj[y])


