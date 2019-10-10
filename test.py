# task 1
def sum_list_items(arr):
	"""Add the items of a list and return the result"""
	# Only change code below this line
	return sum(arr)
	# Only change code above this line


# task 2

def get_unique_items(arr):
	"""Return unique items from a list"""
	# Only change code below this line
	setArr = set(arr)
	
	
	return list(setArr)
	# Only change code above this line

# task 3

def is_palindrome(s):
	"""A string is said to be palindrome if reverse of the string is same as string. 
	Return True if s is palindrome
	"""
	# Only change code below this line
	if s == s[::-1] or s == "":
	    return True
	else: 
	    return False
	# Only change code above this line

	# task 4

	def get_3_lagest(l):
    """Find 3 the largest items from a list"""
    # Only change code below this line
    uniq = set(l)
    uniq = sorted(uniq)
    return uniq[-3:]
           
    # Only change code above this line

	# task 5

	def count_words(text):
    """Find quantities of each unique word in a text.
    Return list of tuples (word, count) sorted by counts"""
    # Only change code below this line
    text = text.split(' ')
    newtext = []
    for i in text:
        if '\n' in i:
            i = i.split('\n')
            newtext.append(i[0])
            newtext.append(i[1])
        else:
            newtext.append(i)
    newList = {}
    for i in newtext:
        if i:
            # i = i.replace('.', '').replace(',', '')
            # i = i.replace('\n', ' ')
            if i in newList:
                newList[i] += 1
            else:
                newList[i] = 1
    ret = [(key, v) for key, v in newList.items()]
    ret = sorted(ret, key=lambda kv: kv[1], reverse=True)
    return ret
    # Only change code above this line