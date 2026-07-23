# Python 학습 히스토리 — 캐슬타이거

> SKALA 입과 준비 / 프로그래밍 완전 처음부터 시작  
> 학습 방식: 개념 설명 → 직접 타이핑 → 실행 → 결과 공유 → 다음 단계

---

## Day 1 — 변수 / 자료형
**파일:** `day1.py`  
- 변수 선언, 문자열/숫자/불린 자료형
- `str()` 형변환, `print()` 출력
```python
name = "캐슬타이거"
score = 95.5
is_pass = True
```

---

## Day 2 — 조건문 (if / elif / else)
**파일:** `day2.py`  
- `if`, `else`, `elif` 구조
- 비교 연산자: `==`, `>=`, `<=`, `!=`
- `==` 과 `=` 의 차이 (비교 vs 대입)

---

## Day 3 — 반복문 (while / for)
**파일:** `day3.py`  
- `while` 루프, `count += 1`
- 1~10 합계 계산
- **실수 포인트:** `count += 1` 을 `if` 블록 안에 넣으면 무한루프 발생

---

## Day 4 — 함수 (def / return)
**파일:** `day4.py`  
- `def`, `return` 기본 구조
- `range()`, `%` 나머지 연산자로 짝/홀수 판별
- `print` vs `return` 차이 이해

---

## Day 5 — 리스트
**파일:** `day5.py`  
- 리스트 생성, `for item in list` 순회
- `len()`, 합계/평균 계산
- **실수 포인트:** `total += total + score` → `total += score` 가 맞음

---

## Day 6 — 딕셔너리
**파일:** `day6.py`  
- 딕셔너리 기본 구조 `{"key": value}`
- 딕셔너리 리스트 순회
- **실수 포인트:** `student("name")` → `student["name"]` (괄호 종류 주의)

---

## Day 7 — 문자열 / f-string
**파일:** `day7.py`  
- f-string 문법: `f"{변수}"`
- 중첩 따옴표 처리: `f"{student['name']}"`
- **실수 포인트:** `f"name님..."` → `{}` 없으면 변수가 아닌 문자열로 출력됨

---

## Day 8 — 파일 입출력
**파일:** `day8.py`  
- `open()`, `with ~ as f`, `f.write()`
- `encoding="utf-8"`, `"w"` 쓰기 모드
- **실수 포인트:** `f.write()` 는 인자 하나만 받음 (print처럼 여러 개 안 됨)

---

## Day 9 — 오류 처리 (try / except)
**파일:** `day9.py`  
- `try`, `except ValueError`, `finally`
- 문자열 리스트에서 숫자만 골라 합산
- **실수 포인트:** `except` 블록에서 존재하지 않는 변수명 사용 주의

---

## Day 10 — 클래스 / 메서드 (OOP)
**파일:** `day10.py`  
- `class`, `__init__`, `self`
- 인스턴스 생성, 메서드 호출
- `self.balance = self.balance + amount` (return 없이 값 변경)
- **실수 포인트:** `self.` 빠뜨리기, `return` 과 대입문 혼용

---

## Day 11 — 모듈
- `import math`, `import random`, `import datetime`
- `math.sqrt()`, `random.choice()`, `datetime.date.today()`

---

## Day 12 — pandas 기초
**파일:** `day12.py`  
- `import pandas as pd`
- `pd.DataFrame()`, `df["열"]`, `apply(lambda x: ...)`
- `to_csv()`, `read_csv()`, `encoding="utf-8-sig"`

---

## Day 13 — numpy
- `import numpy as np`
- `np.array()`, 통계함수 (`mean`, `sum`, `max`, `min`)
- 2D 배열, 불린 필터링

---

## Day 14 — pandas 심화
**파일:** `day14.py`  
- 새 열 추가: `df["총점"] = df["국어"] + df["수학"]`
- `df["매출"].sum()` (루프 없이 합계)
- **실수 포인트:** `df["총점"] = df["국어"] = df["수학"]` → `+` 로 연결해야 함

---

## Day 15 — pandas 고급
**파일:** `day15.py`  
- `groupby()`, `agg()`, `merge()`
- 복합 조건 필터링: `df[(조건1) & (조건2)]`
- **실수 포인트:** `&` 사용 시 각 조건을 `()` 로 감싸야 함

---

## Day 16 — matplotlib 시각화
**파일:** `day16.py`  
- `import matplotlib.pyplot as plt`
- `plt.rcParams['font.family'] = 'Malgun Gothic'` (한글 폰트)
- `df.plot(kind="bar"/"line"/"pie")`, `plt.show()`
- `plt.xticks(rotation=0)`, `plt.tight_layout()`
- **실수 포인트:** `import matplotlib as plt` → `matplotlib.pyplot as plt` 가 맞음  
  `plt.show` → `plt.show()` 괄호 필수  
  `marker="0"` → `marker="o"` (숫자 0이 아닌 알파벳 o)

---

## 연습 문제

### practice1~4 — pandas 기초 다지기
- DataFrame 생성, 열 추가, groupby, 필터링, 막대 그래프 기본 패턴 반복

### practice5 — 도서관 대출 데이터
- `groupby` + `agg("mean")` 두 열 동시
- 복합 조건 필터링 (`&`)
- `apply(lambda)` 로 인기도 열 추가
- **실수 포인트:** `&` 조건에서 두 번째 조건 `()` 빠뜨림

