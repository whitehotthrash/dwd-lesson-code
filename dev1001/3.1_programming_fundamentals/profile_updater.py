# profile_updater.py
# Get user input
user_name = input('What is your name?')
user_city = "New York"
years_experience = 3.57 # Can be a float
project_count = 15

# Current basic output
# print("User:", user_name)
# print("Location:", user_city)
# print("Experience (Years):", years_experience)
# print("Projects Completed:", project_count)
print(f'{user_name} from {user_city} has {years_experience:.1f} years of experience and completed {project_count} projects.')
years_experience = 5 # update value of variable
print(f'{user_name} from {user_city} has {years_experience:.1f} years of experience and completed {project_count} projects.')
# Get the value of years_experience, add 1 to it, store result in years_experience
years_experience = years_experience + 1
print(years_experience)

x, y = 5, 10 # multiple assignment
print(x, y)
