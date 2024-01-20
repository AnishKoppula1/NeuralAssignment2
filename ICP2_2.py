sentence = input("Enter any Sentence : ")
result = ""
for i in range(0,len(sentence)):
    if(i%2 ==0):
        result += sentence[i]
print(result)