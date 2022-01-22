# import package

import syllapy

# input three lines

line_one = input('enter line one: ')
line_two = input('enter line two: ')
line_three = input('enter line three: ')

# calculate syllables

syllables_line_one = syllapy.count(line_one)
syllables_line_two = syllapy.count(line_two)
syllables_line_three = syllapy.count(line_three)

# merge syllable count

total_syllables = syllables_line_one + syllables_line_two + syllables_line_three

# return haiku true or false

if total_syllables == 17:
  print(f'your haiku poem has {total_syllables} syllables')
else:
  print(f'this is not a haiku poem it has {total_syllables} syllables')
