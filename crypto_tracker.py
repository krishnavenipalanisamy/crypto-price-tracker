from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

# Start Chrome
driver = webdriver.Chrome()

# Open CoinMarketCap
driver.get("https://coinmarketcap.com/")

# Wait for page load
time.sleep(15)

# Get all rows
rows = driver.find_elements(By.XPATH, "//tbody/tr")

print("\nTop 10 Cryptocurrencies\n")

crypto_data = []

for i in range(10):
    try:
        data = rows[i].text.split("\n")

        rank = data[0]
        name = data[1]
        symbol = data[2]
        price = data[4]

        change_1h = data[5] if len(data) > 5 else "N/A"
        change_24h = data[6] if len(data) > 6 else "N/A"
        change_7d = data[7] if len(data) > 7 else "N/A"

        market_cap = data[8] if len(data) > 8 else "N/A"
        volume_24h = data[9] if len(data) > 9 else "N/A"

        print(
            f"{rank}. {name:<15} "
            f"Price: {price}"
        )

        crypto_data.append([
            rank,
            name,
            symbol,
            price,
            change_1h,
            change_24h,
            change_7d,
            market_cap,
            volume_24h
        ])

    except Exception as e:
        print(f"Error processing row {i+1}: {e}")

# Save CSV
with open(
    "top10_crypto_prices.csv",
    mode="w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.writer(file)

    writer.writerow([
        "Rank",
        "Coin Name",
        "Symbol",
        "Price",
        "1H Change",
        "24H Change",
        "7D Change",
        "Market Cap",
        "24H Volume"
    ])

    writer.writerows(crypto_data)

print("\nCSV file created successfully!")
print("File Name: top10_crypto_prices.csv")

driver.quit()