### practice6 — 쇼핑몰 고객 데이터
- 계산 열 추가: 순구매금액 = 총구매금액 - (반품횟수 × 50000)
- VIP 필터링 후 정렬
- **실수 포인트:** `"vip"` 소문자 → `"VIP"` 대문자

### practice7 — 온라인 강의 플랫폼
- `agg({"총매출": "sum", "평점": "mean"})` — 열마다 다른 집계 함수
- **실수 포인트:** 두 열에 다른 통계 쓸 때 딕셔너리 형태 필요

### practice8 — 영화 스트리밍 플랫폼
- lambda 3단계 조건: `"강력추천" if x >= 4.7 else "추천" if x >= 4.5 else "보통"`
- **실수 포인트:** lambda 안에서 `elif` 사용 불가 → `else ... if` 체이닝

### practice9 — 배달 앱 주문 분석
- `pd.merge(df1, df2, on="주문ID")` — 두 DataFrame 합치기 첫 실습
- 스스로 오류 발견하고 수정

### practice10 — 직원 성과 데이터 (결측값 처리)
- `isnull().sum()` — 결측값 개수 확인
- `fillna(df["열"].mean())` — 평균으로 결측값 채우기
- `fillna("미배정")` — 문자열로 채우기

### practice11 — 학원 수강생 종합 분석 (최종 복습)
- merge + fillna + groupby + 필터링 + lambda + sort + 그래프 전부 조합
- 오류 없이 첫 실행 통과

---

## agg() 문법 정리

```python
# 같은 통계를 여러 열에
df.groupby("카테고리")[["열1", "열2"]].agg("mean")

# 열마다 다른 통계
df.groupby("카테고리").agg({"열1": "sum", "열2": "mean"})
```

---

## 자주 실수한 패턴

| 실수 | 올바른 코드 |
|------|------------|
| `import matplotlib as plt` | `import matplotlib.pyplot as plt` |
| `plt.show` | `plt.show()` |
| `df["a"] = df["b"] = df["c"]` | `df["a"] = df["b"] + df["c"]` |
| `lambda x: "A" if x>90 elif x>80 "B"` | `lambda x: "A" if x>90 else "B" if x>80 else "C"` |
| `df[(조건1) & 조건2]` | `df[(조건1) & (조건2)]` |
| `f"name님"` | `f"{name}님"` |

---

---

## Flask 기초 (Day 17)
**파일:** `app.py`, `templates/index.html`, `templates/result.html`

### 핵심 개념
- `@app.route("/주소")` → 주소랑 함수 연결 (라우팅)
- `render_template("파일.html", 변수=값)` → HTML에 데이터 전달
- `request.form["name"]` → 폼 입력값 받기
- `debug=True` → 코드 저장 시 서버 자동 재시작

### Jinja2 템플릿 문법
| 문법 | 역할 |
|------|------|
| `{{ 변수 }}` | 변수 출력 |
| `{% for x in list %}` `{% endfor %}` | 반복 |
| `{% if 조건 %}` `{% endif %}` | 조건 |

### 카페 매출 대시보드 미니 프로젝트
- pandas DataFrame → Flask → HTML 테이블 출력
- matplotlib 차트 → `static/chart.png` 저장 → 웹에 표시
- `df.to_dict("records")` → Jinja2에서 다루기 쉬운 형태로 변환
- `matplotlib.use('Agg')` → 브라우저 없이 이미지 파일로 저장

```
app.py          → 데이터 처리 (pandas) + 라우트
templates/
  index.html    → 화면 출력 (Jinja2 테이블 + 차트)
static/
  chart.png     → matplotlib이 저장한 차트 이미지
```

---

## scikit-learn 입문
**파일:** `ml1.py`, `ml2.py`

### 핵심 개념
> 데이터로 패턴을 학습해서, 새로운 데이터의 값을 예측하는 것

```
데이터 준비 → train_test_split → model.fit(학습) → model.predict(예측) → accuracy_score
```

### 선형 회귀 (ml1.py)
- 숫자를 예측하는 모델 (공부시간 → 점수)
- `LinearRegression` 사용
- **주의:** 학습 데이터 범위를 벗어나면 현실과 맞지 않는 값 나올 수 있음 (106.5점)

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y)
model.predict([[9]])
```

### 분류 - Decision Tree (ml2.py)
- 카테고리를 예측하는 모델 (합격/불합격)
- `feature_importances_` 로 변수별 영향력 확인

```python
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X, y)
model.predict(...)
```

### 학습/테스트 분리
```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
accuracy_score(y_test, model.predict(X_test))
```

> **핵심:** 모델은 데이터의 패턴을 학습할 뿐, 현실의 진실을 학습하는 게 아니다.

---

## 클래스 연습 (class_practice.py)
- Book 클래스: `__init__`, `borrow()`, `return_book()`, `info()`
- **실수 포인트:** `self.is_available = True` 는 파라미터가 아닌 `__init__` 바디에 작성
- `return` 과 대입문은 한 줄에 쓸 수 없음
- f-string 에 `self.` 접두사 필요: `f"{self.title}"`

---

## Gemini API 연동 시도
**파일:** `gemini_test.py`

```python
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="질문"
)
print(response.text)
```

- 패키지: `pip install google-genai` (구버전 `google-generativeai` 는 deprecated)
- 무료 티어 한도 이슈로 실행 실패 → 구조는 이해함
- **보안 주의:** API 키를 코드에 직접 넣으면 GitHub 푸시 시 차단됨

---

## GitHub
- `git init` → `git add .` → `git commit -m "메시지"` → `git push`
- 코드 변경 후 업데이트: `git add .` → `git commit -m "메시지"` → `git push`
- 레포지토리: `github.com/castle0tiger/python-practice`
- **보안 주의:** API 키를 코드에 직접 넣으면 GitHub 푸시 시 차단됨 → `"YOUR_API_KEY"` 로 대체

---

## Groq API + Flask 챗봇
**파일:** `groq_test.py`, `chatbot.py`, `templates/chat.html`

### 작동 구조
```
브라우저 (입력)
    ↓ POST /chat
