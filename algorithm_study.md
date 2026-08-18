# 알고리즘 문제풀이 기록

> **이 파일 = "어떤 문제를 어떻게 풀었나"의 기록.** (문법/개념 자체의 설명은 GLOSSARY.md)
> 하루 한 문제. 재구축 방식(예측 → 백지 풀이 → 리뷰)으로 진행.
> 문법은 오픈북, 로직은 백지. 목표: 손으로 짜는 근육 + 재구축 약점 보강.
> 코드는 `19_algorithm/dayN.py`.

---

## 📍 알고리즘 로드맵 (지금 내 위치)

```
[완료] 1단계: 기본 체력 — 순회하며 데이터 주무르기 (Day 1~10) ✅ 졸업
              변형 / 필터링 / 집계 / 상태관리 + 조합 + set/sorted
        ↓
[현재] 2단계: 입문 알고리즘 — 정렬 / 완전탐색 / 그리디 / 카운터·그룹핑  ← 지금 (Day 11~18)
        ↓
       3단계: 본격 코테 — 재귀(Day19 진입) → DFS·BFS / DP / 그래프
```

**"알고리즘"의 두 뜻:** 넓은 뜻(문제 푸는 절차, 지금 하는 것) vs 좁은 뜻(정렬·DFS 등 기법, 코테의 그것).
지금은 넓은 뜻으로 **기본 동작 4종**을 훈련 중. 이 동작들의 조합이 나중의 좁은 뜻 알고리즘이 됨.

**기본 동작 4종 (모든 알고리즘의 벽돌):**
| 동작 | 뜻 | 실전 예 |
|------|-----|---------|
| 변형(transform) | 순회하며 새 데이터 만들기 | 뒤집기, 대소문자 변환 |
| 필터링(filter) | 조건 맞는 것만 고르기 | 모음만, 짝수만, **주식 종목 필터** |
| 집계(aggregate) | 순회하며 세거나 합치기 | 개수, 합계, 평균 |
| 상태관리(track) | 순회하며 값을 추적·갱신 | 최대/최소, 누적 등수 |

*(각 Day 마지막의 "→ 알고리즘 연결" 줄이 이 표의 어디에 해당하는지 표시)*

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

**→ 알고리즘 연결:** **변형(transform)** — 순회하며 새 데이터를 만드는 동작. 입력을 그대로 두지 않고 가공. 나중에 "데이터 전처리", 문자열 처리 문제의 뿌리.

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

**→ 알고리즘 연결:** **필터링 + 집계** — 조건(모음?)에 맞는 것만 골라 세는 동작. 이게 정확히 **주식 filter.py**의 구조(`for stock: if 조건: append`). 코테에선 "특정 조건 만족하는 원소 개수" 유형의 뿌리.

---

## Day 3 — 최댓값과 최솟값의 차이 (★★☆)

**문제:** 숫자 리스트에서 (최댓값 - 최솟값)을 return. `max_min_diff([3,7,1,9,4]) → 8`

**내 풀이 (비교·갱신 — 원리):**
```python
def max_min_diff(numbers):
    max_result = numbers[0]   # 첫 값으로 초기화 (0으로 하면 음수리스트 버그 — 자판기 때 배운 함정 회피)
    min_result = numbers[0]
    for n in numbers:
        if max_result < n:
            max_result = n
    for n in numbers:
        if min_result > n:    # min은 부등호만 뒤집기 (대칭)
            min_result = n
    return max_result - min_result
```

**내장 함수 버전:**
```python
def max_min_diff_v2(numbers):
    return max(numbers) - min(numbers)
```

**막혔던 것:** `def f(???)` 괄호에 "리스트 넣는 문법"이 따로 있는 줄 앎.
→ 괄호 안은 **"받을 이름표(변수명)"**일 뿐. text든 numbers든 그냥 이름. 종류 무관.

**리뷰 → v3로 복습 구현:** for를 두 번 돌았는데(max용, min용), 한 반복문 안에서 max/min을 둘 다 체크하면 한 번만 돌면 됨(큰 데이터면 2배 빠름). 직접 v3로 구현해서 확인.
→ **한 문제 세 풀이 완성: v1(for 두 번=원리·명확) / v2(max()-min()=도구) / v3(for 한 번=효율).** 같은 문제를 여러 각도로 = 트레이드오프를 아는 학습.

**배운 것:** 매개변수 = 받을 이름표(특별 문법 없음). 비교·갱신을 리스트에 적용. max()/min() 내장. 반복문 한 번에 여러 판단 넣기.

**→ 알고리즘 연결:** **상태관리(track)** — 순회하며 "지금까지의 최고/최소"를 변수에 기억·갱신하는 동작. 코테 단골(최대 구간합, 최장 길이 등)의 뿌리. "한 번 순회로 여러 상태 동시 추적"(v3)은 효율 알고리즘의 기본 감각.

---

## Day 4 — 가장 많이 나온 글자 (★★★, 첫 딕셔너리 문제)

**문제:** 문자열에서 최다 등장 글자를 return. `most_frequent("banana") → "a"`

