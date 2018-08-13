

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



def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3