def cleanup(sentence: str) -> str:
    for i in "?,.!":
        sentence = sentence.replace(i,"")
    sentence = sentence.strip()

    return sentence.lower()

print(cleanup("  Hello!., there?    "))