**내 풀이 (2단계: 딕셔너리 카운터 + 비교갱신):**
```python
def most_frequent(text):
    counts = {}
    for t in text:               # 1단계: 개수 세기
        if t in counts:
            counts[t] += 1       # 이미 있으면 +1
        else:
            counts[t] = 1        # 처음이면 1로 (새 키 생성)

    frequent = text[0]           # 2단계: 최다 찾기 (비교갱신)
    for key in counts:           # 딕셔너리 순회 → 키(글자)가 하나씩
        if counts[frequent] < counts[key]:   # 개수끼리 비교 (counts[키]로 꺼냄)
            frequent = key
    return frequent, counts[frequent]   # 여러 값 동시 return (쉼표) → ('l', 2)
```

**막혔던 것 & 배운 것:**
- **딕셔너리 카운터 패턴** = "있으면 +1, 없으면 1". 개수 세기의 표준. (재구축 conversations[user]=[] 로 새 키 만들던 것과 같음)
- **키 vs 값 구분이 관문:** 글자(키)는 `for key in counts`로, 개수(값)는 `counts[key]`로 꺼낸다. 이걸 섞어서 처음엔 `frequent[key] < key`로 꼬였음.
- **여러 값 동시 return:** `return A, B` (쉼표). 받을 땐 `글자, 개수 = 함수()`.
- **v2(중복 저장 버전)와 비교:** frequent에 [글자,개수] 쌍으로 저장하니 `frequent[1]`, `[key,counts[key]]`로 매번 쌍을 풀고 담아 복잡 + 두 곳(counts와 frequent)이 어긋날 위험. → **원칙: 정보는 한 곳에만(Single Source of Truth). 개수 출처는 counts, frequent는 글자만 가리키고 필요할 때 꺼낸다.**

**→ 알고리즘 연결:** **집계(aggregate) — 딕셔너리 카운터.** "무엇이 몇 번 나오는가"를 딕셔너리로 세는 것. **코테에서 가장 자주 쓰는 핵심 패턴 중 하나**(빈도수, 중복 찾기, 그룹핑, 애너그램 등 전부 이 뿌리). Day2 집계가 "개수 하나"였다면 Day4는 "항목별 개수" = 한 단계 위. + 딕셔너리 순회는 새 도구.

---

## Day 5 — 두 리스트의 공통 원소 (★★☆)

**문제:** 두 리스트에 다 있는 원소를 새 리스트로 return. `common_elements([1,2,3,4],[3,4,5,6]) → [3,4]`

**내 풀이 (수집 패턴):**
```python
def common_elements(list1, list2):
    result = []                # 빈 리스트 초기화 (반복문 밖!)
    for c in list1:
        if c in list2:         # 두 번째 리스트에 있나? (in)
            result.append(c)   # 있으면 결과에 모으기
    return result
```
- **거의 힌트 없이 혼자 완성 = 성장 신호.** 예측 단계에서 세 조각(for/if in/append)을 다 스스로 설계.
- 빈 결과([])도 자동 처리 — 아무것도 append 안 되면 빈 리스트 그대로.

**엣지 케이스 → 중복 제거 두 방법 직접 구현 (v2, v3):**
- list1에 중복 있으면 결과도 중복(`[3,3,4],[3,4]→[3,3,4]`). "중복 없이" 처리법:
- **v2 (원리, 방법 A):** `if c in list2 and c not in result` — `and`로 조건 두 개 묶기(자판기 때 그거) + `not in`으로 "이미 담았으면 건너뛰기"
- **v3 (도구, 방법 B):** `list(set(list1) & set(list2))` — set은 중복 자동 제거, `&`는 교집합. 단 **순서 보장 안 됨**
- 셋(v1 중복허용 / v2·v3 중복제거)을 나란히 남겨 트레이드오프 비교. 예외 상황 떠올리는 감각은 코테 필수.

**→ 알고리즘 연결:** **필터링 → 수집(collect).** Day2 필터링이 "개수를 셌다"면, 오늘은 "고른 것을 리스트로 모았다". 세기 vs 모으기 = 필터링의 두 출력.
**이게 정확히 주식 filter.py 구조:** `for stock in stocks: if 조건: result.append(stock)`. 교집합(intersection)의 기본형이기도 함.

---

## Day 6 — 중복된 원소 찾기 (★★★, 첫 패턴 조합)

**문제:** 리스트에서 2번 이상 나온 원소를 리스트로 return. `find_duplicates([1,2,2,3,3,3,4]) → [2,3]`

**내 풀이 (Day4 + Day5 조합):**
```python
def find_duplicates(numbers):
    counts = {}
    for n in numbers:               # 1단계: 딕셔너리 카운터 (Day4)
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    result = []
    for key in counts:              # 2단계: 조건 필터 + 수집 (Day5)
        if counts[key] >= 2:        # 개수 2 이상인 키만
            result.append(key)
    return result
```
- **★★★인데 힌트 없이 두 패턴을 통으로 조립.** Day4에선 쪼개줬던 걸 오늘은 스스로 이어붙임 = 성장.
- 부등호 감각: "2번 이상"이라 `>= 2`. "정확히 2번"이면 `== 2`. 조건이 문제 뜻을 정확히 반영해야(자판기 경계값 때 배운 것).

**→ 알고리즘 연결:** **"count then filter" 패턴 (집계 → 필터).** Day4(집계) + Day5(수집)의 조합. 빈도 기반 문제(중복 찾기, 한 번만 나온 것, N번 이상)는 전부 이 골격 = 세고 → 거른다. 주식으로 치면 "종목별 집계 → 조건 만족 종목 추리기"와 같은 2단계 구조.

---

## Day 7 — 한 번만 나온 첫 글자 (★★★, 순서 + 엣지케이스)

