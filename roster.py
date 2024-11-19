# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "Cadeau", "Claude", "Brown", "Tyson", "Davis", "Trimble", "Powell", "Jackson",],
            "First Name": ["Armando", "RJ", "Elliot", "Ty", "James", "Cade", "Elijah", "Seth", "Drake", "Ian",],
            "height": [83, 72, 73, 79, 82, 79, 75, 75, 78, 76],
            "weight": [240, 180, 180, 230, 215, 200, 215, 195, 195, 190]
}

data = pd.DataFrame(player)

# To get the bmi down to 2 decimal places, I asked chatgpt, it gave me several options
# I did try using round() to format the values as they are assigned to the data frame
# data["bmi"] = round((data["weight"]/2.205)/((data["height"]/39.37)**2), 2)
data["bmi"] = (data["weight"]/2.205)/((data["height"]/39.37)**2)

# The second option is the one I went with, it formats during printing, rather than
# modifying the data frame
# I like it because it looks pretty clean in the code, rather than hiding in a long line,
# like the first option
print(data.round({"bmi": 2}))

data.to_csv("bmi.csv")

# The third option chatgpt offered for formatting the bmi was this bit of code:
# data["bmi"] = data["bmi"].apply(lambda x: f"{x:.2f}")
# Which I chose not to use, because I am not fully sure how it works
# It was labeled as formatting the string during printing