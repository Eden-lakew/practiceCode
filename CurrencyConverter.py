import requests 

def get_exchange_rate(base_currency, target_currency):
    print("Changes the currency to the target currency.")

    url = f"https://v6.exchangerate-api.com/v6/3866213b2b49714eef580c0c/latest/{base_currency}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if target_currency in data["conversion_rates"]:
            return data["conversion_rates"][target_currency]
        else:
            print("Target currency not found.")
            return None
    else:
        print("Error fetching data. Please check your API key or connection.")
        return None

def main():
    print("Welcome to the Currency Converter!")
    
    base_currency = input("Enter the base currency (e.g., USD, EUR): ").upper()
    target_currency = input("Enter the target currency (e.g., INR, GBP): ").upper()
    
    amount = float(input(f"Enter the amount in {base_currency}: "))
    
    # get the exchange rate
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    
    if exchange_rate:
        converted_amount = amount * exchange_rate
        print(f"\n{amount:.2f} {base_currency} is equal to {converted_amount:.2f} {target_currency}.")
    else:
        print("Conversion failed. Please try again.")
    
if __name__ == "__main__":
    main()