chatbot.py → conversation 리스트에 추가 → Groq API 호출
    ↓ 응답
conversation에 assistant 답변 추가 → chat.html 렌더링
    ↓
브라우저 (출력)
```

### 핵심 개념
- `conversation` 리스트가 대화 기록 전체를 쌓아가며 AI가 맥락을 기억하는 것처럼 동작
- `role`: `"user"` (사용자), `"assistant"` (AI), `"system"` (행동 지침)
- LLM은 학습 데이터 컷오프(cutoff) 이후 정보는 모름

### API 키 보안 관리 (.env)
```
# .env 파일
GROQ_API_KEY=실제키값

# 코드에서 불러오기
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
```
- `.gitignore` 에 `.env` 추가 → GitHub에 키 노출 방지
- **실수 포인트:** API 키 코드에 직접 입력 시 GitHub push 차단됨

---

## Flask DB 연결 (SQLite)
**파일:** `app_db.py`, `templates/guestbook.html`

### 핵심 개념
> app_db.py = DB 관리자 + 브라우저 연결자

```
클라이언트 (브라우저)
    ↓ 입력
app_db.py  →  DB 저장 (INSERT)
           →  DB 조회 (SELECT)
           →  HTML로 변환해서 브라우저에 전달
    ↓ 출력
클라이언트 (브라우저)
```

### DB 기본 명령어
| 코드 | 역할 |
|------|------|
| `sqlite3.connect("파일.db")` | DB 연결 (없으면 자동 생성) |
| `CREATE TABLE IF NOT EXISTS` | 테이블 없으면 생성 |
| `INSERT INTO` | 데이터 저장 |
| `SELECT *` | 데이터 전체 불러오기 |
| `conn.commit()` | 변경사항 확정 |
| `conn.close()` | 연결 종료 |

### DB vs CSV 비교
- pandas `to_csv()` / `read_csv()` 와 같은 개념
- DB가 csv보다 더 안전하고 빠른 저장소
- `guestbook.db` 파일은 `init_db()` 실행 시 자동 생성

---

## 클라우드 배포 (Render)
**배포 URL:** `https://python-practice-rmyn.onrender.com`

### 배포 준비 파일
```
requirements.txt  →  필요한 패키지 목록
gunicorn          →  프로덕션 서버 (로컬의 flask run 대신)
```

### 배포 과정
1. `requirements.txt` 생성 (flask, groq, python-dotenv, gunicorn)
2. `chatbot.py` 포트 환경변수 설정: `os.environ.get("PORT", 5002)`
3. GitHub 푸시
4. Render → New Web Service → GitHub 레포 연결
5. Build Command: `pip install -r requirements.txt`
6. Start Command: `gunicorn chatbot:app`
7. Environment Variables에 `GROQ_API_KEY` 추가
8. Deploy

### 로컬 vs 배포 차이
```
로컬:    http://127.0.0.1:5002  (내 컴퓨터에서만 접속)
배포 후: https://python-practice-rmyn.onrender.com  (누구나 접속 가능)
```

> **주의:** Render 무료 티어는 비활성 시 50초 딜레이 발생

---

---

## 통계 기초
**파일:** `stats1.py`

### 핵심 개념 4가지

| 개념 | 의미 | pandas 함수 |
|------|------|-------------|
| 평균(Mean) | 데이터의 중심값 | `.mean()` |
| 분산(Variance) | 평균에서 얼마나 흩어졌나 | — |
| 표준편차(Std) | 분산의 제곱근, 단위 복원 | `.std()` |
| 상관관계(Correlation) | 두 변수가 같이 움직이는 정도 | `.corr()` |

### 핵심 함수

```python
df.describe()   # 평균/표준편차/최소/최대 한번에 요약
df.corr()       # 변수 간 상관관계 수치로 확인
```

### 상관관계 해석
```
+1에 가까울수록 → 같이 올라감 (공부시간↑ 점수↑)
-1에 가까울수록 → 반대로 움직임 (결석수↑ 점수↓)
 0에 가까울수록 → 관계없음
```

### 실습 결과
```
공부시간 ↔ 시험점수: 0.98  → 강한 양의 상관관계
공부시간 ↔ 결석횟수: -0.95 → 강한 음의 상관관계
```

### ML과의 연결
- 선형회귀(ml1.py)는 산점도에 직선 하나를 긋는 것
- 상관관계가 높을수록 → 직선이 잘 맞음 → 예측 정확도 높음
- **ML 하기 전에 `.corr()` 로 변수 관계 먼저 확인하는 것이 표준 순서**

> **핵심:** 공식 외울 필요 없음. pandas가 다 해줌. 목적과 해석만 알면 됨.

---

---

## RAG (Retrieval-Augmented Generation)
**파일:** `09_rag/rag1.py`, `09_rag/rag2.py`, `09_rag/company_rules.txt`

### 핵심 개념
> AI가 학습한 것 외에, 내가 준 문서에서도 답변하게 만드는 기술

