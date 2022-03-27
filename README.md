# Rewrite bytes in files
**status:**

- version 1 - alpha version, one-time replacement algorithm

- version 2 - development version, new replacement algorithm

**Usage**:

`python3 main.py -c config.json -f file`

or

`python3 main.py --config config.json --file file`

`config.json` - Json file. Contains bytes that need to be replaced.

`file` - The file in which the bytes need to be overwritten.

Example of content in the config (for `version 2`):
```
{
	"hex_old": ["aa aa aa"],
	"hex_new": ["ff ff ff"]
}
```

or

```
{
	"hex_old": ["AA AA AA"],
	"hex_new": ["FF FF FF"]
}
```





Version 2 can record multiple groups in the text.

Example:
```
{
	"hex_old": ["AA AA AA", "00 00 00"],
	"hex_new": ["FF FF FF", "11 11 11"]
}
```

`AA AA AA` will change to `FF FF FF` and `00 00 00` will change to `11 11 11`.

But keep in mind: `The number of groups should not be different`:

```
{
	"hex_old": ["AA AA AA", "00 00 00", "99 A5 F1"],
	"hex_new": ["FF FF FF", "11 11 11"]
}
```

Bytes `99 A5 F1` will be ignored





**NOTE**:

For `version 1`, there should be a STRING in the config, not an array:
```
{
	"hex_old": "AA AA AA",
	"hex_new": "FF FF FF"
}
```


**NOTE 2**:
Version 1 overwrites a group of bytes only once!
Example:
replace `AA` with `FF` in the text:
```AA 00 AA 00 AA```
When version 1 starts, the text will change to `FF 00 AA 00 AA`.
Version 2 replaces all byte groups! And from `AA 00 AA 00 AA` will change to `FF 00 FF 00 FF`.

**NOTE 3**:
when replacing bytes (for example, if we replace `AA` with `FF` in the file, then when replacing it back (`AA` to `FF`), extra bytes (which were in the file before the replacement) may be replaced
Example:
replaced `AA` with `FF` in the text ```AA AA AA FF``` and the text will change to ```FF FF FF FF```. If we try to change bytes from `FF` to `AA` after replacement, we will change the text to ```AA AA AA AA``` (which was not in the original file and the file may stop not working) 
Make copies before replacing bytes!
