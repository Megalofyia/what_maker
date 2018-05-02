def what_maker(): #Function that makes string of the word "what", repeated a user-chosen number of times
	
	print "How many whats would you  like in your string?"
	
	what_number = '' #Create blank variable to hold number of "what"s
	
	while what_number is not int: #Loop until the user enters a valid integer
		user_input = raw_input(">") #Take user's input
		
		try:
			int(user_input) #Check if the user's input is an integer
			what_number = int(user_input) #If it is, set the what_number variable equak to the integer the user entered
			break #Leave the input loop
		
		except ValueError:
			print "Please enter a valid integer" #Ask the user to try again
	
	what_list = [] #Defines empty list to hold "what" strings
	
	while len(what_list) < what_number: #Loop through the following code until the number of "what"s in the list number the user entered
		what_list.append("what ") #Add an entry to the list, containing "what"
	
	what_list.append("?") #Add a question mark to the end of the list #FIX ME
	
	what_string = ''.join(what_list) #Turn the list into a string, ready to be printed
	
	return what_string

print what_maker() #Run the function, and print the result to the user
