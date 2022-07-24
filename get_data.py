
import requests as rq
import pandas as pd
import numpy as np
import time

def get_apy(apr):
    """APY assuming compounding daily"""
    return ((1+(apr/365))**(365))-1
    
def get_cost(price, set):
    """Get cost from current price and amount needed to get in the set"""
    return price*set

def get_monthly_income(p, apy):
    """calc month income from current price and the apy"""
    return (p*apy)/12

def fetch():
    juno_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=juno-network&vs_currencies=usd").json()['juno-network']['usd']
    osmo_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=osmosis&vs_currencies=usd").json()['osmosis']['usd']
    cosmos_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=cosmos&vs_currencies=usd").json()['cosmos']['usd']
    evmos_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=evmos&vs_currencies=usd").json()['evmos']['usd']
    akash_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=akash-network&vs_currencies=usd").json()['akash-network']['usd']
    stargaze_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=stargaze&vs_currencies=usd").json()['stargaze']['usd']
    umee_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=umee&vs_currencies=usd").json()['umee']['usd']
    secret_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=secret&vs_currencies=usd").json()['secret']['usd']
    terra_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=terra-luna-2&vs_currencies=usd").json()['terra-luna-2']['usd']
    injective_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=injective-protocol&vs_currencies=usd").json()['injective-protocol']['usd']
    sifchain_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=sifchain&vs_currencies=usd").json()['sifchain']['usd']
    kava_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=kava&vs_currencies=usd").json()['kava']['usd']
    comdex_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=comdex&vs_currencies=usd").json()['comdex']['usd']
    cryptoorgchain_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=crypto-com-chain&vs_currencies=usd").json()['crypto-com-chain']['usd']
    persistence_price = rq.get(f"https://api.coingecko.com/api/v3/simple/price?ids=persistence&vs_currencies=usd").json()['persistence']['usd']

    #minimum amount needed to get in active set https://www.mintscan.io/
    # assets = ['juno', 'osmosis', 'cosmoshub', 'evmos','akash', 'stargaze','umee', 'secretnetwork', 'terra']
    juno_val_set = rq.get("https://validators.cosmos.directory/chains/juno").json()
    juno_val_set_df = pd.DataFrame(juno_val_set['validators'])
    juno_actv_val_set_df = juno_val_set_df[juno_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    juno_set = float(juno_actv_val_set_df.tail(1)['delegator_shares'])/1000000

    osmosis_val_set = rq.get("https://validators.cosmos.directory/chains/osmosis").json()
    osmosis_val_set_df = pd.DataFrame(osmosis_val_set['validators'])
    osmosis_actv_val_set_df = osmosis_val_set_df[osmosis_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    osmosis_set = float(osmosis_actv_val_set_df.tail(1)['delegator_shares'])/1000000

    cosmoshub_val_set = rq.get("https://validators.cosmos.directory/chains/cosmoshub").json()
    cosmoshub_val_set_df = pd.DataFrame(cosmoshub_val_set['validators'])
    cosmoshub_actv_val_set_df = cosmoshub_val_set_df[cosmoshub_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    cosmoshub_set = float(cosmoshub_actv_val_set_df.tail(1)['delegator_shares'])/1000000

    evmos_val_set = rq.get("https://validators.cosmos.directory/chains/evmos").json()
    evmos_val_set_df = pd.DataFrame(evmos_val_set['validators'])
    evmos_actv_val_set_df = evmos_val_set_df[evmos_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    evmos_set = float(evmos_actv_val_set_df.tail(1)['delegator_shares'])/1000000000000000000

    akash_val_set = rq.get("https://validators.cosmos.directory/chains/akash").json()
    akash_val_set_df = pd.DataFrame(akash_val_set['validators'])
    akash_actv_val_set_df = akash_val_set_df[akash_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    akash_set = float(akash_actv_val_set_df.tail(1)['delegator_shares'])/1000000

    stargaze_val_set = rq.get("https://validators.cosmos.directory/chains/stargaze").json()
    stargaze_val_set_df = pd.DataFrame(stargaze_val_set['validators'])
    stargaze_actv_val_set_df = stargaze_val_set_df[stargaze_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    stargaze_set = float(stargaze_actv_val_set_df.tail(1)['delegator_shares'])/1000000

    umee_val_set = rq.get("https://validators.cosmos.directory/chains/umee").json()
    umee_val_set_df = pd.DataFrame(umee_val_set['validators'])
    umee_actv_val_set_df = umee_val_set_df[umee_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    umee_set = float(umee_actv_val_set_df.tail(1)['delegator_shares'])/1000000

    secretnetwork_val_set = rq.get("https://validators.cosmos.directory/chains/secretnetwork").json()
    secretnetwork_val_set_df = pd.DataFrame(secretnetwork_val_set['validators'])
    secretnetwork_actv_val_set_df = secretnetwork_val_set_df[secretnetwork_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    secretnetwork_set = float(secretnetwork_actv_val_set_df.tail(1)['delegator_shares'])/1000000

    sifchain_val_set = rq.get("https://validators.cosmos.directory/chains/sifchain").json()
    sifchain_val_set_df = pd.DataFrame(sifchain_val_set['validators'])
    sifchain_actv_val_set_df = sifchain_val_set_df[sifchain_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    sifchain_set = float(sifchain_actv_val_set_df.tail(1)['delegator_shares'])/1000000000000000000

    kava_val_set = rq.get("https://validators.cosmos.directory/chains/kava").json()
    kava_val_set_df = pd.DataFrame(kava_val_set['validators'])
    kava_actv_val_set_df = kava_val_set_df[kava_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    kava_set = float(kava_actv_val_set_df.tail(1)['delegator_shares'])/1000000

    comdex_val_set = rq.get("https://validators.cosmos.directory/chains/comdex").json()
    comdex_val_set_df = pd.DataFrame(comdex_val_set['validators'])
    comdex_actv_val_set_df = comdex_val_set_df[comdex_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    comdex_set = float(comdex_actv_val_set_df.tail(1)['delegator_shares'])/1000000

    cryptoorgchain_val_set = rq.get("https://validators.cosmos.directory/chains/cryptoorgchain").json()
    cryptoorgchain_val_set_df = pd.DataFrame(cryptoorgchain_val_set['validators'])
    cryptoorgchain_actv_val_set_df = cryptoorgchain_val_set_df[cryptoorgchain_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    cryptoorgchain_set = float(cryptoorgchain_actv_val_set_df.iloc[-1]['delegator_shares'])/100000000

    persistence_val_set = rq.get("https://validators.cosmos.directory/chains/persistence").json()
    persistence_val_set_df = pd.DataFrame(persistence_val_set['validators'])
    persistence_actv_val_set_df = persistence_val_set_df[persistence_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    persistence_set = float(persistence_actv_val_set_df.iloc[-1]['delegator_shares'])/1000000
    
    # terra_val_set = rq.get("https://validators.cosmos.directory/chains/terra").json()
    # terra_val_set_df = pd.DataFrame(terra_val_set['validators'])
    # terra_actv_val_set_df = terra_val_set_df[terra_val_set_df['status']=='BOND_STATUS_BONDED'].sort_values(by=['rank'], ascending=True)
    # terra_set = float(terra_actv_val_set_df.tail(1)['delegator_shares'])/1000000
    terra_set = 292900
    injective_set = 10009


    #staking aprs https://www.mintscan.io/
    juno_apr = .8009 
    osmo_apr = .3401
    evmos_apr = 6.2943 
    cosmos_apr = .1884
    akash_apr = .2157 
    stargaze_apr = .6038 
    umee_apr = .5157
    secret_apr = .2337
    terra_apr = .1431
    injective_apr = .1297
    sifchain_apr = 1.2937
    kava_apr = .2634
    comdex_apr = .4037
    cryptoorgchain_apr = .1453
    persistence_apr = .3393

    data = {
        "juno":{"price":juno_price, "set":juno_set, "apr":juno_apr},
        "osmo":{"price":osmo_price, "set":osmosis_set, "apr":osmo_apr},
        "evmos":{"price":evmos_price, "set":evmos_set, "apr":evmos_apr},
        "cosmos":{"price":cosmos_price, "set":cosmoshub_set, "apr":cosmos_apr},
        "akash":{"price":akash_price, "set":akash_set, "apr":akash_apr},
        "stargaze":{"price":stargaze_price, "set":stargaze_set, "apr":stargaze_apr},
        "umee":{"price":umee_price, "set":umee_set, "apr":umee_apr},
        "secret":{"price":secret_price, "set":secretnetwork_set, "apr":secret_apr},
        "terra":{"price":terra_price, "set":terra_set, "apr":terra_apr},
        "injective":{"price":injective_price, "set":injective_set, "apr":injective_apr},
        "sifchain":{"price":sifchain_price, "set":sifchain_set, "apr":sifchain_apr},
        "kava":{"price":kava_price, "set":kava_set, "apr":kava_apr},
        "comdex":{"price":comdex_price, "set":comdex_set, "apr":comdex_apr},
        "cryptoorgchain":{"price":cryptoorgchain_price, "set":cryptoorgchain_set, "apr":cryptoorgchain_apr},
        "persistence":{"price":persistence_price, "set":persistence_set, "apr":persistence_apr},
    }
    for i in data.keys():
        apy = get_apy(data[i]['apr'])
        p = get_cost(data[i]['price'], data[i]['set'])
        monthly_income = get_monthly_income(p,apy)

        data[i]['apy'] = apy
        data[i]['cost_to_enter_set'] = p
        data[i]['est_monthly_revenue'] = monthly_income
        data[i]['est_monthly_income_to_validator'] = monthly_income *.1
    return data



# v_data = pd.DataFrame(data)
# v_data.to_csv("data/validator_data")
    # print(f"""{i} 
    # price: ${round(data[i]['price'],2)}
    # apy: {round(apy*100,2)}%
    # cost to get in the set: ${round(p,2)}
    # monthly income: ${round(monthly_income,2)}""")