### 동작 구조
```
[내 컴퓨터 - 로컬]
1. 문서 로드 (company_rules.txt)
2. 청크 분리 (문단 단위)
3. 임베딩 변환 → 각 청크를 숫자 벡터로
4. 질문 입력
5. 질문도 임베딩 변환
6. 코사인 유사도 계산 → 관련 청크 선별

[인터넷 - API 호출]
7. 관련 청크 + 질문 → Groq 전달
8. Groq이 자연스러운 문장으로 답변 생성
```

### rag1.py vs rag2.py 비교

| 구분 | rag1.py (키워드) | rag2.py (임베딩) |
|------|-----------------|-----------------|
| 방식 | 단어 글자 비교 | 의미 벡터 비교 |
| "휴가" → "연차" | 실패 | 성공 (유사도 0.68) |
| 속도 | 빠름 | 느림 (신경망 계산) |
| 토큰 소모 | 동일 | 동일 |

### 임베딩(Embedding)
```
"연차"  → [0.2, 0.8, 0.1, ...]
"휴가"  → [0.3, 0.7, 0.2, ...]  ← 의미가 비슷 → 벡터도 비슷
"급여"  → [0.9, 0.1, 0.8, ...]  ← 의미가 다름 → 벡터도 다름
```
- 모델: `paraphrase-multilingual-MiniLM-L12-v2` (한국어 지원)
- 첫 실행 시 모델 다운로드(471MB), 이후 캐시에서 로드

### 역할 분담
```
sentence-transformers  →  내 컴퓨터 계산 (전기세만 듦)
Groq API              →  외부 서버 계산 (토큰 소모)
```
- Groq은 질문당 1번 호출 (4개 질문 → 4번 호출)
- RAG는 관련 청크만 골라 전달 → 토큰 절약 + 정확도 향상

### 라이브러리
```
pip install sentence-transformers
```

---

---

## HTML/CSS 기초
**파일:** `10_html_css/index.html`, `06_ai_api/templates/chat.html`

### HTML — 구조 (뼈대)
```html
<!DOCTYPE html>
<html>
<head>  <!-- 브라우저 설정 (제목, 스타일) -->
  <title>제목</title>
</head>
<body>  <!-- 실제 화면에 보이는 내용 -->
  <h1>제목</h1>
  <p>문단</p>
  <ul><li>목록</li></ul>
  <div>구역 나누기</div>
</body>
</html>
```

### CSS — 디자인 (스타일)
```css
/* 선택자 { 속성: 값; } */
h1 { color: blue; }          /* 태그 선택 */
.card { padding: 20px; }     /* class 선택 */
#title { font-size: 24px; }  /* id 선택 */
```

### 자주 쓰는 CSS 속성
| 속성 | 역할 |
|------|------|
| `color` / `background-color` | 글자/배경 색 |
| `padding` / `margin` | 안쪽/바깥쪽 여백 |
| `border-radius` | 모서리 둥글게 |
| `box-shadow` | 그림자 |
| `display: flex` | 가로 정렬 |
| `max-width` / `margin: auto` | 가운데 정렬 |

### CSS 작성 위치
```
방법 1 (인라인):  HTML <head> 안에 <style> 태그로 작성
방법 2 (분리):   style.css 파일 따로 만들고 <link>로 연결 → 실제 서비스 표준
```

### 실습 결과
- `index.html`: 순수 HTML → CSS 추가 후 카드 레이아웃으로 변환
- `chat.html`: 디자인 없는 챗봇 → 말풍선 UI로 변환
  - 내 메시지: 오른쪽 파란 말풍선
  - AI 메시지: 왼쪽 회색 말풍선

> **핵심:** HTML은 구조, CSS는 디자인. Flask의 `static/` 폴더가 CSS 파일을 두는 곳.

---

---

## Prompt Engineering
**파일:** `12_prompt/prompt1.py`

### 핵심 개념
> 어떻게 질문하느냐에 따라 AI 답변 품질이 완전히 달라진다

### 3가지 기법

| 기법 | 방법 | 효과 |
|------|------|------|
| System Prompt | "너는 ~야" 역할 설정 | 톤/대상/성격 제어 |
| Few-shot | 원하는 형식 예시 제공 | 출력 형식 완벽 제어 |
| Chain of Thought | "단계별로 생각해" | 복잡한 문제 정확도 향상 |

### 코드 구조
```python
client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {"role": "system", "content": "너는 초등학생 선생님이야"},  # 역할 설정
        {"role": "user", "content": "파이썬 리스트가 뭐야?"}
    ]
)
```

### 핵심 이해
```
일반 사용자  →  채팅창에 직접 입력 (매번 수동)
개발자       →  System Prompt에 고정 (모든 사용자 자동 적용)
```
Claude/ChatGPT/Gemini 채팅창에서 하는 프롬프트 작성과 완전히 동일한 원리.
AI 서비스 개발자는 사용자 대신 최적의 프롬프트를 미리 설계해두는 역할.

---

---

## LangChain
**파일:** `13_langchain/lc1.py`

### 핵심 개념
> LLM 호출, RAG, 체인 연결을 단순화해주는 프레임워크

### 기존 방식 vs LangChain 비교
```python
# 기존 Groq 직접 호출
response = client.chat.completions.create(...)
answer = response.choices[0].message.content  # 길고 복잡

# LangChain
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=...)
response = llm.invoke(messages)
answer = response.content  # 간결
```

