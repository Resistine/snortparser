# snortparser

> This is a fork of snortparser by g-rd. The original repo can be found at https://github.com/g-rd/snortparser.
> There was another one already but it didn't fixed all the errors: https://github.com/crashingstatic/snortparser 
> There are also others: Python's https://github.com/jtschichold/snortparser/ (https://pypi.org/project/snortparser/) and https://github.com/novasec-x/SnortParser (SRParser)

Snort rule parser written in python. The main goal for this library is to validate snort rules and have them parsed into a workable dictionary object. A interactive python notebook can be found [here](example.ipynb).

The parser class accepts a snort rule as input and returns a dictionary that contains the parsed output.

```python
from snortparser import Parser

# define a snort rule
rule = ('alert tcp $HOME_NET any -> !$EXTERNAL_NET any (msg:\"MALWARE-BACKDOOR - Dagger_1.4.0\"; flow:to_client,established; content:\"2|00 00 00 06 00 00 00|Drives|24 00|\"; depth:16; metadata:ruleset community; classtype:misc-activity; sid:105; rev:14;)')

# parse the rule
parsed = Parser(rule)

# print the parsed rule
print(parsed.header)
print(parsed.options)
```

**NOTE**: If the parser is unable to parse the rule, it will return a `ValueError` with the invalid rule item. Additionally, it does not care about misplaced spaces in the headers ip and port definitions like: " alert tcp ![ 127.0.0.1, !8.8.8.8 ] any --> ". This is by design, since I am not sure if snort cares about header syntax that much.

## Recent Updates
- Added support for `alert ssl` headers (header size 2).
- Added default values for missing header fields (`source`, `src_port`, `arrow`, `destination`, `dst_port`).
- Added support for `ber_data` and `ber_skip` options.
- Added test script to verify the parser.
