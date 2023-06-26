import requests
import json


# def lambda_handler(event, context):
def main():
  headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8,ka;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Referer': 'https://cloud.eyedea.cz/api/anonymizer',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua':
    '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
  }

  params = (
    ('url',
     'https://cloud.eyedea.cz/api/assets/anonymizer_example06-97670e9ef4347a9df680c162004ea04b.jpg'
     ),
    ('rotate_pic', '0'),
    ('showDetections', 'false'),
    ('anonymizeFace', 'true'),
    ('anonymizeLP', 'true'),
    ('_', '1686352370777'),
  )

  # for record in event['Records']:
  #   data = json.loads(record['body'])
  #   if data.get('image'):
  #     params = (
  #       ('url', data.get('image')),
  #       ('rotate_pic', '0'),
  #       ('showDetections', 'false'),
  #       ('anonymizeFace', 'true'),
  #       ('anonymizeLP', 'true'),
  #       ('_', '1686352370777'),
  #     )

  response = requests.get(
    'https://cloud.eyedea.cz/api/v2/anonymize.json',
    headers=headers,
    params=params,
  )

  json_data = response.json()

  filename = 'data.json'  # Replace with your desired filename
  with open(filename, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)


main()

''' requests layer!
mkdir python
cd python
pip install requests -t .
cd ..
zip -r relayer.zip python
'''
