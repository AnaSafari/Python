def extendList(val, list=[]):
    list.append(val)
    return list

list1 = extendList(5)
list2 = extendList(249,[])
list3 = extendList('ana')

print "list1 = %s" % list1
print "list2 = %s" % list2
print "list3 = %s" % list3


#### output ####
# list1 = [5, 'ana']
# list2 = [249]
# list3 = [5, 'ana']

# The new default list is created only once 
# when the function is defined, 
# and that same list is then used subsequently 
# whenever extendList is invoked without a list argument 
# being specified. This is because expressions in default 
# arguments are calculated when the function is defined, 
# not when it is called.
# list1 and list3 are therefore operating on the same default list, 
# whereas list2 is operating on a separate list 
# that it created (by passing its own empty list 
# as the value for the list parameter).


def modifiedExtendList (val, mlist=None):
	if mlist is None:
		mlist = []
	mlist.append(val)
	return mlist

mlist1 = modifiedExtendList(50)
mlist2 = modifiedExtendList(150,[])
mlist3 = modifiedExtendList('anahita')

print "mlist1 = %s" % mlist1
print "mlist2 = %s" % mlist2
print "mlist3 = %s" % mlist3

### output ###
# mlist1 = [50]
# mlist2 = [150]
# mlist3 = ['anahita']