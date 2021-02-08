import math

def generate(line_comment, separator, total_width, rows, title, 
			preferred_spacing):

	print(line_comment)

	separator_line = line_comment + "".join(
		[separator for elem in range(total_width - len(line_comment))]
	) + "\n"
	above_below_symbols = "".join(
		[separator_line for elem in range(math.ceil(rows/2))]
	)

	result = ""
	result += above_below_symbols
	result += line_comment + title + "\n"
	result += above_below_symbols	
	return result


print(
	generate("//", "#", 80, 3, "The title", 30)
)