**문제:** 딱 한 번 나온 글자 중 최초의 것을 return, 없으면 None. `first_unique("abcabd") → "c"`

**내 풀이:**
```python
def first_unique(text):
    counts = {}
    for t in text:                  # 1단계: 카운터 (Day4)
        if t in counts: counts[t] += 1
        else: counts[t] = 1
    result = []
    for t in text:                  # 2단계: text를 순회! (counts 아님) — 순서 지키려고
        if counts[t] == 1:
            result.append(t)
    if result:                      # 엣지: 빈 결과 처리
        return result[0]
    else:
        return None
```

**오늘의 두 배움:**
- **순회 대상 선택 = 알고리즘 사고.** "가장 먼저"를 요구하면 → "먼저"라는 정보가 어디 있나 → **원본 text에 있다** → text를 돈다. (counts를 돌면 순서 꼬일 수 있음. 요즘 dict가 입력순서 기억하긴 하지만, 순서에 "기대는 것"과 "확실히 지키는 것"은 다름 — text 순회가 의도 명확·안전)
- **엣지 케이스 + `if result:` 문법.** 빈 리스트에 `result[0]` → IndexError. 로직("있으면 첫 개, 없으면 None")은 스스로 세웠고 문법만 몰랐음 = **목표 상태**(로직 서고 문법은 오픈북). `if result:` = "뭐라도 있으면"(빈 리스트는 거짓).

**효율 팁(알아둘 것):** "첫 개만 필요"하면 찾자마자 `return t`, 못 찾으면 `return None`. result 리스트 불필요 + 즉시 멈춤(Day3 v3의 "한 번 순회" 정신). 단 현재 풀이(다 모으고 첫 개)도 정답.

**→ 알고리즘 연결:** count then filter + **순회 대상 선택(순서)** + **엣지 케이스 처리(빈 결과)**. 뒤 둘은 "정답은 나오는데 예외에서 터지는" 코테 감점 포인트를 막는 디테일.

---

## Day 8 — 두 번째로 큰 수 (★★☆, 정렬 첫 등장 · 2단계 다리)

**문제:** 리스트에서 두 번째로 큰 수 return (중복 없다고 가정). `second_largest([3,7,1,9,4]) → 7`

**방법 A (원리 — 상태관리 심화, 애먹음):**
```python
def second_largest(numbers):
    first = numbers[0]; second = numbers[1]
    if first < second:                 # 초기 두 개를 큰 순서로 세팅
        first, second = numbers[1], numbers[0]
    for n in numbers:
        if n > first:                  # 1등보다 크면: 1등을 2등으로 밀고(순서 중요!) 새 값이 1등
            second = first
            first = n
        elif n < first and n > second: # 1등 아닌데 2등보단 크면: 2등 교체
            second = n
    return second
```
- 핵심: **변수 2개(1등·2등) 동시 추적.** `second = first` 먼저 → `first = n` 순서 지켜야 옛 1등 안 사라짐.
- `elif n < first and n > second` = "중간 구간" 조건. 빠뜨리기 쉬운데 챙김.

**방법 B (도구 — 정렬):**
```python
def second_largest_v2(numbers):
    return sorted(numbers)[-2]   # 정렬 → 뒤에서 두 번째
```
- `sorted(numbers)` = 작은 순 정렬 `[1,3,4,7,9]`. `[-2]` = 음수 인덱스, 뒤에서 둘째(=둘째로 큰 값). `[-1]`=제일 큰 값.

**비교:** A는 20줄·머리아픔·근데 원리 앎+한 번 순회(빠름) / B는 3줄·간단·sorted가 뭘 하는지 알아야.

**엣지(알아둘 것):** 중복 있으면 갈림. `[9,9,5]` → A는 5("9 다음 큰 값"), B는 `sorted[-2]=9`("위치 기준"). "두 번째로 큰"의 정의(값 기준 vs 위치 기준)에 따라 다름. 지금 문제는 중복 없어 동일.

**v3 (스스로 응용 — Day5 set 끌어옴):** 중복을 "값 기준"으로 처리.
```python
def second_largest_v3(numbers):
    return sorted(list(set(numbers)))[-2]   # set으로 중복 제거 → 정렬 → 뒤에서 둘째
```
- 시키지 않았는데 **Day5의 set을 다른 문제에 스스로 적용** = 지식 연결 신호.
- set의 단점(순서 없음)이 뒤의 sorted로 무력화됨 → 도구 조합으로 단점 상쇄되는 좋은 예.

---

## Day 9 — 학생별 평균 점수 (★★★, 중첩 반복 · 1단계 마무리)

**문제:** `[{"name":.., "scores":[..]}, ...]` → `{이름: 평균}` 딕셔너리 return.

**내 풀이:**
```python
def average_scores(students):
    result = {}
    for student in students:                 # 바깥: 학생마다
        total = 0                            # ★ 초기화 위치: 바깥 안·안쪽 밖 (학생마다 리셋)
        for score in student["scores"]:      # 안쪽: 그 학생 점수마다
            total += score
        average = total / len(student["scores"])
        result[student["name"]] = average    # 결과 딕셔너리에 {이름: 평균}
    return result
```

