from Question import Question
question_prompts = [
    "What colour are apples?\n(a)Red/Green \n(b)Purple \n(c)Orange\n",
    "What colour are bananas?\n(a)Mauve \n(b)Blue \n(c)Yellow\n",
    "What colour are strawberries?\n(a)Green \n(b)Purple \n(c)Orange\n"
    ]

questions = [
        Question(question_prompts[0],"a"),
        Question(question_prompts[1],"c"),
        Question(question_prompts[2],"b")
    ]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got "+str(score)+"/"+str(len(question_prompts))+" correctly")
   
run_test(questions)     