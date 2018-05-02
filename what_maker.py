#Function that makes string of the word "what", repeated a user-chosen number of times
def what_maker():
	print "How many whats would you  like in your string?"
	what_number = ''
	while what_number is not int:
		user_input = raw_input(">") #FIX ME
		try:
			int(user_input)
			what_number = int(user_input)
			break
		except ValueError:
			print "Please enter a valid integer"
	what_list = [] #Defines empty list to hold "what" strings
	while len(what_list) < what_number:
		what_list.append("what ")
	what_list.append("?")
	what_string = ''.join(what_list)
	return what_string

print what_maker()