front=" Library System"
print(front)
firstbook="press 1 for 101 book information"
secondbook="press 2 for 102 book information"
thirdbook="press 3 for 103 book information"
fourthbook="press 4 for 104 book information"
fifthbook="press 5 for 105 book information"



def start():
    print(firstbook)
    print(secondbook)
    print(thirdbook)
    print(fourthbook)
    print(fifthbook)
    main()
   
book101 = ("Title=The Hundred-Page Machine Learning Book" 
       "\n Author=Andriy Burkov"
        "\n Price=$35"
         "\n Language=English"
          "\n Rating=4.5/5" ) 
   
book102 = ("Title=Python for Data Analysis" 
       "\n Author=Wes McKinney"
        "\n Price=$45"
         "\n Language=English"
          "\n Rating= 4.7/5" ) 
book103 = ("Title=torytelling with Data: A Data Visualization Guide for Business Professionals" 
       "\n Author=Cole Nussbaumer Knaflic"
        "\n Price=$30"
         "\n Language=English"
          "\n Rating=4.5/5" ) 
book104 = ("Title=Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy" 
       "\n Author=Cathy O'Neil"
        "\n Price=$16"
         "\n Language=English"
          "\n Rating=4.4/5" ) 
         
book105 = ("Title=Data Science for Business: What You Need to Know About Data Mining and Data-Analytic Thinking" 
       "\n Author=Foster Provost and Tom Fawcett"
        "\n Price=$40"
         "\n Language=English" 
         "\n Rating=4.6/5") 

def main():
    user = int(input("Enter the number for book information: "))
        
    if (user == 1):
            print(book101)
    elif (user == 2):
            print(book102)
    elif (user == 3):
            print(book103)
    elif (user == 4):
            print(book104)
    elif (user == 5):
            print(book105)
    else:
            print("Invalid input. Thanks for visiting.")


    again=int(input("Do you want to continue \n if yes press 0 \n if exit press 9\n"))
    if again==0:
        start()
    elif(again==9):
        print("Thanks for visiting the Skill Circle Library System")
    else:
        print("Invalid input ")
start()

       
  
