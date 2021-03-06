# lotsoftext

Download a high quantity of text by grabbing it off of Wikipedia.
The output is a ZIP file with JSON files for every article.

Process can be interupted with CTRL-C which will properly close the file.
If the target file already exists it is simply appended.

## Output schema

| Field      | Description                                         |
| ---------- | --------------------------------------------------- |
| `url`      | URL of article                                      |
| `title`    | Title of article                                    |
| `content`  | Pure text content of article (sanitized whitespace) |

## Usage

```
usage: lotsoftext [-h] [--output OUTPUT] [--limit LIMIT]

Download a high quantity of text by grabbing it off of Wikipedia

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        the target output file, defaults to ./lotsoftext.zip
  --limit LIMIT, -l LIMIT
                        a limit for the amount of articles to download, by
                        default no limit is set
```

## Single file output

As a utility script the `pack.py` script is included. It combines all articles downloaded previously and combines them into a single file. By default the separator is a single space, however this can be switched to a newline. The general usage is as follows:

```
usage: pack.py [-h] [--newline] [--input INPUT] [--output OUTPUT]
               [--unidecode]

optional arguments:
  -h, --help            show this help message and exit
  --newline, -n         use newline as separator between articles
  --input INPUT, -i INPUT
                        zip file containing downloaded articles
  --output OUTPUT, -o OUTPUT
                        file to dump content in
  --unidecode, -u       transform to ascii
```



## License

MIT.
