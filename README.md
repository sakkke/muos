# muOS
muOS

## Dev

1. In target:

```bash
dest="$(ip route get 1.2.3.4 | head --lines=1 | awk '{print $7}')"
echo "dest=$dest"
nc -lvp 6867 | install /dev/stdin /usr/local/bin/serve
```

2. In host:

```bash
nc -vw 2 '<dest>' 6867 < ./scripts/serve
```

3. In target:

```bash
serve
```

4. In host:

```bash
./scripts/transfer '<dest>'
```
