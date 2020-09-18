import calendar as cl

a = input("What is your year of birth?\n")
b = input("Enter your month of birth:\nFor January enter 1\n    February    2\n    March       3\n    April       4\n    May         5\n    June        6\n    July        7\n    August      8\n    September   9\n    October    10\n    November   11\n    December   12\n")
c = input("Enter the date on which you were born(1-30)\n")
x = cl.weekday(year=int(a), month=int(b), day=int(c)) 

if int(c) == 1:
    d = c +"st"
    
elif int(c)==2:
    d = c +"nd"
    
elif int(c)==3:
    d = c +"rd"
    
elif int(c) >= 4 and int(c) <= 20:
    d = c +"th"
    
elif int(c)==21:
    d = c +"st"
    
elif int(c) == 22:
    d = c +"nd"
    
elif int(c) == 23:
    d = c +"rd"
    
elif int(c) == 31:
    d = c +"st"
    
else:
    d = c+"th"

if int(b) == 1:
       m = "January"
       
elif int(b) == 2:
        m = "February"
        
elif int(b) == 3:
        m = "March"
        
elif int(b) == 4:
        m = "April"
        
elif int(b) == 5:
        m = "May"
        
elif int(b) == 6:
        m = "June"
        
elif int(b) == 7:
        m = "July"
        
elif int(b) == 8:
        m = "August"
        
elif int(b) == 9:
        m = "September"
        
elif int(b) == 10:
        m = "October"
        
elif int(b) == 11:
     m = "November"
     
else:
    m = "December"

if x == 0:
    y = "Monday"
    
elif x == 1:
    y = "Tuesday"
    
elif x == 2:
    y = "Wednesday"
    
elif x == 3:
    y = "Thursday"
    
elif x == 4:
    y = "Friday"
    
elif x == 5:
    y = "Saturday"
    
else:
    y = "Sunday"

print("you were born on "+y+" "+d+", "+m+" "+a)