**핵심:**
- **중첩 반복(nested loop) 첫 등장.** 바깥(학생) 안에 안쪽(점수). `total=0`을 정확한 자리(학생마다 리셋)에 놓는 게 함정 — 맞힘.
- **에러를 스스로 진단·해결 (1단계 졸업 신호!):** 처음 `result[student]=average`로 씀 → `TypeError: unhashable type: 'dict'`(딕셔너리는 딕셔너리 키로 못 씀) → 스스로 원인 찾아 `result[student["name"]]`로 고침. "통째(student) vs 그 안의 값(student['name'])" 구분 = Day4 키/값 감각 재적용.
- (unhashable = 딕셔너리 키로 못 쓰는 타입. 딕셔너리·리스트는 키 불가, 문자열·숫자·튜플은 가능. 깊이는 이해의 선 아래.)

**→ 알고리즘 연결:** **그룹별 집계(group aggregation).** 바깥(그룹) 돌며 안쪽(그룹 내부) 집계. "학생별 평균/카테고리별 합계/부서별 인원" 전부 이 구조. **주식 프로젝트의 "종목별로 여러 날 데이터 집계"가 정확히 이 모양**(리스트 안 딕셔너리 안 리스트).

---

## Day 10 — 🎓 1단계 졸업 시험: 성적 리포트 (★★★)

**문제:** 점수 리스트 → `{"합격자수":.., "최고점":.., "평균":..}` 딕셔너리. (합격=60 이상)

**내 풀이 (힌트 없이 스스로 설계·완성):**
```python
def grade_report(scores):
    result = {}
    passer = 0                    # 합격자 카운트
    highest = scores[0]           # 최고점 (첫 값 초기화)
    total = 0                     # 합계
    for score in scores:          # ★ 한 번 순회로 세 패턴 동시에
        if score >= 60:
            passer += 1           # ① 필터+카운트 (Day2)
        if highest < score:
            highest = score       # ② 상태관리 비교갱신 (Day3)
        total += score            # ③ 누적 (Day1~)
    average = total / len(scores)
    result["합격자수"] = passer
    result["최고점"] = highest
    result["평균"] = average
    return result
```

**졸업 판정 통과.** 힌트 없이 예측→완성. **세 패턴을 하나의 반복문에** 넣음(리스트 3번 돌 걸 1번에) = "한 번 순회로 여러 상태" 완성형. 초기값 셋 다 정확.

**→ 알고리즘 연결:** 1단계 종합 — 필터+집계+상태관리+딕셔너리 결과를 한 번 순회로. Day4에선 내가 쪼개줬는데 Day10은 스스로 통으로 설계 = 졸업 신호.

---

# 🎓 1단계 졸업 (Day 1~10 완료)

**익힌 것:** 기본 동작 4종(변형·필터링·집계·상태관리) + 조합(count then filter) + 순서/엣지케이스 처리 + 중첩반복 + 도구(set, sorted, 딕셔너리 카운터). 뒤로 갈수록 힌트↓, 스스로 조립·에러 자가해결·지식 응용(set 끌어옴) 신호 나타남.

**다음: 2단계 (정렬 심화 → 완전탐색 → 그리디).** 방식 전환 — 로직도 "30분은 스스로 버티기" 후 힌트(끙끙대는 시간=학습). 문법은 여전히 오픈북.

---

## Day 11 — 점수 높은 순 이름 정렬 (★★★, 2단계 첫 문제 · 정렬 심화)

**문제:** 학생 딕셔너리 리스트 → 점수 높은 순 이름 리스트. `rank_names(students) → ["이영희","김철수","박민수"]`

**내 풀이:**
```python
def rank_names(students):
    result = []
    sorted_students = sorted(students, key=lambda x: x["score"], reverse=True)  # 정렬(새 도구)
    for s in sorted_students:        # 순회하며 수집 (Day5)
        result.append(s["name"])
    return result
```

**새 문법 — 정렬 기준 `key=`:**
- `sorted(리스트, key=lambda x: x["score"], reverse=True)` = "각 항목의 score를 **기준으로** 내림차순 정렬"
- **중요(오해했다 교정):** `key=`는 "뭘 보고 순서 정할지"만 지정. **결과는 원래 항목(딕셔너리 통째) 그대로, 순서만 재배열.** score 기준이라고 score만 남는 게 아님. → 그래서 정렬 후 `s["name"]`으로 이름 꺼낼 수 있음.
- `lambda x: x["score"]` = "x 받으면 x['score'] 돌려주는 이름 없는 미니 함수"(기준 지정용). 깊이는 이해의 선 아래.
- 오해 상황을 **직접 print 찍어 실제 결과 확인 후 해결** = Day9 에러 자가진단과 같은 태도.

**v2 (리스트 컴프리헨션으로 재구현):** `return [s["name"] for s in sorted(students, key=lambda x: x["score"], reverse=True)]`
- "빈 리스트 → for → append" 3줄을 한 줄로. **문법 상세는 GLOSSARY "리스트 컴프리헨션" 항목** 참조.
- agent01.py 아닌 **14_fastapi/main.py:57**의 `len([m for m in ... if m["role"]=="user"])`가 실제 컴프리헨션 예시 (대화기록에서 user 카드만 골라 세기). 오늘 배운 걸로 그 줄이 읽힘.

**→ 알고리즘 연결:** **정렬 기준 정하기(key=).** Day8 "숫자 그냥 정렬"에서 → "딕셔너리를 특정 필드 기준 정렬"로. 코테 "~순 정렬" 유형 대부분 이걸로 풀림. **주식 프로젝트 "종목을 점수/거래량 순 정렬"에 직결.**

