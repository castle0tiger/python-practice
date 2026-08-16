def group_anagrams(texts):
    groups = {}

    for t in texts:
        processed = "".join(sorted(t))

        if processed in groups:
            groups[processed].append(t)
        else:
            groups[processed] = [t]

    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))