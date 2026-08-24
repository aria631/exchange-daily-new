import os
from datetime import datetime, timezone, timedelta
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def main():
    date = datetime.now(timezone.utc).astimezone(
        timezone(timedelta(hours=8))
    ).strftime("%Y-%m-%d")

    prompt = f"""
生成 {date} 的《交易所 & 股票今日动态》。

结构：
1. 交易所动态 Top 3
2. 其他交易所重大事件
3. 美股热点 Top 3
4. 韩股热点 Top 3
5. 今日结论

要求：
- 中文
- 普通人易懂
- 不包含建议和行动项
- 关注 Coinbase、Robinhood、Bullish、Binance、OKX、Kraken、Bybit、Gate、Bitget、MEXC、
  美股和韩股热点。
"""

    r = client.responses.create(
        model="gpt-5",
        input=prompt
    )

    Path("reports").mkdir(exist_ok=True)
    Path(f"reports/{date}.md").write_text(
        r.output_text,
        encoding="utf-8"
    )

if __name__ == "__main__":
    main()
