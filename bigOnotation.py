def find_name(name, phone_book):
    for person in phone_book:
        if name == person: 
            return True



name = "Kim"

phone_book = ["Tim", "Dan", "Oliver", "Kim"]
# O(n) time is linear, grows constantly if adding another element

def find_name(austin_phone_book, philly_phone_book):
    for austinite in austin_phone_book:
        for philadelphian in philly_phone_book:
            if austinite == philadelphian:
                return True 




austin_phone_book = ["Tim", "Dan", "Oliver", "Kim"]
philly_phone_book = ["Patrick", "Brandy", "Soosh", "Jen"]
# grows exponentially, to the power of 2
# O(n^2)

