def reversedict(d):
	"""Reverses a Dictionary so that the values are the keys and the keys are the values"""
	unhashables = {}
	non_duplicates = {}
	duplicates = {}
	reverse = zip(d.values(), d.keys())
	for i in reverse:
		val = i[0]
		try: 
			hash(val)
		except TypeError:
			unhashables.update({i[1]: i[0]})
			reverse.remove(i)
			continue
		if val not in non_duplicates.keys():
			non_duplicates.update({i[0]: i[1]})
		else:
			duplicates.update({i[1]: i[0]})
	non_duplicates.update({"unhashable_types": unhashables})
	non_duplicates.update({"returned_duplicates": duplicates})
	return non_duplicates

