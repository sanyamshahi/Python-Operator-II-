math=int(input("enter your marks in math"))
science=int(input("enter your marks in science"))
english=int(input("enter your marks in english"))
average=(math+science+english)//3
print(f"your average is {average}")
if average>90 and average<100:
 print("A")

elif average>80 and average<90:
 print("B")

elif average>70 and average<80:
 print("C")

elif average>60 and average<70:
 print("d")

elif average>50 and average<60:
 print("E")

elif average>100:
 print("invalid input")

else:
 print("you have failed")