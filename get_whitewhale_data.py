import requests as rq
import pandas as pd

def get_monthly_apy(apr):
    """APY assuming compounding monthy"""
    return ((1+(apr/12))**(12))-1
    
def get_cost(price, set):
    """Get cost from current price and amount needed to get in the set"""
    return price*set

def get_monthly_income(p, apy):
    """calc month income from current price and the apy"""
    return (p*apy)/12


def fetch():
    #PRICES
    juno_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=juno-network&vs_currencies=usd").json()['juno-network']['usd']
    terra_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=terra-luna-2&vs_currencies=usd").json()['terra-luna-2']['usd']
    injective_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=injective-protocol&vs_currencies=usd").json()['injective-protocol']['usd']
    chihuahua_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=chihuahua-token&vs_currencies=usd").json()['chihuahua-token']['usd']

    #QUERY DELEGATOR SHARES
    juno_val_set = rq.get("https://validators.cosmos.directory/chains/juno").json()
    juno_val_set_df = pd.DataFrame(juno_val_set['validators'])
    juno_delegator_shares = float(juno_val_set_df[juno_val_set_df['moniker']=="White Whale"]['delegator_shares'])/(10**6)

    terra_val_set = rq.get("https://validators.cosmos.directory/chains/terra2").json()
    terra_val_set_df = pd.DataFrame(terra_val_set['validators'])
    terra_delegator_shares = float(terra_val_set_df[terra_val_set_df['moniker']=="White Whale"]['delegator_shares'])/(10**6)

    # injective_val_set = rq.get("https://validators.cosmos.directory/chains/injective").json()
    # injective_val_set_df = pd.DataFrame(injective_val_set['validators'])
    # injective_delegator_shares = float(injective_val_set_df[injective_val_set_df['moniker']=="White Whale"]['delegator_shares'])/(10**6)
    injective_delegator_shares = 1904

    chihuahua_val_set = rq.get("https://validators.cosmos.directory/chains/chihuahua").json()
    chihuahua_val_set_df = pd.DataFrame(chihuahua_val_set['validators'])
    chihuahua_delegator_shares = float(chihuahua_val_set_df[chihuahua_val_set_df['moniker']=="White Whale"]['delegator_shares'])/(10**6)

    juno_apr = 0.6217
    terra_apr = 0.1446
    injective_apr = 0.1354
    chihuahua_apr = 0.8429
    
    juno_staked = 11866
    terra_staked = 640
    injective_staked = 1904
    chihuahua_staked = 0

    data = {
        "juno":{"price":juno_price, "set":juno_delegator_shares, "apr":juno_apr, "staked":juno_staked},
        "terra":{"price":terra_price, "set":terra_delegator_shares, "apr":terra_apr, "staked":terra_staked},
        "injective":{"price":injective_price, "set":injective_delegator_shares, "apr":injective_apr, "staked":injective_staked},
        "chihuahua":{"price":chihuahua_price, "set":chihuahua_delegator_shares, "apr":chihuahua_apr, "staked":chihuahua_staked},
    }

    for i in data.keys():
        apy = get_monthly_apy(data[i]['apr'])
        p = get_cost(data[i]['price'], data[i]['set'])
        monthly_income = get_monthly_income(p,apy)

        data[i]['apy'] = apy
        data[i]['est_monthly_revenue'] = monthly_income
        if data[i] != "terra":
            data[i]['est_monthly_commission_income_to_validator'] = monthly_income*(0.05)
        else:
            data[i]['est_monthly_commission_income_to_validator'] = monthly_income*(0.1)
        data[i]['est_monthly_staking_income'] = ((data[i]["staked"]*data[i]["price"]*apy)/12)


    return data
