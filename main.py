import functions


# welcome message
print("""\nHello. This is a 20 question test that will measure your ability to
accurately add, subtract and divide decimals up to two decimal places. Any
answer that has more than 2 decimal points, must be rounded off.""")
print("\n")

# generates 20 different problems
for i in range(1,21):
    print("Problem {}".format(i))
    functions.new_problem()
    print("Current score:", functions.score_counter, "\n")

# make variables more readible
num_score = functions.score_counter
percent_score = int(functions.score_counter / 20 * 100)

# output to user
print("""Your overall score is {} out of 20. That is a percentage of {}%, which
is your grade for the test.""".format(num_score, percent_score))

# sends the user's answers, the computer generated problems and the score count to a file
with open("Results.txt", "w") as result_file:
    result_file.writelines(functions.answers_list)
    result_file.write("\nOverall score: {} out of 20.".format(num_score))
    result_file.write("\nPercentage as a score: {}%".format(percent_score))
