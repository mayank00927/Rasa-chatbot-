import re

# The string containing multiple email addresses without separators
email_addresses = "mayank00@gmail.comvishes@dataxlsolutionsradha@gmail.com"

# Split the string at the '@' symbol to separate email addresses
email_list = email_addresses.split('@')

# Filter out any empty strings and add back the '@' symbol to each address
email_list = [f"{email}@{domain}" for email, domain in zip(email_list[::2], email_list[1::2])]

# Now, email_list will contain the individual email addresses
print(email_list)