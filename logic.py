
def verify_string(input, name, max_length):
	if len(input) <= max_length:
		return input
	else:
		return (False, f"Error: {name} needs to be shorter than {max_length}.")


def verify_int(input, name, max_size):
	try:
		number = int(input)
		
		if number <= max_size:
			return number
		else:
			return (False, 
					f"Error: {name} needs to be smaller than {max_size}.")

	except ValueError:
		return (False, f"Error: {name} needs to be an integer value.")

	
def is_error(potential_error):
	return isinstance(potential_error, tuple) and potential_error[0] == False
	