---

## Day 12 — 가장 가까운 두 수의 차이 (★★★, 정렬을 "무기"로)

**문제:** 리스트에서 가장 가까운 두 수의 차이(최솟값) return. `closest_diff([3,8,1,12,5]) → 2`

**내 풀이 (정렬 → 인접 비교):**
```python
def closest_diff(numbers):
    sorted_numbers = sorted(numbers)                    # 먼저 정렬
    closest = sorted_numbers[1] - sorted_numbers[0]     # 첫 인접 차이로 초기화
    for i in range(len(sorted_numbers) - 1):            # 마지막 직전까지! (i+1 보니까)
        if sorted_numbers[i+1] - sorted_numbers[i] < closest:
            closest = sorted_numbers[i+1] - sorted_numbers[i]
    return closest
```

**오늘의 핵심 통찰 (2단계 사고):**
- ❌ 순진한 법: 모든 쌍 비교(5개→10쌍, 100개→4950쌍). ✅ 영리한 법: **정렬하면 가장 가까운 건 반드시 "인접"** → 인접만 비교(100개→99번).
- **"정렬을 출력용이 아니라 문제 해결의 무기로"** = Day11과의 차이. "정렬하면 가까운 건 옆에 있다"는 보장을 활용.
- 로직은 스스로 세웠고 **문법(range)만 몰라서 막힘 = 목표 상태.** `for l in len(...)`(숫자는 순회 불가) → `for i in range(len(...)-1)`.

**함정 — range 범위:** `[i+1]`(다음 원소) 볼 땐 `range(len()-1)`로 **마지막 직전까지**. 안 그러면 마지막에서 `[len]` 접근 → IndexError.

**→ 알고리즘 연결:** **"정렬 후 인접 비교" 패턴.** 코테 단골(중복 찾기, 구간 겹침, 최소 간격 등). 정렬이 "가까운 건 인접"을 보장 → 완전탐색(모든 쌍)을 회피. 2단계의 대표 사고방식.

**방법 B (완전탐색 맛보기 — 스스로 도전):** 정렬 없이 모든 쌍 비교.
```python
def closest_diff_v2(numbers):
    closest = abs(numbers[0] - numbers[1])
    for i in range(len(numbers)):
        for j in range(len(numbers)):     # 중첩: 모든 쌍 (i,j) 만들기
            if i == j:
                continue                  # 같은 것끼리는 건너뛰기
            if abs(numbers[i] - numbers[j]) < closest:  # abs=절댓값
                closest = abs(numbers[i] - numbers[j])
    return closest
```
- **A vs B:** A(정렬)=빠름(100개→99번) / B(완전탐색)=느림(100개→~10000번)이지만 정렬 없이도 확실히 답. **코테 접근법: 일단 완전탐색 되나 보고 → 느리면 영리한 방법(정렬 등).**
- **새 문법:** `abs()`=절댓값(음수 차이 방지), `continue`=이번 반복 건너뛰고 다음으로.
- **continue vs pass:** continue=이번 바퀴 중단하고 다음 반복으로(흐름 제어) / pass=진짜 아무것도 안 함(빈 블록 자리채우기, 에러 방지용). 완전히 다름.
- 완전탐색(모든 경우 다 해보기)의 골격 = 중첩 반복. 다음 2단계 주제 미리 맛봄.

---

## Day 13 — 두 수의 합 (★★★, 완전탐색 정면 · "존재하는가")

**문제:** 서로 다른 두 수의 합이 target이 되는 쌍이 있으면 True. `has_pair_sum([2,7,11,15], 9) → True`

**내 풀이:**
```python
def has_pair_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue                       # 같은 원소 제외
            if numbers[i] + numbers[j] == target:
                return True                    # 찾으면 즉시 탈출 (반복문 안)
    return False                               # ★ 다 돌고도 없으면 (반복문 밖!)
```

**핵심 — `return False` 위치 (오늘의 함정, 맞힘):**
- `return True`는 반복문 **안**(찾자마자 탈출), `return False`는 반복문 **밖**(다 봐야 "없다" 결론).
- False를 안에 넣으면 첫 쌍 안 맞자마자 반환 → 나머지 안 봄 → 버그. "다 찾아봤는데 없다"는 반복 끝난 후에만 가능.
- Day7 v2("찾자마자 return, 끝까지 없으면 return")의 구조를 그대로 적용 = 지식 연결.

**완전탐색 "존재하는가?" 표준 틀:**
```
for 모든 경우:
    if 조건: return True    ← 하나라도 찾으면 성공
return False               ← 다 봐도 없으면 실패
```
코테에서 "~인 경우 있나/가능한가" = 대부분 이 골격.

**알아둘 것(효율):** `for j in range(i+1, len())`로 하면 (i,j)와 (j,i) 중복·자기자신 자동 제거 → continue 불필요, 절반만 검사. 현재 코드도 정답, 이건 더 깔끔한 버전.

**→ 알고리즘 연결:** **완전탐색(brute force) 정면.** 모든 쌍을 다 만들어(중첩 반복) 조건 검사 → 찾으면 탈출. Day12 맛보기(모든 쌍 만들기) + 오늘(존재 판정 틀) = 완전탐색 기본기 완성. "일단 다 해보기"의 대표형.

---

## Day 14 — 거스름돈 동전 개수 (★★★, 그리디 시작)

