import random, decimal
import operator
ops = {"+": operator.add, "-": operator.sub, "/": operator.truediv,
"*": operator.mul} # this is so that strings are converted to operators
score_counter = 0 # overall score of the user. Modified by counter(t_or_f)
answers_list = [] # data for sending it to the Results.txt file


# generates a random number with with 2 d.p.
def random_number():
    return float(random.randint(1, 10000)/10)


# generates a random operation in form of a string
def random_ops():
    t = random.randint(1, 4)

    if t == 1:
        oper = "+"
    elif t == 2:
        oper = "-"
    elif t == 3:
        oper = "/"
    elif t == 4:
        oper = "*"
    else:
        pass

    return oper


# changes the score counter according to the answer. Takes a True or False as an input
def counter(t_or_f):
    global score_counter

    if t_or_f == True:
        score_counter += 1
    else:
        pass


# # supposed to send the result to the file
# def send_to_file(num, result):
#     result_file = open("Results.txt", "w")
#     sentence = "{}, {}".format(num, result)
#     result_file.write(sentence)
#     result_file.close()


# prints a problem that has to be solved
def new_problem():
    num1 = random_number() # first random number
    num2 = random_number() # second random number
    calc = random_ops() # random operation
    print(num1, calc, num2, "= ") # sticks everything together to form a random problem

 # if a user does not enter anything
    try:
        answer = float(input("--> ")) # asks the user for an answer
    except ValueError:
        answer = 0

# round() is to round off the recurring decimals that may come up while dividing
    if answer == round(ops[calc](num1, num2), 2): # ops[calc](num1, num2) is how calc, which is a string, is converted into an operation
        counter(True)
    elif answer != round(ops[calc](num1, num2), 2):
        counter(False)

    sentence = "{} {} {} = {}, score: {} \n".format(num1, calc, num2, answer, score_counter) # stciks togther the user's answer and score
    global answers_list # modifying a list outside the function
    answers_list.append(sentence) # appending the sticked sentence to the list which will be later sent to a file
