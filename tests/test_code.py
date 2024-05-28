"""
Concept code.
Just trying things out.
Delete this later.
"""
import requests  # pip install requests
URL = "https://api.mangadex.org"

# Searching for manga
while True:

    # Query user for mange title
    title = input("Search: ")

    # Make request to MangaDex API
    request = requests.get(f"{URL}/manga", params={"title": title})

    # Display results of query
    if len(request.json()["data"]) == 0:
        continue
    for i in range(len(request.json()["data"])):
        print(i, request.json()["data"][i]["attributes"]["title"])

    # Query user for selection
    manga = None
    while manga is None:
        print("Please enter a number on the list to make your selection or "
              "\"quit\" to search another manga.")
        selection = input("Selection: ")
        if selection == "quit":
            break
        if not selection.isnumeric() \
                or int(selection) < 0 \
                or int(selection) > len(request.json()["data"]) - 1:
            print("Invalid selection.")
            continue
        manga = request.json()["data"][int(selection)]

    # Display manga info
    print(manga)
