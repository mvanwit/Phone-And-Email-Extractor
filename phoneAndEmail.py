#! python3

import re, pyperclip

# Create a regex object for phone numbers

phoneRegex = re.compile(r'''

( 0\d | \+\d\d\s?\d | 00\s?\d\d\s?\d)			#first 2 digits -or- international area code with plus and first digit -or- intenational area code with space and first digit
(\s | \.)?										#space or dot separator
(\d\d)											#second 2 digits
(\s | \.)?										#space or dot separator
(\d\d)											#third 2 digits
(\s | \.)?										#space or dot separator
(\d\d)											#fourth 2 digits
(\s | \.)?										#space or dot separator
(\d\d)											#last 2 digits

	''', re.VERBOSE)

#TODO: Create a regex for email adress

#TODO: Get the text off the clipboard

#TODO: Extract the email/phone from this text

#TODO: Copy the extracted email/phone to the clipboard