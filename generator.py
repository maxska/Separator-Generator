import math


def get_maximum_spacing(line_comment, total_width, title):
    """ Returns the maximum possible spacing on each side of the title. """
    return math.floor((total_width - (len(line_comment) + len(title)))/2)


def get_side_separator_length(maximum_spacing, preferred_spacing):
    """ Returns the length that will be used for the side separator symbols 
    (maximum_spacing - preferred_spacing). """
    # print(f"maximum: {maximum_spacing}, preferred: {preferred_spacing}")

    assert maximum_spacing > preferred_spacing  # temporary solution
    return maximum_spacing - preferred_spacing


def is_uneven(number):
    """ Returns True if number is uneven. """
    return number/2 != number//2


def generate(
    line_comment,
    separator_symbol,
    total_width,
    rows,
    title,
    preferred_spacing
):
    """ Generates and returns a separator. """

    # one line for the above_and_below_separators:
    separator_line = (
        line_comment
        + separator_symbol * (total_width - len(line_comment))
        + "\n"
    )

    # above_and_below_separators is the line or lines of separator symbols that
    # will be placed above and below the title of the separator:
    above_and_below_separators = separator_line * math.floor(rows/2)

    # the maximum possible spacing that there's room for on both sides of the
    # title:
    maximum_spacing = get_maximum_spacing(line_comment, total_width, title)

    # maximum_spacing - preferred_spacing is the length that will be
    # used for the side separator symbols (and the rest will be used for just
    # spaces):
    side_separator_length = get_side_separator_length(
        maximum_spacing,
        preferred_spacing
    )

    # side_separator is the separator string containing multiple separator
    # symbols that will be placed on both sides of title:
    side_separator = separator_symbol * side_separator_length

    # side_spacing is the spacing that will be placed between the title
    # and the side_separator:
    side_spacing = " " * preferred_spacing

    # compensate with extra separator symbol if one of len(title) and
    # total_width is uneven and not the other:
    compensate_uneven_title = (
        separator_symbol
        if is_uneven(len(title)) and not is_uneven(total_width)
        else ""
    )

    compensate_uneven_length = (
        separator_symbol
        if is_uneven(total_width) and not is_uneven(len(title))
        else ""
    )

    result = ""
    result += above_and_below_separators
    result += f"{line_comment}{side_separator}{side_spacing}"
    result += f"{title}{side_spacing}{side_separator}"
    result += f"{compensate_uneven_title}{compensate_uneven_length}\n"
    result += above_and_below_separators
    return result
