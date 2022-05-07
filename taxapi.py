import taxjar

client = taxjar.Client(api_key='bccb6325e7bc94c6da498afcf46b5564')

def taxrate(zipcode: str) -> float:
    rates = client.rates_for_location(zipcode)
    print(rates.combined_rate)
    return rates.combined_rate
