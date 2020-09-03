voted = {"Archimedes", "Sena", "Senadju", "Vincent", "Eli"}
def check_voter(name):
    if voted.get("name"):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")


print(check_voter("Sena"))


# Using hash table in caching
cache = {}
def get_page(url):
    if cache.get(url):
        return cache(url) # return cached data
    else:
        data = get_data_from_server(url)
        cache[url] = data # saves this data in your cache first
        return data


