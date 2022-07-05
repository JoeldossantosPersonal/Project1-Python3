'''''
  * Class: 44-141 Computer Programming I
  * Author:  Joel Dos Santos Iraha
  *Description: The main area of the program will open the text file with the table of student info, prompt the user for a last name, and print a message returning all info to the user regarding the student.
      * Due: November 3rd, 2021
      * I pledge that I have completed the programming assignment independently.
      * I have not copied the code from a student or any source.
      * I have not given my code to any other student and will not share this code with anyone under any circumstances.
'''''

# open file
#create funtions
def fileReader(lastName, fileInput):      #function to search name, lastName
    studentInfo = fileInput.split()       #using split method to divide strings by elements in a list and convert everything to lowercase
    name = lastName.lower()
    last = studentInfo[1]                 #asigning position in list
    last = last.lower()
    if name==last:                        
        return studentInfo
    else:
        return "False"

def firstName(studentInfo):
    firstName= studentInfo[1]            #asigning position in list and returning variable created. Same process for other functions
    return firstName


def lastName(studentInfo):
    lastName= studentInfo[0]
    return lastName
    
def gpa(studentInfo):
    gpa = studentInfo[2]
    return gpa
    
def creditHours(studentInfo):
    creditos = studentInfo[3]
    return creditos

def mealPlan(studentInfo):
    meal_plan = studentInfo[4]
    return meal_plan

def advisor(studentInfo):
    advisor = studentInfo[5]
    return advisor

def enrollmentSubmit(studentInfo):
    enrollment=studentInfo[6]
    return enrollment



# main program
print("Welcome to the Enrollment Center!\n")                              
name = input("Please enter a last name or enter 0 to stop program: ")        #gather input from user and storing in a varibale called name

                                                             
while (name != "0"):                                                         #creating nested loop and creating count=0
    file = open("studentInfo.txt", "r")                                      #open text file                    
    count=0
    for i in file:
        file = open("studentInfo.txt", "r")                                  #for loop ro read each student in file 
        readingFile = fileReader(name, i)                                    
        if (readingFile != "False"):                                         #In case student is found (!= "False"), execute following code 
            fn=firstName(readingFile)                                        #Calling functions and assigning them to the return value
            ln=lastName(readingFile)
            g=gpa(readingFile)
            ch=creditHours(readingFile)
            mp=mealPlan(readingFile)
            a=advisor(readingFile)
            es=enrollmentSubmit(readingFile)
            print(ln, fn + " has a " + g + " gpa")                          #printing results
            print("Credit hours: ", ch)
            print("Meal Plan", mp)
            print(ln + "'s advisor is " + a)
            print(ln + " has enrolled")
            file.close()                                                    #close file 
            if (es == "True"):                                              #Check if student has or hasn't enrolled
                print(ln, "has enrolled\n")
            else:
                print(ln, "has not enrolled\n")
            count+=1
            
    if (count==0):                                                         #if student is not found, print following message:
        print("Student not found\n")
    name = input("Please enter a last name or enter 0 to stop program: ")  #gather more inut from user
                                                               
print()
print("Thanks for using Enrollment Center Application!")                   #printing ending prompt
        
           
  
    

        
        
        
        