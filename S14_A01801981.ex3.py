actual_year=int(input("What year is it? "))
year_born=int(input("What year where you born? "))
had_birthday=input("Have you had your birthday yet this year? ")
if had_birthday=="yes":
    age=actual_year-year_born
elif had_birthday=="no":
    age=actual_year-year_born-1

print(f"You are {age} years old")
