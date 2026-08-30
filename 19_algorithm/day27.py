def nested_contains(numbers, target):
    for n in numbers:
        if isinstance(n, list):
            if nested_contains(n, target) == True:
                return True
        else:  
            if n == target:
                return True
    return False


print(nested_contains([1, 2, 3], 2))
print(nested_contains([1, [2, 3], 4], 3))
print(nested_contains([1, [2, [3, 4]], 5], 4))
print(nested_contains([1, [2, 3]], 9))
print(nested_contains([[1], [2, [3]]], 3))


## 예시로 결과 추적하기
# 회의실 A: nested_contains([[1], [2,[3]]], 3)
#   [1] 만남 → 회의실 B 호출
#              │
#              회의실 B: nested_contains([1], 3)
#                1 → 숫자, 3 아님 → 넘어감
#                for 끝 → return False   ← ★ B의 마지막 줄(8번)이 실행됨
#              │
#   결과 = False → if False → return 안 함 → 다음 형제로 계속!  (고친 덕분)
#   [2,[3]] 만남 → 회의실 C 호출
#              │
#              회의실 C: nested_contains([2,[3]], 3)
#                2 → 숫자, 아님
#                [3] → 회의실 D 호출 → 3 찾음 → return True
#                결과 = True → return True
#   결과 = True → return True
#   → A도 return True

## 한 줄정리
# return False (9번 줄) = "이 회의실에서 for 다 돌았는데 못 찾음" 이라는 뜻.
# 호출(회의실)마다 각자 자기 for가 끝나면 자기 return False를 실행한다.
# 안쪽 회의실의 False가 바깥까지 끝내는 게 아니라, 바깥은 그걸 받아 판단한다.

## 문법 사항 짚기
# if 참/거짓값 == True:   →   if 참/거짓값:       같은 뜻, 아래가 깔끔
# if 참/거짓값 == False:  →   if not 참/거짓값:   이것도

