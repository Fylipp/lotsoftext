import argparse
import json
import zipfile

from lotsoftext.fetch import get_random

parser = argparse.ArgumentParser(prog='lotsoftext',
                                 description="Download a high quantity of text by grabbing it off of Wikipedia")

parser.add_argument('--output', '-o', type=str, default='./lotsoftext.zip',
                    help="the target output file, defaults to ./lotsoftext.zip")
parser.add_argument('--limit', '-l', type=int, default=0,
                    help="a limit for the amount of articles to download, by default no limit is set")

args = parser.parse_args()

output_target = args.output
limit = args.limit

print('lotsoftext - (c) Philipp Ploder')
print('Use CTRL-C to stop manually')
print()

with zipfile.ZipFile(output_target, 'a', zipfile.ZIP_DEFLATED) as zip_file:
    try:
        names = zip_file.namelist()

        # Odd numeric iteration to accommodate for failed attempts and initial offset
        i_off = len(names)
        i = 1
        while True:
            if 0 < limit == i + 1:
                break

            print(f'{i + i_off}: ', end='')

            try:
                article = get_random()
            except Exception as e:
                print(e)
                continue

            filename = f'{abs(hash(article.url))}.json'

            if filename in names:
                print('Article already present in archive')
                continue
            names.append(filename)

            json_data = json.dumps(article, default=lambda o: o.__dict__)
            zip_file.writestr(filename, json_data)

            print(article.url)

            i += 1
    except KeyboardInterrupt:
        print('Interrupted by keyboard signal')
    print('Closing file ...')
