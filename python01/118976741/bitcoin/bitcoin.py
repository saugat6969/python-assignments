import sys
import requests
if len(sys.argv)==2:
    try:
        in_float=float(sys.argv[1])
    except:
        print("command line argument is not a number")
        sys.exit(1)
else:
    print("missing command line arg")
    sys.exit(1)

try:
    response=requests.get(" https://api.coindesk.com/v1/bpi/currentprice.json")
    r=response.json()
    rate=r['bpi']['USD']['rate_float']
    amount=rate*in_float
    print(f"${amount:,.4f}")


except requests.RequestException:
    sys.exit(1)


