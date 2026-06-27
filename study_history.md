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
- [ ] Prompt Engineering
- [ ] LangChain
- [ ] FastAPI
