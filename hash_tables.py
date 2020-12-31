# ------------------------------------------
# Grokking Algorithms  -- Hash Tables
# ------------------------------------------

#----------------------------------------
# Phonebook System

# Creating the phone_book dictionary/hash table
phone_book = dict() # same as phone_book = {}

# Adding phone numbers to the phone_book
phone_book["Jenny"] = 8675309
phone_book["Emergency"] = 911

# print(phone_book)
# print(phone_book["Jenny"])

#----------------------------------------
# Voting System

voted = {}

# value = voted.get("tom")
# print(value)

def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

# check_voter("Tom")
# check_voter("Mike")
# check_voter("Tom")

#----------------------------------------
# Cache System

cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_servers(url)
        cache[url] = data
        return data
