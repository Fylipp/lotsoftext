import argparse
import json
import zipfile

from unidecode import unidecode

parser = argparse.ArgumentParser()
parser.add_argument('--newline', '-n', action='store_true', help='use newline as separator between articles')
parser.add_argument('--input', '-i', default='lotsoftext.zip', help='zip file containing downloaded articles')
parser.add_argument('--output', '-o', default='lotsoftext.txt', help='file to dump content in')
parser.add_argument('--unidecode', '-u', action='store_true', help='transform to ascii')
args = parser.parse_args()

separator = '\n' if args.newline else ' '

first = True
with open(args.output, 'w') as output_file:
    with zipfile.ZipFile(args.input) as input_zip:
        for filename in input_zip.namelist():
            with input_zip.open(filename) as input_file:
                raw = input_file.read()

            try:
                dec = json.loads(raw)
                content = dec['content']

                if len(content) == 0:
                    continue

                if not isinstance(content, str):
                    raise Exception(f'\'content\' attribute of object in {filename} is not a string')

                if args.unidecode:
                    content = unidecode(content)

                if first:
                    first = False
                else:
                    output_file.write(separator)
                output_file.write(content)
            except Exception as e:
                print(f'{filename}: {e}')
                continue
