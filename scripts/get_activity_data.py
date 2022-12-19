import argparse
import requests as re
import ujson

from datetime import datetime

parser = argparse.ArgumentParser(description='get activity data')
parser.add_argument('--token', help='access token for the request')

if __name__=="__main__":
    args = parser.parse_args()
    token = args.token

    headers = {
    'accept': "application/json",
    'authorization': f"Bearer {token}",
    'content-type': "application/json",
    }
    url = "https://www.strava.com/api/v3/athlete/activities"

    results = re.get(url=url, headers=headers)

    if results.status_code == 200:

        current_time = datetime.today().strftime('%Y%m%d%H%M')
        with open(f'data/activities_{current_time}.json', 'w') as jsonfile:
            ujson.dump(results.json(), jsonfile)