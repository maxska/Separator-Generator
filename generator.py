import math


def get_maximum_spacing(line_comment, total_width, title):
	""" Returns the maximum possible spacing on each side of the title. """
	return math.floor((total_width - (len(line_comment) + len(title)))/2)


def get_side_separator_length(maximum_spacing, preferred_spacing):
	""" Returns the spacing that is actually used. """
	# print(f"maximum: {maximum_spacing}, preferred: {preferred_spacing}")
	assert maximum_spacing > preferred_spacing  # fix later

	return maximum_spacing - preferred_spacing


def generate(line_comment, separator, total_width, rows, title, 
			 preferred_spacing):
	""" Generates and returns a separator. """

	separator_line = line_comment + "".join(
		[separator for elem in range(total_width - len(line_comment))]
	) + "\n"

	above_and_below_separators = "".join(
		[separator_line for elem in range(math.ceil(rows/2))]
	)

	maximum_spacing = get_maximum_spacing(line_comment, total_width, title)

	side_separator_length = get_side_separator_length(
		maximum_spacing, 
		preferred_spacing
	)

	side_separator = separator * side_separator_length
	side_spacing = " " * preferred_spacing


	result = ""
	result += above_and_below_separators
	result += f"{line_comment}{side_separator}{side_spacing}"
	result += f"{title}{side_spacing}{side_separator}\n"
	result += above_and_below_separators	
	return result


print(
	generate("//", "#", 80, 3, "The title", 5)
)