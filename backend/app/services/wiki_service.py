import wikipedia
wikipedia.set_lang("en")

def search_wiki_summary(query: str, sentences: int = 2) -> str:
    try:
        return wikipedia.summary(query, sentences=sentences)
    except Exception:
        return "Sorry, I couldn't find information on that topic."
