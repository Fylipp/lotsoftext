import argparse
import json
import zipfile

from lotsoftext.fetch import get_random

parser = argparse.ArgumentParser(prog='lotsoftext',
                                 description="Download a high quantity of text by grabbing it off of Wikipedia")

parser.add_argument('--output', '-o', type=str, default='./lotsoftext.zip', help="the target output file")
parser.add_argument('--limit', '-l', type=int, default=10_000,
                    help="a limit for the amount of articles to download, 0 to wait for keyboard interrupt, default 10,000")

args = parser.parse_args()

output_target = args.output
limit = args.limit

print('lotsoftext')
print()

with zipfile.ZipFile(output_target, 'w', zipfile.ZIP_DEFLATED) as zip_file:
    try:
        # Odd numeric iteration to accommodate for failed attempts
        i = 0
        while True:
            if 0 < limit == i:
                break

            print(f'{i}: ', end='')

            try:
                article = get_random()
            except Exception as e:
                print(e)
                continue

            filename = f'{i}.json'
            if filename in zip_file.namelist():
                continue

            json_data = json.dumps(article, default=lambda o: o.__dict__)
            zip_file.writestr(filename, json_data)

            print(article.url)

            i += 1
    except KeyboardInterrupt:
        print('Interrupted by keyboard signal')
    print('Closing file ...')
