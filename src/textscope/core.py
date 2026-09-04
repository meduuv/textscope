from collections import Counter

def stats(text: str) -> dict[str,int]:
    """Return basic deterministic text statistics."""
    return {"characters":len(text),"words":len(text.split()),"lines":len(text.splitlines()),"unique_words":len(set(text.lower().split()))}
