import requests
import json
import os
import time


def build_url(symbol: str, period1: int, period2: int) -> str:
    return (f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?"
            f"events=capitalGain%7Cdiv%7Csplit&formatted=true"
            f"&includeAdjustedClose=true&interval=1d"
            f"&period1={period1}&period2={period2}"
            f"&symbol={symbol}&userYfid=true&lang=en-US&region=US")


PERIODS = {
    "train": {"period1": 1761955200, "period2": 1765929600},
    "test": {"period1": 1765324800, "period2": 1765929600}
}


def fetch_and_save(symbol: str, save_dir: str, period_type: str):
    periods = PERIODS[period_type]
    url = build_url(symbol, periods["period1"], periods["period2"])
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.9',
        'Referer': 'https://finance.yahoo.com/'
    }
    
    max_retries = 3
    for attempt in range(max_retries):
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            break
        elif response.status_code == 429 and attempt < max_retries - 1:
            wait_time = (attempt + 1) * 10
            print(f"Rate limit aşıldı. {wait_time} saniye bekleniyor...")
            time.sleep(wait_time)
        else:
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.text}")
            raise RuntimeError(f"Veri çekilemedi → {symbol} için {save_dir} (Status: {response.status_code})")

    data = response.json()

    os.makedirs(save_dir, exist_ok=True)

    file_path = os.path.join(save_dir, f"{symbol}.json")
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

    print(f"Oluşturuldu: {file_path}")


if __name__ == "__main__":

    SYMBOL = "KO"

    fetch_and_save(
        symbol=SYMBOL,
        save_dir="train_data",
        period_type="train"
    )

    print("5 saniye bekleniyor...")
    time.sleep(5)

    fetch_and_save(
        symbol=SYMBOL,
        save_dir="test_data",
        period_type="test"
    )
