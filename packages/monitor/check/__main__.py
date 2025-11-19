import os
import requests

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID =  os.getenv("CHAT_ID")

def startup():
    if not BOT_TOKEN or not CHAT_ID:
        raise ValueError("BOT_TOKEN and CHAT_ID environment variables must be set.")

def notify(msg: str):
    startup()

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={"chat_id": CHAT_ID, "text": msg}, timeout=10)
    except Exception as e:
        print("Failed to send Telegram message:", e)

def main(args):
    ##Test notify
    if args and args.get("test_notify") == "true":
        notify("Test message from ShareToBuy monitor.")
        return {"ok" : True, "mode": "Test"}


    url='https://www.sharetobuy.com/properties-count/?location=Hackney%20-%20Hackney&locationId=106452&lat=51.55492&lon=-0.060450000000000004&developmentId=&hasPolygon=1&userSearchId=&hereLocation=&hereLocation=%23%23%23hereLocation%23%23%23&locationId=106452&lat=51.55492&lon=-0.060450000000000004&developmentId=&hasPolygon=1&userSearchId=&radius=40&minBedrooms=&maxBedrooms=&schemeType%5B%5D=14&minMonthlyCost=&maxMonthlyCost=&minDeposit=&maxDeposit=&radius=40&rentOrBuy=2&createdAtPeriod=&minMinShareAvailable=&maxMinShareAvailable=&minFullMarketPrice=&maxFullMarketPrice=&viewType=1&campaignId=&developerId=&_token=f43dXRIWHwknKKWt1tLLanlXJPdnczEWdZDOhBYb&showAllPopular=showAllPopular&propertyTypeGroup=undefined&showAllOther=1&_token=f43dXRIWHwknKKWt1tLLanlXJPdnczEWdZDOhBYb&action=%2Fproperties-count%2F&_=1763550069528'
    response = None
    count_of_properties_available = 0
    try:
        print("Calling URL...")
        response = requests.get(url,timeout=10)
        #raises an HTTPError if the HTTP request returned an unsuccessful status code
        response.raise_for_status()
        data = response.json()
        count_of_properties_available = int(data['data']['count'])
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    print (f'Status code: {response.status_code}')
    print (f'Response: {response.text}')
    print (f'Number of properties available: {count_of_properties_available}')


    if count_of_properties_available > 0:
        print("Properties available!")
        notify(f"Properties available: {count_of_properties_available}")

    return {"ok" : True, "count_of_properties_available": count_of_properties_available}


if __name__ == "__main__":
    main(None)