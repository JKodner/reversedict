def reversedict(d):
	"""Reverses a Dictionary so that the values are the keys and the keys are the values"""
	unhashables = [{}]
	reverse = zip(d.values(), d.keys())
	for i in reverse:
		val = i[0]
		try: 
			hash(val)
		except TypeError:
			unhashables[0].update({i[1]: i[0]})
			reverse.remove(i)
	newdict = dict(reverse)
	newdict.update({"unhashable_types": unhashables})
	return newdict

