from flask import Flask, render_template
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

app = Flask(__name__)

plt.rcParams['font.family'] = 'Malgun Gothic'

data = {
    "메뉴": ["아메리카노", "라떼", "카푸치노", "에이드", "스무디", "케이크", "샌드위치"],
    "카테고리": ["커피", "커피", "커피", "음료", "음료", "푸드", "푸드"],
    "판매수량": [150, 120, 80, 60, 45, 90, 70],
    "단가": [3000, 4000, 4500, 4000, 5000, 5500, 6000]
}

df = pd.DataFrame(data)
df["총매출"] = df["판매수량"] * df["단가"]

@app.route("/")
def home():
    table = df.to_dict("records")
    
    summary = df.groupby("카테고리").agg({"총매출": "sum", "판매수량": "sum"}).reset_index()
    summary_table = summary.to_dict("records")
    
    summary.plot(kind="bar", x="카테고리", y="총매출", title="카테고리별 총매출", legend=False)
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.savefig("static/chart.png")
    plt.close()

    return render_template("index.html", table=table, summary_table=summary_table)

if __name__ == "__main__":
    app.run(debug=True)

