import json
import requests
import pprint
import pandas as pd
import csv

def main():
    # adjustable params
    FROM_ID = 110000
    FETCH_CNT = 10 ** 3
    TO_ID = FROM_ID + FETCH_CNT
    THRES = 30
    handles = set()
    data_points = []
    for i in range(FROM_ID, TO_ID):
        print('Fetching blog id ' + str(i) + '...')
        try:
            response = requests.get('https://codeforces.com/api/blogEntry.comments?blogEntryId=' + str(i))
            data = response.json()
            if data['status'] == 'OK':
                for comment in data['result']:
                    if abs(comment['rating']) >= THRES:
                        comment_extracted = dict({'rating': comment['rating'], 'commentatorHandle': comment['commentatorHandle'], 'text': comment['text']})
                        data_points.append(comment_extracted)
                        handles.add(comment['commentatorHandle'])
            print('Fetching blog id ' + str(i) + ' successfully attempted.')
        except:
            print('An accident is faced while fetching blog id ' + str(i) + '.')

    user_response = requests.get('https://codeforces.com/api/user.info?handles=' + ';'.join(handles))
    user_data = user_response.json()
    assert user_data['status'] == 'OK'
    with open('user_data_3.json', 'w') as f:
        json.dump(user_data, f)
    with open('comments_3.json', 'w') as f:
        json.dump(data_points, f)

if __name__ == '__main__':
    main()