### Chain 핵심 문법
```python
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "너는 Python 강사야. 한국어로 간결하게 설명해."),
    ("human", "{topic}이 뭐야? 세 줄로 설명해줘.")
])

chain = prompt | llm  # | 기호로 프롬프트 + LLM 연결

chain.invoke({"topic": "Flask"})   # 변수만 바꿔서 재사용
chain.invoke({"topic": "RAG"})
```

### 핵심 정리
```
| 기호  →  프롬프트와 LLM을 연결 (Chain)
템플릿 →  한 번 만들고 변수만 교체해서 재사용
```
- 라이브러리: `pip install langchain langchain-groq`
- 실제 LangChain은 여기에 RAG, 메모리, 에이전트까지 확장 가능

---

## FastAPI
**파일:** `14_fastapi/main.py`

### FastAPI란?
> Python으로 만드는 백엔드 API 서버 프레임워크
> 프론트엔드(HTML/앱)와 AI/DB 사이에서 교통정리 역할

```
[프론트엔드]    →    [FastAPI]    →    [AI / DB]
HTML 화면            중간 처리          Groq, SQLite
모바일 앱            라우팅
```

### Flask vs FastAPI
| 항목 | Flask | FastAPI |
|------|-------|---------|
| 용도 | HTML 페이지 서빙 | API 서버 (JSON 반환) |
| 문서 | 없음 | `/docs` 자동 생성 |
| 데이터 검증 | 수동 | Pydantic 자동 |

### 핵심 문법

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# GET 요청
@app.get("/경로")
def 함수():
    return {"key": "value"}  # 자동으로 JSON 반환

# POST 요청 - 데이터 받기
class 요청모델(BaseModel):
    field1: str          # 필수
    field2: str = "기본값"  # 선택

@app.post("/경로")
def 함수(request: 요청모델):
    return {"결과": request.field1}

# Path 파라미터 - URL에서 값 받기
@app.get("/history/{user_name}")
def 함수(user_name: str):
    return {"사용자": user_name}

# DELETE 요청
@app.delete("/history/{user_name}")
def 함수(user_name: str):
    return {"message": "삭제 완료"}
```

### 서버 실행
```
python -m uvicorn 14_fastapi.main:app --reload --port 8000
```
- `--reload`: 코드 저장 시 자동 재시작
- `/docs`: Swagger UI 자동 생성 (테스트 가능)

### HTTP 메서드
| 메서드 | 역할 | 예시 |
|--------|------|------|
| GET | 데이터 조회 | 대화 기록 보기 |
| POST | 데이터 전송/생성 | 질문 보내기 |
| DELETE | 데이터 삭제 | 기록 초기화 |

### 대화 기록 (in-memory)
```python
conversations = {}  # { "사용자이름": [메시지 리스트] }

# 매 요청마다 전체 대화 기록을 Groq에 전달 → AI가 맥락 기억
messages = [{"role": "system", "content": "..."}] + conversations[user_name]
```
- **단점:** 서버 재시작 시 초기화됨 → 영구 저장하려면 SQLite 필요 (11_project 방식)

### HTTP 상태 코드
| 코드 | 의미 |
|------|------|
| 200 | 성공 |
| 404 | 찾을 수 없음 |
| 422 | 데이터 형식 오류 (Pydantic 자동 처리) |
| 500 | 서버 내부 오류 |

---

## HTML ↔ FastAPI ↔ AI 전체 흐름 연결
**파일:** `14_fastapi/main.py`, `14_fastapi/static/index.html`

### 완성된 흐름
```
브라우저 index.html
    ↓ fetch('/ask', POST)   ← JavaScript가 서버에 요청
FastAPI /ask 엔드포인트
    ↓ Groq API 호출
AI 답변 JSON 반환
    ↓
JavaScript가 받아서 화면에 표시 (페이지 새로고침 없음)
```

### HTML 파일의 3가지 구성
```html
<style>  ... </style>   ← CSS (디자인)
<body>   ... </body>    ← HTML (화면 구조)
<script> ... </script>  ← JavaScript (동작)
```

### fetch() — JS에서 서버에 HTTP 요청 보내기
```javascript
const response = await fetch('/ask', {
    method: 'POST',                              // POST 요청
    headers: { 'Content-Type': 'application/json' },  // JSON 형식임을 알림
    body: JSON.stringify({ question: question, user_name: '사용자' })  // 보낼 데이터
});
const data = await response.json();  // 응답 JSON 파싱
// data.AI답변 으로 AI 답변 꺼내서 화면에 표시
```
- `await` = 응답 올 때까지 기다려
- `/docs`에서 손으로 했던 것과 동일한 요청을 코드로 자동화한 것

### FileResponse — HTML 파일을 응답으로 보내기
```python
from fastapi.responses import FileResponse

@app.get("/")
def home():
    return FileResponse("static/index.html")
    # JSON 대신 HTML 파일 자체를 브라우저에 전송
