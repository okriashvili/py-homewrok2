# დავალება 1
# ჰიპოტენუზა
A = float(input("შეიყვანეთ სამკუხედის პირველი კათეტის სიგრძე"))
B = float(input("შეიყვანეთ სამკუხედის მეორე კათეტის სიგრძე"))
C = (A**2 + B**2) **0.5
print("სამკუთხედის ჰიპოტენუზის სიგრძე არის ", int(C), "სანტიმეტრი")
#ფართობი:
S = (A * B) *0.5
print("მართკუთხედის ფართობია",  int(S), "სანტიმეტრი")



# დავალება 2:
seconds = float(input("შეიყავენთ წამების რაოდენობა: "))
# საათი
secondsIntoHour = seconds // 3600
# წუთი
restMinutes = seconds % 3600
secondsIntoMinutes = restMinutes // 60
# წამი
restSeconds = seconds % 60
# ფორმულა
print(int(seconds), "წამი არის:", int(secondsIntoHour), "საათი",",", int(secondsIntoMinutes), "წუთი და", int(restSeconds), "წამი")