T = int(input())
for t in range(1, T+1):
    words = list(input())
    while True:
        for i in range(1, len(words)):
            if words[i] == words[i-1]:
                words.pop(i)
                words.pop(i-1)
                break
        else:
            break
    print(f"#{t} {len(words)}")