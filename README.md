<h1>

![muos](https://socialify.git.ci/sakkke/muos/image?issues=1&language=1&name=1&owner=1&pattern=Formal%20Invitation&stargazers=1&theme=Light)

</h1>

[![](https://img.shields.io/circleci/build/github/sakkke/muos?style=for-the-badge)](https://app.circleci.com/pipelines/github/sakkke/muos)

muOS

## Links

- [CHANGELOG.md](./CHANGELOG.md)
- [LICENSE](./LICENSE)
- [Website](https://muos.netlify.app/)

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
