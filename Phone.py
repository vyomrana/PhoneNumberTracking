import phonenumbers
from phonenumbers import carrier , geocoder, timezone

mobileNo = input ("Enter Mobile Number with Country Code:")
mobileNo = phonenumbers.parse(mobileNo)

# get timezone of a phone number 
print(timezone.time_zones_for_number(mobileNo))

# get carrier of a phone number 
print(carrier.name_for_number(mobileNo, "en"))

# get region information 
print(geocoder.description_for_number(mobileNo, "en"))

# validating of a phone number 
print("Valid Mobile Number :",phonenumbers.is_valid_number(mobileNo))

# checking possibility of a phone number
print("Checking possibility of Number :", phonenumbers.is_possible_number(mobileNo))