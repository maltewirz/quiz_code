#-------# Game content
quiz_easy = "--1-- often! For every small piece of code you write, --1-- it immediately before moving on. Try to write the smallest testable --2-- you can manage for each step; it's good practice both for minimizing debugging --3-- and for reusing --2-- later! Thank --4--!"
quiz_medium = "When debugging a --1--, it is very useful to check the --2-- of variables at various points in the execution of the --1--. Scattering print statements to find out what the --3-- of selected variables are will show you what the variable is at specific points in the --1--. This can be used to compare what you think the variable --2--s should be with what they actually are, allowing you to find --4--s."
quiz_hard = "Procedural --1-- is key to mastering programming: we break the --2-- down into small little procedures that --3-- one after the other. Outlining our code or writing pseudocode will enable us to organize our code in a high-level way so we can keep track of the bigger --4-- of our program."

blank_spaces = ["--1--", "--2--", "--3--", "--4--"]
answers_easy = ["test", "code", "time", "you"]
answers_medium = ["program","state","values","error"]
answers_hard = ["thinking","problem","execute","picture"]

#-------# Playing game
def play_game(quiz, blank_spaces, answers):
  for e in range(len(blank_spaces)):
    print quiz
    print "\n" "What's the answer to " + blank_spaces[e] + ": " "\n"
    user_input = raw_input("Enter here: ").lower()
    count_tries = 5
    while user_input != answers[e]:
      print "\n" "False. You have " + str(count_tries) + " tries left!" "\n"
      count_tries -= 1
      if count_tries <=0:
        print "\n" "Game Over" "\n"
        exit(0)
      user_input = raw_input("Enter here: ")                             
    if user_input in answers[e]:
      print "\n" "Correct!" "\n"
      quiz = quiz.replace(blank_spaces[e], answers[e])
  print "\n" "You won" "\n" + "\n" + quiz


#-------# Selecting Difficulty
def user_select():
	print "Please select a game difficulty by typing it in! " "\n"
	difficulty = raw_input("Possible choices include easy, medium and hard: ")
	while difficulty not in ("easy", "medium", "hard"):
		print "Please, choose 'easy', 'medium' or 'hard'!"
		difficulty = raw_input("Possible choices include easy, medium and hard: ")
	if difficulty == "easy":
	  print "\n" "You've chosen easy" "\n"
	  play_game(quiz_easy, blank_spaces, answers_easy)
	if difficulty == "medium":
		print "\n" "You've chosen medium" "\n"
		play_game(quiz_medium, blank_spaces, answers_medium)
	if difficulty == "hard":
		print "\n" "You've choosen hard" "\n"
		play_game(quiz_hard, blank_spaces, answers_hard)

user_select()


