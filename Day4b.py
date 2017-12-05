def create_phrase_list(path):
    phrase_file = open(path, "r")
    return phrase_file.readlines()

valid_count = 0
for phrase in create_phrase_list("input.txt"):
    words = phrase.strip().split(" ")
    s = set()
    for word in words:
        s.add(''.join(sorted(word)))

    if(len(s) == len(words)):
        valid_count += 1

print(valid_count)