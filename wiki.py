import wikipedia


def wiki_search():

    topic = input("Please enter a search topic: ")
    results = wikipedia.search(topic)

    if not results:
        print("No results found. try another topic.")
        return

    summary = wikipedia.summary(results[0])

    print("* * * SEARCH RESULTS * * *")
    print(summary)


wiki_search()
