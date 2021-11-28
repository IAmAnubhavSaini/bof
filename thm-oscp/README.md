# TryHackMe buffer overflow oscp application

## Generating bad chars

```python
python3 -c 'print("".join(["\\x" + "{:02x}".format(x) for x in range(1, 256)]))'
```

```shell
for i in {0..255}; do printf "\\\x%02x" $i; done
```

### Removing unwanted bad chars

```
| sed 's/\\x01//; s/\\x02//; s/\\x03//'
```

```
for·i·in·{0..255};·do·printf·"\\\x%02x"·$i;·done | sed 's/\\x00//; s/\\x0a//; s/\\x0d//; s/\\xff//'
```
|        |                 |
|--------|-----------------|
| `\x00` | NULL            |
| `\x0a` | New Line        |
| `\x0d` | Carriage Return |
| `\xff` | Form Feed       |

