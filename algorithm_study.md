# 알고리즘 문제풀이 기록

> **이 파일 = "어떤 문제를 어떻게 풀었나"의 기록.** (문법/개념 자체의 설명은 GLOSSARY.md)
> 하루 한 문제. 재구축 방식(예측 → 백지 풀이 → 리뷰)으로 진행.
> 문법은 오픈북, 로직은 백지. 목표: 손으로 짜는 근육 + 재구축 약점 보강.
> 코드는 `19_algorithm/dayN.py`.

---

## Day 1 — 문자열 뒤집기 (★☆☆)

**문제:** 문자열을 받아 거꾸로 뒤집어 return. `reverse_text("hello") → "olleh"`

**내 풀이 (반복문 — 원리 이해용):**
```python
def reverse_text(text):
    result = ''
    for c in text:
        result = c + result   # 새 글자를 앞에 붙임(교체 대입) → 뒤집힘
    return result
```
- 예측 단계에서 "새 글자를 앞으로 붙인다"는 핵심을 스스로 찾아냄 (알고리즘 감각)
- 누적 패턴의 반대 버전: `result += c`(뒤에 붙임=순서유지) vs `result = c + result`(앞에 붙임=뒤집힘)

**실무 방식 (슬라이싱):**
```python
def reverse_text_2(text):
    return text[::-1]   # [시작:끝:간격], 간격 -1 = 뒤에서부터 = 통째로 뒤집기
```

**배운 것:** "이해의 선" 실전 적용 — **원리는 한 번 손으로(반복문), 그 다음엔 도구로([::-1])**.
실무자도 반복문으로 풀 줄 알면서 편해서 슬라이싱을 쓰는 것. 원리 겪었으니 이제 도구 써도 됨.

---

## Day 2 — 모음 개수 세기 (★★☆)

**문제:** 문자열에서 모음(a,e,i,o,u) 개수를 세어 return. `count_vowels("hello") → 2`

**내 풀이 (두 버전 — 조건 판단 방식 비교):**
```python
def count_vowels(text):
    result = 0
    for t in text:
        if t in 'aeiou':          # v2: in 으로 간결하게
            result += 1           # 누적 카운트 패턴
        # v1은 t == 'a' or t == 'e' or ... (길지만 같은 결과)
    return result
```
- 접근: for로 글자 순회(Day1) + if로 모음 판단 + result += 1 누적 카운트
- 두 버전(`or 5개` vs `in "aeiou"`)이 같은 결과임을 직접 확인 → in 쓰는 이유를 몸으로 익힘

**리뷰:** 테스트 결과를 변수 6개에 담았다가 출력했는데, 테스트는 바로 print해도 됨. 출력에 라벨 붙이면 나중에 뭐가 뭔지 보임(재구축 때 반복 지적).

**배운 것:** `in` 연산자 = "포함 관계" 도구. 세 맥락이 같은 뿌리 — `"a" in "aeiou"`(있냐), `for c in text`(순회), `x not in list`(없냐).