**문제:** 동전 리스트로 금액 만들 최소 개수. `min_coins([500,100,50,10], 1260) → 6`

**내 풀이 (if 분기 버전 — 동작 정답):**
```python
def min_coins(coins, target):
    sorted_coins = sorted(coins, reverse=True)   # 큰 것부터
    count = 0
    for coin in sorted_coins:
        if target % coin == 0:      # 딱 떨어지면
            count += target // coin
            return count
        else:
            count += target // coin
            target = target - (coin * (target // coin))   # 남은 금액
    return count
```

**간결 버전 v2 (if 분기 불필요):**
```python
def min_coins(coins, target):
    count = 0
    for coin in sorted(coins, reverse=True):
        count += target // coin     # 이 동전 몇 개 (몫)
        target = target % coin      # 쓰고 남은 금액 (나머지)
    return count
```
- `target - coin*(target//coin)`(내가 손계산) = **`target % coin`(나머지)** 와 같음. //(몫)·%(나머지)가 짝.
- 딱 떨어지면 target이 0 → 다음 동전들은 `//`가 0이라 자동으로 안 더해짐 → **if 분기 없어도 됨.** "이 조건 분기가 정말 필요한가?" 의심하는 감각.

**그리디 골격:** 큰 것부터(정렬) → 매 순간 최대한(`//`) → 남은 걸로 계속(`%`). 모든 조합 안 따져도 최소 나옴.

**⚠️ 그리디의 함정 (알아둘 것):** 그리디가 **항상 맞진 않음.** 동전 `[4,3,1]`, 금액 6이면 그리디는 4+1+1=3개인데 실제 최소는 3+3=2개. "큰 것부터"가 항상 최선은 아님. 한국 동전(500/100/50/10)은 그리디가 성립하게 설계돼 오늘은 풀림. **"그리디는 빠르지만 조건이 맞아야 정답."**

**메모:** 내(Claude)가 낸 예시 답 `890→12`는 계산 실수, **정답은 9**(500×1+100×3+50×1+10×4). 사용자가 검산해서 잡아냄 = "주어진 답 의심·검증" 습관 (중요).

**→ 알고리즘 연결:** **그리디(greedy) 시작.** "매 순간 최선"만 골라 빠르게. 완전탐색(다 해보기)의 반대 축. 단 성립 조건 필요. 새 문법 //(몫)·%(나머지).

---

## Day 15 — 최대한 많이 담기 (★★★, 정렬+그리디 조합)

**문제:** 무게 리스트 + 용량 → 담을 수 있는 최대 개수. `max_items([2,5,1,8,3], 10) → 3`

**내 풀이 (if/elif/else 3갈래 — 동작 정답):**
```python
def max_items(weights, target):
    sorted_weights = sorted(weights)   # ★ 가벼운 것부터! (개수 최대가 목표)
    total = 0; count = 0
    for w in sorted_weights:
        if w < target and total + w <= target:
            total += w; count += 1
        elif ...: return count   # 못 담으면 멈춤
        else: return count
```

**핵심 판단 (맞힘):** "개수 최대"면 **가벼운 것부터**. Day14는 "큰 동전부터"였는데 이번엔 반대 — **목표에 따라 정렬 방향이 바뀜.** 스스로 잡음.

**간결 버전 v2 (break):**
```python
def max_items(weights, target):
    total = 0; count = 0
    for w in sorted(weights):
        if total + w <= target:   # 담아도 용량 안 넘으면 (이 조건 하나면 충분)
            total += w; count += 1
        else:
            break                 # 넘으면 반복 중단
    return count                  # 밖에서 한 번만 return
```
- 조건은 `total + w <= target` **하나면 됨** (`w<target` 불필요, `[100],10`도 이걸로 걸러짐). "이 분기 정말 다 필요한가?" 감각(Day14에 이어).
- **새 문법 `break`:** 반복문 즉시 종료. Day13 "return을 반복문 밖에" 구조와 같음("끝까지 담거나 / break로 멈추거나 → 밖에서 한 번 return").
- **break vs return:** break=반복문만 빠져나감(함수 계속) / return=함수 자체 종료(값 들고 나감).

**→ 알고리즘 연결:** **정렬+그리디 조합.** "가벼운 것부터 담아 개수 최대화"는 그리디 논증(정렬로 순서 보장 → 앞에서부터 담으면 최적). 누적(Day1)+순회(Day12)+조기중단(break). 코테 "최대 개수/최소 그룹" 유형의 기본.

---

## Day 16 — 빈도수 순 정렬 (★★★, 카운터+정렬 조합)

**문제:** 많이 나온 순으로 원소 정렬(각 하나씩). `sort_by_frequency([1,2,2,3,3,3]) → [3,2,1]`

**내 풀이:**
```python
def sort_by_frequency(inputs):
    counts = {}
    for i in inputs:                    # 1단계: 딕셔너리 카운터 (Day4)
        if i in counts: counts[i] += 1
        else: counts[i] = 1
    return sorted(counts, key=lambda x: counts[x], reverse=True)   # 2단계: 개수 기준 정렬 (Day11)
```

**오늘의 핵심 (함정을 한 번에 맞힘):**
- `sorted(counts, key=lambda x: counts[x], reverse=True)`
- `sorted(counts)` → 딕셔너리는 **키(원소)**가 정렬 대상. `key=lambda x: counts[x]` → 각 원소 x를 **그 원소의 개수**로 정렬.
- **정렬 대상(원소)과 정렬 기준(개수)이 다름** = Day11("학생을 점수로")보다 한 단계 추상적. "원소를, 그 원소의 개수로" 정렬.
- (`sorted(counts.keys(), ...)`로 명시해도 같음. 그냥 `counts`만 써도 키가 나옴.)

