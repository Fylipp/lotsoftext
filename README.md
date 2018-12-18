# lotsoftext

Download a high quantity of text by grabbing it off of Wikipedia.

The output is a ZIP file with JSON files for every article.

## Output schema

| Field   | Description                  |
| ------- | ---------------------------- |
| `url`   | URL of article               |
| `title` | Title of article             |
| `text`  | Pure text content of article |

## Usage

```
usage: lotsoftext [-h] [--output OUTPUT] [--limit LIMIT]

Download a high quantity of text by grabbing it off of Wikipedia

optional arguments:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        the target output file
  --limit LIMIT, -l LIMIT
                        a limit for the amount of articles to download, 0 to
                        wait for keyboard interrupt, default 10,000
```

## License

MIT.
