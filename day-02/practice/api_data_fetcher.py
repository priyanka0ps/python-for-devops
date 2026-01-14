import json
import requests

Api_key="d5hmf21r01ql0oaind4gd5hmf21r01ql0oaind50"

api_url="https://finnhub.io/"


def get_stock_market_data(symbol):
    
    query=f"api/v1/company-news?symbol={symbol}&from=2025-05-15&to=2025-06-20&token={Api_key}"
    print(api_url+query)
    response=requests.get(url=api_url+query)
    data=response.json()
    print(type(data))

    '''print(data[0])
    print(type(data[0]))'''

    processed_data=[]
    for article in data:
        
        record = {
                "symbol": symbol,
                "headline": article.get("headline"),
                "source": article.get("source"),
                "datetime": article.get("datetime"),
                "url": article.get("url"),
                "summary": article.get("summary")
            }

        print(f"[{record['source']}] [{record['headline']}]")

        processed_data.append(record)


    filename=f"{symbol}_news.json"
    with open(filename, "w") as file:
        json.dump(processed_data, file, indent=4)

    print(f"\n Data save to {filename}")   

    # print(response.json())


symbol=input("Enter the symbol you want see stocks news for eg. (IBM,AMZN,GOGL,AAPL): ")
get_stock_market_data(symbol)