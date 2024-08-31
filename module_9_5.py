def all_variants(text):
    lenght = len(text)
    for start in range(lenght):
        for end in range(start + 1, lenght + 1):
            yield text[start:end]

a = all_variants("abc")
for i in a:
    print(i)