**→ 알고리즘 연결:** **Day4(카운터) + Day11(정렬 기준) = "세고 → 개수로 정렬".** "Top N 자주 나온 것" 유형의 핵심(인기순 정렬, 최빈 단어 등). **주식: "가장 자주 신호 뜬 종목 순 정렬"이 정확히 이 패턴** — `sorted(종목별횟수, key=lambda x: 종목별횟수[x], reverse=True)`.

---

## Day 17 — 길이별 단어 묶기 (★★★, 그룹핑 = 값이 리스트인 딕셔너리)

**문제:** 글자 수 같은 단어끼리 묶기. `group_by_length(["a","bb","cc","ddd"]) → {1:["a"], 2:["bb","cc"], 3:["ddd"]}`

**내 풀이:**
```python
def group_by_length(texts):
    groups = {}
    for t in texts:
        if len(t) in groups:
            groups[len(t)].append(t)   # 이미 있으면 그 리스트에 추가
        else:
            groups[len(t)] = [t]        # 없으면 새 리스트 [t]로 시작
    return groups
```

**핵심 — Day4 카운터의 진화 (값: 숫자 → 리스트):**
```
Day4:  counts[x] += 1  /  counts[x] = 1     (값이 숫자)
오늘:  groups[k].append(t)  /  groups[k] = [t]  (값이 리스트)
```
구조 동일, 담는 게 숫자→리스트. "그룹핑 패턴"(dict of lists). 스스로 연결.

**에디터 색깔 관찰(중요 개념):** `result=[]` 후 `result.append`는 노랗게 강조되는데, `groups[len(t)].append`는 하얗다. → **색깔은 에디터의 "확신도"지 코드 정답 여부가 아님.** `result=[]`는 리스트임이 확실 → 에디터가 앎. `groups[len(t)]`는 딕셔너리에서 꺼낸 값이라 실행 전엔 타입 확신 못 함 → 색칠/자동완성 안 함. 하얀색=틀린 게 아님. "내가 알고 쓰는가"가 기준, 실행 확인이 정답. (이해의 선 아래)

**→ 알고리즘 연결:** **그룹핑(group by) — 값이 리스트인 딕셔너리.** "카테고리별로 묶기"의 표준. Day9 그룹별 집계가 "그룹별 숫자"였다면, 오늘은 "그룹별 목록". 주식 "종목을 조건/패턴별로 묶기"에 직결. 코테 애너그램 그룹핑 등의 뿌리.

---

## Day 18 — 애너그램 묶기 (★★★, 그룹핑+정렬 조합 · 코테 단골)

**문제:** 글자 재배열로 같아지는 단어끼리 묶기. `group_anagrams(["eat","tea","tan","ate","nat","bat"]) → [["eat","tea","ate"],["tan","nat"],["bat"]]`

**내 풀이:**
```python
def group_anagrams(texts):
    groups = {}
    for t in texts:
        processed = "".join(sorted(t))   # 서명(signature): 글자 정렬 후 붙이기 → "eat","tea"→"aet"
        if processed in groups:
            groups[processed].append(t)
        else:
            groups[processed] = [t]       # ★ 리스트로 시작 ([t], 대괄호!)
    return list(groups.values())          # 그룹(값)들만 리스트로
```

**핵심 아이디어:** 애너그램 = **글자 정렬하면 같아짐.** 정렬한 값을 그룹 키로 쓰면 자동으로 모임.
- `"".join(sorted(단어))` = 정렬 후 접착제 없이 붙이기. `""`=사이에 아무것도 안 넣음 (`"-".join`이면 `a-e-t`). 서명은 딱 붙어야 하니 `""`.
- 리스트를 키로 못 씀(unhashable) → 문자열 서명으로 변환 필요.

**오늘의 진짜 교훈 — 샷건 디버깅 조심:**
- 진짜 원인은 12번 줄 `vallues`(→`values`) 오타 하나였음. 근데 그걸 못 찾고 **여기저기 만지다가** 멀쩡한 `= [t]`를 `= t`로 바꿈 → 새 버그(`'str' has no attribute 'append'`)까지 생겨 더 꼬임.
- **원칙 ①** 에러는 줄 번호부터. **원칙 ②** 한 번에 한 곳만 고치고, 아니면 되돌린 뒤 다음 시도. 여러 곳 동시에 만지면 뭐 때문에 되고 안 되는지 모름 + 멀쩡한 코드까지 망침.
- 그룹핑 급소: `= [t]`(리스트로 시작)와 `.append(t)`는 **짝**. 하나 어긋나면 터짐.

**→ 알고리즘 연결:** **그룹핑 + "서명(signature)으로 키 만들기".** Day17 그룹핑에 "정렬로 그룹 기준 생성"을 얹음. 코테 최빈 단골(애너그램). "무엇을 기준으로 같은 그룹인가"를 계산해 키로 삼는 발상이 핵심.

---

## Day 19 — 1부터 n까지 합 (재귀 첫 등장, ★★★ 개념 도약)

**문제:** 1~n 합을 **재귀로**(for 없이). `sum_to_n(5) → 15`

