import requests

def get_hero_data(hero_name):
    url = f"https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    response = requests.get(url)
    if response.status_code == 200:
        all_heroes = response.json()
        for hero in all_heroes:
            if hero['name'].lower() == hero_name.lower():
                return hero
    else:
        print(f"Error: {response.status_code}")
        return None

def find_smartest_hero(hero_list):
    smartest_hero = None
    max_intelligence = -1

    for hero_name in hero_list:
        hero_data = get_hero_data(hero_name)
        if hero_data is not None:
            intelligence = int(hero_data['powerstats']['intelligence'])
            if intelligence > max_intelligence:
                max_intelligence = intelligence
                smartest_hero = hero_data['name']
    return smartest_hero

if __name__ == "__main__":
    hero_list = ["Hulk", "Captain America", "Thanos"]
    smartest_hero = find_smartest_hero(hero_list)
    print(f"Самый умный супергерой из списка: {smartest_hero}")
