def group_by_length(texts):
    groups = {}

    for t in texts:
        if len(t) in groups:
            groups[len(t)].append(t)
        else:
            groups[len(t)] = [t]

    return groups 

print(f"['a', 'bb', 'cc', 'ddd'] -> {group_by_length(['a', 'bb', 'cc', 'ddd'])}")
print(f"['cat', 'dog', 'hi', 'a'] -> {group_by_length(['cat', 'dog', 'hi', 'a'])}")
print("")