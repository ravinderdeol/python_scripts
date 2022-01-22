from pycoingecko import CoinGeckoAPI

# access the top seven trending cryptos in the past twenty-four hours
trending = CoinGeckoAPI().get_search_trending()

# save the id of each trending crypto to a variable
trending_one_id = trending["coins"][0]["item"]["id"]
trending_two_id = trending["coins"][1]["item"]["id"]
trending_three_id = trending["coins"][2]["item"]["id"]
trending_four_id = trending["coins"][3]["item"]["id"]
trending_five_id = trending["coins"][4]["item"]["id"]
trending_six_id = trending["coins"][5]["item"]["id"]
trending_seven_id = trending["coins"][6]["item"]["id"]

# save the name of each trending crypto to a variable
trending_one_name = trending["coins"][0]["item"]["name"]
trending_two_name = trending["coins"][1]["item"]["name"]
trending_three_name = trending["coins"][2]["item"]["name"]
trending_four_name = trending["coins"][3]["item"]["name"]
trending_five_name = trending["coins"][4]["item"]["name"]
trending_six_name = trending["coins"][5]["item"]["name"]
trending_seven_name = trending["coins"][6]["item"]["name"]

# print the name of each trending crypto
print(f"1. {trending_one_name}")
print(f"2. {trending_two_name}")
print(f"3. {trending_three_name}")
print(f"4. {trending_four_name}")
print(f"5. {trending_five_name}")
print(f"6. {trending_six_name}")
print(f"7. {trending_seven_name}")
