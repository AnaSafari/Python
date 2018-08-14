# Nested Function: a function defined inside another function 
# 				   - Can access the variables of the enclosing scope. 
# 				     In python, they are only readonly. 
# 				   - Use the "nonlocal" keyword explicitly with these variables 
# 				     in order to modify them.

def printMyname(name):
	'''This is the enclosing function'''
	def printFunction():
		'''This is the nested function'''
		name = "default name"
		print(name)

	printFunction()
	print(name)

printMyname("Anahita")


####     output   ###
#####################
#### default name ###
#### Anahita      ###

#Now we use a nonocal variable:

def printMyID(name):
	'''This is the enclosing function'''
	def printFunction():
		'''This is the nested function'''
		nonlocal name
		name = "default name"
		print(name)

	printFunction()
	print(name)

printMyname("Anahita")

####     output   ###
#####################
#### default name ###
#### default name ###