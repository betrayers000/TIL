T = int(input())
for t in range(1, T + 1):
    search_word = input()[-1::-1]
    origin_word = input()
    # 각 문자열의 길이도 저장한다
    search_len = len(search_word)
    origin_len = len(origin_word)
    # 시작 인덱스
    i = search_len - 1
    result = 0
    while i < origin_len:
        count = 0
        last_word = ""
        # 문자열을 비교한다 last_word에 마지막 문자열을 넣어준다.
        for j in range(search_len):
            last_word += origin_word[i - j]
            if origin_word[i - j] == search_word[j]:
                count += 1
            else:
                break
        # 문자열 비교후 count 가 search_len 과 같으면 전부다 같기 때문에 result에 1을 더해준다
        if count == search_len:
            result += 1
            i += search_len
        # 그렇지 않은경우에는 last_word가 search_word 에 있는지 없는지를 탐색한다.
        else:
            for z in range(search_len - len(last_word) + 1):
                if search_word[z:z + len(last_word)] == last_word:
                    i += z
                    break
            else:
                i += search_len
    print(f"#{t} {result}")

