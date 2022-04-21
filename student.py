file=open("myfile.txt",'r')
correct_answers=[]
for line in file:
    line=line.replace("\n","")
    correct_answers.append(line)
file.close()

# print(correct_answers)

def testQuiz():

    name=input("Please Enter your name:-  ")
    fname=input("Enter quiz answers file:-  ")

    file=open(fname,'r')

    answers=[]
    for line in file:
        line=line.replace("\n","")
        answers.append(line)

    correct_ans=[]
    incorrect_ans=[]

    for i in range(15):
    
        if answers[i]==correct_answers[i]:
            correct_ans.append(i)
        else:
            incorrect_ans.append(i)


    file.close()

    print(name ,'Quiz Results \n')
    print(f"correct answers {len(correct_ans)} \n")
    print(f"incorrect answers {len(incorrect_ans)} :( {str(incorrect_ans)[1:-1]} )")
    if len(correct_ans)>11:
        print("Student PASSED the Quiz \n")

    else:
        print("Student Failed the Quiz\n")

    x=input("\n Do you have another student (y/n):")
    if x=='y':
        testQuiz()
    else:
        pass

testQuiz()