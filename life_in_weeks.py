# Get The User's Current Age

age = int(input('How Old Are You? \n'))

# Get The User's Expected Age Of Death

death = int(input('Till What Age Do You Expect To Live? \n'))

# Years Remaining

years = death - age

# Months Remaining

months = 12 * years

# Weeks Remaining

weeks = 52 * years

# Days Remaining

days = 365 * years

# Life In Weeks Calculation

life_remaining = f'You Have {days} Days, {weeks} Weeks, {months} Months & {years} Years Remaining.'

# Print Life in Weeks

print(life_remaining)