**내 풀이:**
```python
def sum_to_n(n):
    if n == 1:                    # ① 멈추는 조건(base case) — 없으면 무한 추락(RecursionError)
        return 1
    return n + sum_to_n(n - 1)    # ② 자기 자신을 더 작은 문제로 부름
```

**재귀(recursion) = 함수가 자기 자신을 부름.** 뼈대 두 개:
- ① base case: 더 못 쪼개는 지점에서 멈춤. **재귀 짤 때 제일 먼저 "어디서 멈추지?"부터.**
- ② 자기 호출: 자신을 "더 작은 값"으로. `sum_to_n(n-1)`이 나머지를 알아서 해줄 거라 **믿고** n만 더함(러시아 인형).

**흐름 (sum_to_n(3)):** 들어갈 땐 쪼갬 `3+(2+(1))` → 바닥 1 찍고 → **나오면서 하나씩 더함** `1→3→6`.
"한 번에 3+2+1"이 아니라 **"안에서 바깥으로 되돌아 나오며 순차 계산"** — 이 in-and-out 흐름이 DFS의 뿌리.

**본인 설명 통과:** base case 필요성·쪼개짐·되돌아 합침을 스스로 정확히 설명. 첫 재귀치고 이해도 우수.

**→ 알고리즘 연결:** **재귀 = 3단계(DFS/DP)의 문.** "큰 문제 → 같은 모양의 작은 문제 + 끝에서 멈춤". DFS(끝까지 갔다 되돌아옴)·DP(작은 답으로 큰 답)가 다 재귀 위에 섬. 오늘 장난감(sum)이지만 구조는 트리 탐색·미로·조합 생성으로 확장.

---

## Day 20 — 리스트 합 (재귀 + 슬라이싱, ★★★)

**문제:** 리스트 합을 재귀로(for·sum 없이). `recursive_sum([1,2,3,4]) → 10`, `recursive_sum([]) → 0`

**내 풀이:**
```python
def recursive_sum(numbers):
    if not numbers:                                  # base case: 빈 리스트면 0
        return 0
    return numbers[0] + recursive_sum(numbers[1:])   # 첫 원소 + 나머지의 합(재귀)
```

**핵심 — "머리 + 꼬리" 재귀 패턴:**
- `numbers[0]`(머리) + `recursive_sum(numbers[1:])`(꼬리=나머지, 슬라이싱). 매번 한 칸씩 짧아지다 `[]`에서 멈춤.
- **재귀 + 슬라이싱 조합** (서로 다른 날 배운 두 도구가 맞물림).

**base case 설계 감각 (오늘의 깊이):** 어제 `n==1`은 0·음수 입력에서 무한 추락. 오늘 "빈 리스트"는 모든 입력이 반드시 `[]`로 수렴 → **빈 입력([])까지 자연 처리.** → **"끝 상태(빈 것)로 멈추는 게 특정 값으로 멈추는 것보다 안전."**

**→ 알고리즘 연결:** **리스트 재귀 표준 = "머리(첫 원소) + 꼬리(나머지)".** 합·뒤집기·최대·필터 다 이 틀로 재귀 가능. 나중에 트리/그래프 DFS("현재 노드 + 나머지 재귀")로 확장.

---

## Day 21 — 문자열 뒤집기 재귀 (★★★, 세 방식 비교)

**문제:** 문자열을 재귀로 뒤집기(`[::-1]`·for 없이). `reverse_recursive("hello") → "olleh"`

**내 풀이 (세 가지 — 재귀/반복문/슬라이싱):**
```python
def reverse_recursive(text):
    if text == "":                                   # base case: 빈 문자열
        return ""
    return reverse_recursive(text[1:]) + text[0]     # 나머지 뒤집고 + 첫 글자를 "뒤에"

def reverse_text_for(text):          # 반복문 (Day1 안 보고 재구성!)
    r = ""
    for t in text:
        r = t + r                    # 새 글자를 "앞에" 붙이기 (누적)
    return r

reverse_text_slicing = lambda: text[::-1]   # 슬라이싱 한 방
```

**오늘의 핵심 — 재귀에서 "위치가 결과를 바꾼다":**
- `재귀(text[1:]) + text[0]` → 첫 글자를 **뒤에** → 순서 반전(뒤집기)
- 만약 `text[0] + 재귀(text[1:])`였다면 → 순서 유지(Day20 합처럼). **첫 글자를 뒤로 미뤄야 뒤집힘.**
- 재귀 vs 반복문이 방향 정반대: 재귀는 "첫 글자 뒤로", 반복문은 "새 글자 앞으로". 같은 결과 다른 길.
- **Day1 반복문을 안 보고 재구성** = 20일 전 "앞에 붙이기 누적" 패턴이 손에 남음.

**→ 알고리즘 연결:** **"연산을 재귀 앞에 두냐 뒤에 두냐"가 결과를 바꿈.** 머리+재귀(순서 유지) vs 재귀+머리(순서 반전). 나중에 트리 순회(전위/후위)에서 그대로 등장하는 감각의 씨앗.

**→ 알고리즘 연결:** 방법 A = **상태관리 심화**(Day3 확장, 변수 2개 추적). 방법 B = **정렬(sorting) 첫 등장 → 2단계의 핵심 도구.** "줄 세우면 문제가 쉬워지는" 마법. 나중에 "정렬 기준 정하기"(점수순 등)까지 가면 주식 종목 정렬에 직결.
