# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    row = 0
    square = ''
    while row < n:
        if row == 0 or row == n - 1:
            square += '*' * n
        else:
            square +='*' + ' ' * (n - 2) + '*'
        if row < n - 1:
            square += '\n'
        row += 1
    return square


# 1
# 12
# 123
# 1234
def number_pattern(n):
    row = 1
    number_pattern = ''
    while row <= n:
        col = 1
        while col <= row:
            number_pattern += str(col)
            col += 1
        if row < n:
            number_pattern += '\n'
        row += 1
    return number_pattern

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    row = 0
    pyramid = ''
    while row < n:
        pyramid += ' ' * (n - row - 1) + '*' * (2 * row + 1) + '\n'
        row += 1
    return pyramid.rstrip()