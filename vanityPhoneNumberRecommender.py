import os
os.chdir("C:/Users/HP/OneDrive/Desktop/NewFolder")

#taking desired phone number as input 
number = input("Enter a Phone number:")
#converting input string into a list
phoneNo = list(number)

#calculating length of phone number
wordLength = len(phoneNo)

#assigning aplphabets to corresponding numbers
mapping = {'2':'abc','3':'def','4':'ghi', '5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}

word = []
for digit in phoneNo:
    if digit in mapping:
        word.append(mapping[digit])
print(word)

file_path = os.path.abspath("sample_dictionary.txt")

with open(file_path, "r") as file:
    file_contents = file.read()


lines = file_contents.split("\n")
result = [item for item in lines if len(item)== wordLength]
print(result)


final = []
checkWord = 0
for i in result:
     for j in range(0, wordLength):
         if i[j] in word[j]:
             checkWord = 1
         else:
            checkWord = 0
            break
     if checkWord == 1:
         final.append(i)
print(final)

    





