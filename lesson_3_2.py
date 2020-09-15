def user_data(**kwargs):
    return kwargs


name = input('Name: ')
surname = input('Surname: ')
year_of_birth = input('Year of birth: ')
city_of_residence = input('City of residence: ')
email = input('email: ')
telephone = input('telephone: ')

print(user_data(Name=name, Surname=surname, Year_of_birth=year_of_birth, City_of_residence=city_of_residence,
                Email=email, Telephone=telephone))
