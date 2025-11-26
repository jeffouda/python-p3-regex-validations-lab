import re

# Regex pattern for names allowing capitalized first and middle names with optional hyphens and apostrophes, including apostrophes inside name parts like "D'Angelo"
name = r"[A-Z][a-z]*(?:'[A-Z][a-z]+)*(?:[\s\-][A-Z][a-z]*(?:'[A-Z][a-z]+)*)*"
name_regex = re.compile(name)

# Regex pattern for phone numbers in multiple formats: 1234567890, 123-456-7890, (123) 456-7890
phone_number = r"^(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone_number)

# Regex pattern for emails: start with alpha, alphanumeric/dots allowed, @, domain, TLD
email_address = r"[a-zA-Z][a-zA-Z0-9\.]*@[a-zA-Z]+\.[a-zA-Z]{2,}"
email_regex = re.compile(email_address)
