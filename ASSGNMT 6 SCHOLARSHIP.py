
firstname = input("Enter firstname: ")
lastname = input("Enter lastname: ")
studentID = input("Enter your student ID:")
mail_address = input("Enter your mail Address:")
continent = input("Enter Continent:")
student_email = input("Enter your email address:")
phonenumber = input("Enter your phone number:")

if continent == "Africa":
    print ("yes" , "The continent is Africa")
else:
   exit("you are not qulified.")
def tests():
    # Python program to perform Addition of zoom scores
    Test1 = int(input("Enter First test : "))
    Test2 = int(input("Enter Second test : "))

    print("Enter any of between [0-100] for a each call:")
    if Test1 >= 0 and Test1 <= 100 and (Test2 >= 0 and Test2 <= 100):
        result4 = Test1 + Test2
        print("Total tests score!")
        print(Test1, Test2, ":", result4)

    else:
        result4 = 0
    return result4


def quizes():
    # Python program to perform Addition of zoom scores
    quizes1 = int(input("Enter First quiz : "))
    quizes2 = int(input("Enter Second quiz : "))
    quizes3 = int(input("Enter 3rd quiz : "))

    print("Enter any of between [0-100] for a each quiz:")
    if quizes1 >= 0 and quizes1 <= 100 and (quizes2 >= 0 and quizes2 <= 100) and (quizes3 >= 0 and quizes3 <= 100):
        result3 = quizes1 + quizes2 + quizes3
        print("Total quizes score!")
        print(quizes1, quizes2, quizes3, ":", result3)

    else:
        result3 = 0
    return result3


def homework():
    # Python program to perform Addition of zoom scores
    homework1 = int(input("Enter First homework : "))
    homework2 = int(input("Enter Second homework : "))
    homework3 = int(input("Enter 3rd homework : "))

    print("Enter any of between [0-10] for a each call:")
    if homework1 >= 0 and homework1 <= 10 and (homework2 >= 0 and homework2 <= 10) and (
            homework3 >= 0 and homework3 <= 10):
        result1 = homework1 + homework2 + homework3
        print("Total homework score!")
        print(homework1, homework2, homework3, ":", result1)

    else:
        result1 = 0
    return result1


def zoomcalls():
    # Python program to perform Addition of zoom scores
    zoom1 = int(input("Enter First Zoon Call: "))
    zoom2 = int(input("Enter Second Zoon Call: "))
    zoom3 = int(input("Enter 3rd Zoon Call: "))

    print("Enter any of between [0-9] for a each call:")
    if zoom1 >= 0 and zoom1 <= 9 and (zoom2 >= 0 and zoom2 <= 9) and (zoom3 >= 0 and zoom3 <= 9):
        result = zoom1 + zoom2 + zoom3
        print("Total zoom score!")
        print(zoom1, zoom2, zoom3, ":", result)

    else:
        result = 0
    return result


def main():
    result4 = tests()
    result3 = quizes()
    result = zoomcalls()
    result1 = homework()
    average = ((result4) + (result3)) / 5
    sum = result + result1
    print("total homeworks and zooms :", sum)


    print("average tests and quizes:", average)
    if continent == Africa and gender== female and average >= 76:
        print("qualified")
    else:
        print('unqualfied')
    return average


main()


print("First Name" ":" , firstname)
print("Last Name" ":" , lastname)
print("Student ID number" ":" , studentID)
print("mail Address" ":" , mail_address)
print("Email" ":" , student_email)
print("Phone Number" ":" , phonenumber)
print("Continent" ":",Continent)
if average >= 76 and  gender =="Female" or gender =="f" or gender=="F":
    print('Congratulations - You qualify for the Scholarship')
else:
    print('Sorry -  You did not qualify for the Scholarship')

if average>=80 and gender =="Male" or gender =="m" or gender=="M":
    print('You qualify for the Scholarship')
else:
    print('Sorry -  You did not qualify for the Scholarship')
