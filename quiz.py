#定義 class
class question:
    def __init__(self,description, answer):
        self.description = description
        self.answer = answer


# create the list of questions 
test =[
"1+1 =? \n (A)2 \n (B)22 \n (C) 1 \n\n ",
"2+5 =? \n (A)25 \n (B)7 \n (C) 14 \n\n",
"7+7 =? \n (A)0 \n (B)49 \n (C) 14 \n\n "
]


# 將test資料賦予在QS變數上,模組class的question
QS =[
    question(test[0],"A"), # question(description, answer) 
    question(test[1],"B"), # 把test資料第Ｏ筆代入
    question(test[2],"C"),
]


def runTest(X):
    score = 0 #變數，初始值為0
    for question in QS:
        answer = input(question.description)
        if answer == question.answer: #class中的answer
            score +=100
    

    print ("Your score is" + " " +str(score))


runTest(QS)