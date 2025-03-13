import spacy

nlp = spacy.load("pl_core_news_sm")


def findVariants(text, base_word):
    doc = nlp(text)
    variants = 0
    for token in doc:
        if token.lemma_ == base_word.lower():
            variants += 1
    return variants