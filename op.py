#The marks are considered on the basis of marks (Bhavans Vidya Mandir Elamakkara 2019-2020) of Half Yearly Examination 

#welcome
print("welcome to class 8 exam helper")
print("pls enter the correct answers to run this program nice and smooth!!")

#name

name=input("Enter your name")


#english marks(int)

english=float(input("Enter your english marks in decimals"))
if english>25 and english<30:
  print("you are doing well")

elif english==30:
  print("full!!!!!!")

elif english<25:
  print("be there in the class")

else:
    print("in english you are not bad but not good please call anjana miss(9446337809)")

#maths marks(int)

maths=float(input("enter your maths marks in decimals"))
if maths>25 and maths<30:
  print("you are doing well")

elif maths==30:
    print("full")

elif maths<25:
  print("be there in the class")

else:
  print("in maths you are not bad but not good please call siji miss(9495301554)")

#malayalam marks

mal=float(input("enter your malayalam marks in decimals,type 0 if u choosed sanskrit "))
if mal>25 and mal<30:
  print("you are doing well")

elif mal==30:
  print("full")

elif mal==0:
  print("ok carry ahead")

elif mal<25:
  print("be there in the class")

else:
  print("poor")


#scoial marks

social=float(input("enter your maths marks in decimals"))
if social>25 and social<30:
  print("you are doing well")

elif social==30:
    print("full")

elif social<25:
  print("be there in the class")

else:
  print("in social you are not bad but not good please call vibitha miss(9746193923)")


#sanskrit

sanskrit=float(input("enter your sanskrit marks in decimals . type 0 if u choosed malayalam"))

if sanskrit>25 and sanskrit<30:
  print("good")
          
elif sanskrit==30:
  print("full")

elif sanskrit==0:
  print("ok , carry ahead")

elif sanskrit<25:
  print("be there in the class")

      
else:
  print("in sanskrit you are not bad but not good please call MMMMM miss(xxxxxxx)")


#chemistry marks (int)

chemistry=float(input("enter your chemistry marks in decimals"))
if chemistry>6 and chemistry<10:
  print("good")

elif chemistry==10:
  print("full")

elif chemistry<6:
  print("be there in the class")
  
else:
  print(" be focused!!!")

#bio marks (int)

biology=float(input("enter your bio marks"))
if biology>6 and biology<10:
  print("goood")

elif biology==10:
  print("good")

elif biology<6:
  print("be there in the class")
  
else:
  print(" be present in all class!!!")

#physics marks(int)

physics=float(input("enter your physics marks"))
if physics>6 and pysics<10:
  print("i noticed ur a good")

elif physics==10:
  print("full")

elif physics<6:
  print("be there in the class")

else:
  print("do homw work regularly")

#total science marks
total_science =physics+chemistry+biology
print("your total marks in science is",total_science)

#total marks in the exam 

total_marks_in_exam=total_science+physics+chemistry+biology
print("your total marks in the exam is",total_marks_in_exam)

#grading and printing it

if total_marks_in_exam <181 and total_marks_in_exam > 169:
  print("A1 is your grade")

elif total_marks_in_exam >159 and total_marks_in_exam <161:
  print("A2 is yor grade")

elif total_marks_in_exam >130 and total_marks_in_exam < 150:
  print("B1 is your grade")

elif total_marks_in_exam>115 and total_marks_in_exam<130:
  print("B2 is your grade")
  
elif total_marks_in_exam<115:
  print("you are failed")


#percentage

per=total_marks_in_exam/6*100

print(per)

#compining

final= name, per ,english, maths, mal , social , sanskrit , total_science, total_marks_in_exam

#saving the data 

file = open("marks.txt", "w")
file.write("%s = %s\n" %(" The  data is being  saved in this format : name , per ,english , maths,mal,social,sanskrit,total marks in science , total marks in the exam.", final))

file.close()

#instruction

print("pls chnage ur file location to use this program next time")
print("your data wll be saved in a text file named 'marks' where u have saved this script")


#thanks

print("Your response is saved. Thank you for using this")

#to finish

input("type anything to finish this program")





















