

registaredList = []
def register(decorator):
	registaredList.append(decorator)
	# return decorator

@register
def foo():
	return 10

@register
def bar():
	return 50


answers = []
for func in registaredList:   ### The output is [10,50]
	answers.append(func())
	


class Registary(object):
	def __init__(self):
		self.__functions  = []

	def register(self,decorated):
		self._functions.append(decorated)
    	# return decorated

	def run_all(self, *args, **kwargs):
		return_values = []    
		for func in self._functions:
			return_values.append(func(*args, **kwargs))
		# return return_values



