def reversedict(d):
	"""Reverses a Dictionary so that the values are the keys and the keys are the values"""
	reverse = zip(d.values(), d.keys())
	new_dict = dict(reverse)
	return new_dict