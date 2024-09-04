# Default Argument
def show_info(name, city = "Palakkad"):
    print(name)
    print(city)


show_info("Merin", "Thrissur")



# Keyword Argument
def show_info(name, city):
    print(name)
    print(city)


show_info(name = "Merin",city = "Thrissur")
show_info(name = "Anjali",city = "Palakkad")