```

### Flask vs FastAPI 핵심 차이
| | 화면 그리는 곳 | 반환값 |
|---|---|---|
| Flask | 서버 (Jinja2 템플릿) | HTML 완성본 |
| FastAPI | 브라우저 (JavaScript) | JSON 데이터 |

### FastAPI가 중요한 이유
```
FastAPI /ask 엔드포인트 하나로
→ 웹 브라우저에서 연결 가능
→ 모바일 앱에서도 연결 가능
→ 다른 서버에서도 연결 가능
→ React 등 어떤 프론트엔드에서도 연결 가능
```
Groq API 자체가 FastAPI 방식 — JSON으로 어디서든 호출 가능.
Flask는 웹 페이지 하나용, FastAPI는 여러 곳과 연결하는 API 서버용.

---

## 다음 학습 계획

**최종 목표: AI 서비스를 직접 만들고 배포할 수 있는 사람**

- [x] Flask 기초 + 미니 프로젝트
- [x] scikit-learn 입문
- [x] 클래스 연습
- [x] GitHub 세팅
- [x] Flask DB 연결 (SQLite)
- [x] AI API 연동 (Groq + Flask 챗봇)
- [x] .env API 키 관리 + .gitignore
- [x] 클라우드 배포 (Render)
- [x] 통계 기초 (describe, corr, 산점도)
- [x] RAG (키워드 방식 → 임베딩 방식)
- [x] HTML/CSS 기초
- [x] 종합 프로젝트 (Python 학습 Q&A 챗봇)
- [x] Prompt Engineering
- [x] LangChain
- [x] FastAPI
- [x] HTML ↔ FastAPI ↔ AI 전체 흐름 연결
- [x] ChromaDB (벡터 DB)

---

## 백지 재구축 (LEARNING_RULES.md 방식)

### Day 1 — 리스트/딕셔너리 재구축 (practice1, 1b, 1c)
**한 것:** 학생 성적 관리 + 카페 판매 데이터 — 비교·갱신(최고/최저값), 누적 합계, 복합 조건(and), f-string 출력을 백지에서 직접 작성. VSCode AI 자동완성 끔.
**약했던 부분:** `+=` vs `=` 혼동 (Day 5에 이어 반복 실수 — 누적과 교체 구분), f-string 문법 기억 안 남, 변수명 오타·부정확(highst, first_name), 출력 형식 미준수.
**다음 할 것:** 세션 시작 시 `+=` vs `=` 미니 드릴 → 과제 2: pandas CSV 분석 (practice2.py + students.csv).

### Day 2 — `+=` 드릴 + pandas CSV 재구축 (practice2)
**한 것:** `+=` vs `=` 미니 드릴 통과(누적/교체 구분 확립). students.csv 직접 작성 → read_csv, mean(), 불린 필터링 재구축. FileNotFoundError(경로)와 KeyError(헤더 공백 " score")를 에러 메시지 읽고 df.columns로 직접 진단·해결.
**약했던 부분:** 변수명 무지성 복사(expensive — 2회째 네이밍 지적), 불린 필터의 "True/False 목록을 만든다"는 중간 단계 설명 부족, 출력 라벨 누락.
**다음 할 것:** 과제 3 — FastAPI 재구축 (Flask 대체: 사용자 스택 기준으로 커리큘럼 변경).

### Day 2 (계속) — 과제 3-A: FastAPI 서버 + GET 엔드포인트 (api1.py)
**한 것:** FastAPI 서버를 백지에서 구성 (`app = FastAPI()`, `@app.get`, JSON 반환, uvicorn 실행). `/`와 `/scores`(누적 패턴으로 평균 계산) 완성.
**배운 것:** 404(주소에 함수 없음) vs 500(코드 실행 중 사망 → 서버 터미널 traceback 확인). f-string 밖의 `{}`는 set이 됨. `sum` 내장 함수 shadowing과 "이름 변경은 사용처까지 전부" 원칙.
**다음 할 것:** 과제 3-B — POST + BaseModel로 데이터 받기.

### Day 3 — 과제 3-B: POST + BaseModel (api1.py /register)
**한 것:** RegisterRequest(BaseModel) 정의 → POST /register에서 합격 판정(if/else + 단일 return). 422 검문소 2개(json_invalid vs int_parsing)를 직접 실험으로 구분. 초기화 필요 판단 기준("변수가 안 만들어지는 길이 있나") 학습.
**약했던 부분:** attendance(출석)/absence(결석) 의미 혼동 재발(필드명을 라벨에 맞춰버림), if만 있고 else 없이 불합격 응답 누락했었음.
**다음 할 것:** 과제 3-C — HTML + fetch 연결 (3조각 분해: C-1 FileResponse → C-2 HTML+JS 버튼 → C-3 fetch 연결). 컨디션 좋은 날 시작 권장.

### Day 4 — 과제 3-C-1, 3-C-2: HTML 서빙 + JS 첫 작성 (chat.html, /page)
**한 것:** GET /page + FileResponse로 HTML 서빙(C-1). JS 첫 작성(C-2): id로 부품 찾기(getElementById) → .value 읽기 → .innerHTML += 로 화면에 쌓기 → 빈 입력 차단(if+return)과 입력창 비우기의 배치를 실행 순서 논리로 직접 판단. getElementByld 오타를 F12 Console 읽고 해결.
**약했던 부분:** HTML/JS 문법이 완전 처음이라 "작동 논리를 어디에 어떻게 쓰는지" 감 잡는 데 시간 소요. 문법 카드만으론 부족했고 STEP별 분해가 필요했음 (본인 피드백).
**다음 할 것:** 과제 3-C-3 — fetch로 /register 연결 (3-C 최종 관문, 비동기 개념 등장). 맑은 머리로 시작.

### Day 5 — 과제 3-C-3: fetch 연결 완성 (3-C 전체 완료!)
**한 것:** STEP 분해로 fetch 정복 — GET /scores 몸풀기 → POST 포장(method/headers/body+JSON.stringify) → 입력값 연결 → 응답을 화면에 쌓기. 화면→서버→화면 완전 순환을 백지에서 완성. ReferenceError를 콘솔 읽고 자가 해결. 개념 질문 다수: GET/POST vs git, body 포장법 3종(JSON/form/multipart), JS 객체 = 파이썬 딕셔너리 + 점표기, /page(화면 배달) vs fetch(대화)의 구분.
**약했던 부분:** 조립형 과제는 아직 부담 (STEP 분해 필수 유지). 변수명 선언-사용 불일치 재발(score vs scoreBox — 콘솔로 자가 해결한 건 성장). 학습 속도에 대한 자신감 저하 호소 → 기록 기반으로 반박해줌.
**다음 할 것:** 과제 4 — Groq 챗봇 API 재구축 (14_fastapi/main.py 완전 재구축) → 중간 점검(함수/클래스/데코레이터) → agent01.py 졸업 시험.

### Day 6 — 과제 4-A, 4-B: Groq 호출 단독 성공 + POST /ask (ai1.py, api1.py)
**한 것:** Groq 심장을 격리 테스트(ai1.py: .env 로드 → 클라이언트 → create → 응답 까기) 후 서버에 이식(POST /ask). 에러 4개 자가 경험: 값 증발(print 없는 홀로 선 표현식), 함수 밖 들여쓰기 NameError(in <module> 읽는 법), uvicorn 자리표시 대괄호, 모듈 경로에 .py 붙임. import/from/as 3형제, client 함수 밖 배치 이유, response 상자 구조(choices 리스트인 이유, 보낸 카드와 받은 카드의 {role, content} 대칭) 학습.
**약했던 부분:** 함수 소속(들여쓰기)과 지역 변수 개념이 처음 정면 등장 — 아직 낯섦. create 블록 들여쓰기 정리 습관. "개발자는 이 코드를 암기하나?" 질문 → 구조의 감 + 오픈북이 실무 방식임을 확인.
**다음 할 것:** 과제 4-C — 대화 기록(assistant 카드를 append해서 맥락 기억) → 4-D — chat.html을 /ask에 연결하면 챗봇 완성.

### Day 7 — 과제 4-C: 대화 기록 완성 (api1.py, groq_memory)
**한 것:** 전역 리스트 groq_memory에 user/assistant 카드 축적 → [system] + 기록으로 대본 조립 → AI가 이름을 기억함(금붕어 탈출). 버그 2개를 단서로 추적: ①누적대화수 홀수(3) → assistant 카드를 사본(script)에 적어 증발 ②500 → `groq_memory += [...]`가 대입문이라 지역 변수 취급(UnboundLocalError) → append로 해결.
**배운 것:** 전역 변수(로비 게시판) vs 지역 변수(회의실 화이트보드) 개념 첫 정면 학습 — 3규칙: 전역 읽기/부탁은 자유, 지역은 요청 끝나면 증발, 함수 안 대입은 지역 취급이라 전역 리스트 추가는 반드시 .append(). 숫자 패턴(홀짝)이 버그 단서가 됨.
**다음 할 것:** 과제 4-D — chat.html의 fetch를 /ask로 연결 (백지 챗봇 완성) → 중간 점검(함수/클래스/데코레이터).

### Day 8 — 과제 4-D: 챗봇 화면 연결 (과제 4 전체 완성 🎉)
**한 것:** chat.html을 /register에서 /ask로 갈아끼움 (서버는 무수정) — 입력창 1개, body {question}, 응답 data["답변"]을 "나:/AI:" 두 줄로 화면에 축적. 화면 너머로 대화 기억 작동 확인. **이로써 14_fastapi(서버+화면+AI+기억)를 백지에서 완전 재구축 완료.**
**에러 여정:** ①undefined 표시 → response(상자) vs data(알맹이) 혼동 + 없는 키(.value) 접근 (JS는 KeyError 대신 조용히 undefined) ②SyntaxError(문자열 이음새 + 누락) → script 전체 무력화로 "send is not defined" 2차 에러까지 (에러 개수 ≠ 범인 수) ③홀로 선 식 증발 재발견.
**다음 할 것:** 중간 점검 — 함수/클래스/데코레이터 정면 학습 (객체 개념, 사용자 대기 중) → agent01.py 졸업 시험(10줄 중 8개) → Docker.

### Day 9 — 중간 점검: 클래스 직접 만들기 (class1.py, class2.py)
**한 것:** 워밍업 "자기 말로 꺼내기" 1호 통과(객체=값+기능 꾸러미, 리스트도 객체임을 스스로 발견). 5-A 자판기 클래스(__init__/self/메서드, 거스름돈 경계값 버그 예측으로 발견) → 5-B 붕어빵 독립성(객체마다 칸 따로) → 5-C ChatMemory 클래스(groq_memory 로직을 클래스로 승격, print 메서드가 아닌 return 메서드 첫 작성).
**약했던 부분:** 전역 리스트 → self.칸 연결에서 한 번 막힘(대응표로 해소). append에 이중 포장([{}]), return값 증발 재발(오늘만 3회 — 패턴 인지는 빨라지는 중). 예측 훈련 2호 가동: 순서 예측 틀림 → 코드에서 원인 자력 발견.
**다음 할 것:** 데코레이터(@app.post, @tool의 정체) → agent01.py 졸업 시험 → Docker.

### Day 10 — 과제 5-D: StudyLog 클래스 (복습) + 개념사전 확장
**한 것:** 클래스 골격을 혼자 힘으로 작성 (5-C에서 막혔던 self.칸 초기화가 처음부터 나옴). 누적 패턴(total_hours)을 클래스 안에서 완벽 재현. best_subject의 "반복문 안 return" 버그를 데이터 순서 바꾸는 실험으로 직접 확인 후 수정 — "return은 함수 즉시 종료", "테스트 데이터가 버그를 숨길 수 있다"(거스름돈 사건에 이어 2회차). GLOSSARY의 객체/클래스/객체지향 항목을 비전공자 이해 기준으로 대폭 확장 (분량 규칙 변경: 짧게 < 혼자 읽어도 이해되게).
**약했던 부분:** 반복문 안 return 위치 (비교·갱신 패턴에서 발표는 심사 끝난 뒤), 축약 변수명(bs) 습관.
**다음 할 것:** 데코레이터(@app.post, @tool의 정체 — 중간 점검 마지막 조각) → agent01.py 졸업 시험(10줄 중 8개) → Docker.

### Day 11 — 몸풀기(ExpenseBook) + 데코레이터 (중간 점검 완료)
**한 것:** 5일 공백 후 몸풀기 ExpenseBook 클래스 — 골격 노힌트 작성, biggest()의 반복문 안 return 함정을 이번엔 처음부터 회피(지난 버그가 학습으로 전환됨). over() 보너스로 "수집 패턴"(빈 리스트에 조건 맞는 것만 append 후 return) 첫 작성, 리스트에 딕셔너리 접근 TypeError 자가 진단. 데코레이터 정면 학습: deco1.py(@는 정의 순간 실행, 호출과 별개) → deco2.py(나만의 @tool 만들기 — 함수도 리스트에 담기는 객체, tools=[calculator,...]의 정체).
**오늘의 3대 발견:** ①함수도 객체다(리스트에 담고 t()로 실행) ②@ = 정의 즉시 배달(등록 ≠ 호출) ③return 없으면 None 반환 / print와 return은 다른 일(return total and print(total) 실험으로 확인).
**약했던 부분:** print(보여주기) vs return(값 돌려주기) 혼동 — 한 줄에 섞으면 안 됨. 실무는 계산은 return만, 출력은 받은 쪽에서 따로.
**다음 할 것:** agent01.py 졸업 시험(아무 줄 10개 중 8개 설명) → 통과 시 백지 재구축 졸업 → Docker로 튜토리얼 재개.

### Day 12 — RAG/ChromaDB 개념 정리 + 미니 재구축 ① (rag1.py)
**한 것:** RAG 전체 지도 정리(준비=저장 / 찾기=ChromaDB / 답쓰기=AI, 세 역할 분리 — GLOSSARY 확장). rag1.py 조립(A방식: 카드+상세설명): 문서→청크→ChromaDB 저장→query 검색→찾은청크+질문 f-string 조립→Groq 답변. "연차 며칠 쓸 수 있어?"(문서에 없는 표현)로 [휴가규정] 검색 성공 = 의미검색 확인.
**에러/발견:** ①documents 오타(에러가 Did you mean 알려줌) ②Default 임베딩=영어위주라 [재택] 오검색 → 다국어 모델(paraphrase-multilingual-MiniLM-L12-v2)로 교체하니 [휴가] 정확 검색 = RAG 튜닝의 핵심은 임베딩 모델 선택 ③모델명 오타(대소문자/버전) 401 → 긴 에러는 맨위(내코드)+맨아래(진짜원인)만 읽기. 타이핑은 로직만, 고정문자열(모델명/URL/키)은 복붙.
**개념 심화:** "이해했다의 선" 논의 — 목표 레벨 = "이 줄이 뭘 하고 지우면 뭐가 깨지는가"까지. 내부구현/알고리즘/수학은 선 아래(안 파도 됨). chromadb.Client()=클래스(틀), client_db.create_collection()=객체의 메서드 구분을 스스로 정확히 해냄. 라이브러리를 객체+메서드 언어로 읽기 시작.
**다음 할 것:** 미니 재구축 ② LangChain(lc1.py 재활용) → agent01.py 졸업 시험 → Docker.

### Day 13 — 미니 재구축 ② LangChain + 🎓 졸업 시험 통과 (lc1.py)
**한 것:** 워밍업(RAG 역할 분리) 통과. LangChain 4단계: ChatGroq으로 llm 객체 → ChatPromptTemplate로 프롬프트 틀({topic} 빈칸) → 파이프(|)로 chain 조립 → 반복문으로 chain 재사용. 우연히 "손으로 잇기(prompt.invoke→llm.invoke) vs 파이프" 비교 실험이 파일에 나란히 남음.
**핵심 이해:** LangChain은 새 마법이 아니라 직접 하던 걸 부품으로 포장한 것. .invoke()는 모든 LC 부품의 공용 실행 명령. prompt.invoke()는 AI 호출이 아니라 질문지 완성 단계(SystemMessage/HumanMessage = 어제의 role/content 딕셔너리와 같은 것). 노란 Warning=계속 감 / 빨간 Traceback=멈춤.
**🎓 졸업 시험 (agent01.py 10줄, 무참고):** 최종 9.5/10 통과. 정답 7개(import, ChatGroq, PersistentClient, 임베딩 모델, query, tools 리스트, create_react_agent) + 재답변으로 3개 교정(@tool=등록≠실행 / docstring=AI가 읽는 도구 설명서 / join=리스트를 문자열 하나로 합치기).
**의미:** 7월 초 "함수 안이 이해 안 된다"던 파일을 아무것도 안 보고 설명함. 특히 자기가 만든 것(deco2.py toolbox, 자판기 클래스, 어제 오검색 사건)으로 남의 코드를 설명 — 재구축의 목적 달성.
**다음 할 것:** 백지 재구축 졸업 → Docker로 튜토리얼 재개.
