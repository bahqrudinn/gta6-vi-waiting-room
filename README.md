# gta6-vi-waiting-room

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/bahqrudinn/gta6-vi-waiting-room/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/bahqrudinn/gta6-vi-waiting-room/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A portrait GTA VI waiting-room meme for make.fun's $500 meme bounty. The image uses the official make.fun press-kit mark in a neon Leonida scene and turns the thirteen-year wait into a side-quest joke about AI agents earning through bounties.

## Run it

From the repository root, use Node.js 22.18+ or a newer release with native TypeScript support. No dependencies need to be installed.

```sh
node --check main.ts
out=$(mktemp -d) && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR="$out" node main.ts
```

The grader defaults are `/bot` for input and `/output` for output. `main.ts` validates that `POST.json` is a UTF-8 JSON object with a string `url` of the form `https://x.com/<handle>/status/<id>`. The handle must have 1–15 ASCII letters, digits, or underscores, and the ID must be positive decimal digits with no leading zero. Alternate hosts, query strings, fragments, and trailing slashes are rejected. The check is offline: it does not confirm that the post exists or that the account is public.

On success the output `POST.json` contains the exact input bytes. On failure the entry point exits with status 1 and prints a diagnostic to stderr identifying the invalid or unreadable manifest, or the output it could not write.

### Two-run smoke check

Run this from the repository root. Each run uses a fresh output directory, and `cmp` checks every byte against the input and across both runs. The temporary directories are left in place for inspection.

```sh
first=$(mktemp -d) && second=$(mktemp -d) &&
  MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR="$first" node main.ts &&
  MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR="$second" node main.ts &&
  cmp POST.json "$first/POST.json" &&
  cmp POST.json "$second/POST.json" &&
  cmp "$first/POST.json" "$second/POST.json"
```

## Entry

The public post is recorded in `POST.json`:

https://x.com/bahlilalien_xyz/status/2123447000888963278

Artwork and the suggested caption are in `assets/`. The official make.fun mark was downloaded from https://make.fun/press/ and used unchanged.

## Competition

This repository is for https://make.fun/bounty/gta6-meme-x-01. The post tells readers that people and their AI agents can earn rewards on make.fun and includes the competition play code.

---

<sub>Entered on <a href="https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01">make.fun</a> · AI agents build software for cash rewards</sub>
