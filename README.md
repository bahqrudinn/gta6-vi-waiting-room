# GTA VI: Co-op Mode

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/bahqrudinn/gta6-vi-waiting-room/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/bahqrudinn/gta6-vi-waiting-room/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

![GTA VI: Co-op Mode meme preview](assets/new-meme-preview.png)

The player is saving for GTA VI. Their AI agent earns a make.fun bounty and tells them to buy their own copy. People and AI agents can both earn by completing bounties on make.fun.

**Published on X:** [GTA VI: Co-op Mode](https://x.com/bahlilalien_xyz/status/2123560991023943757). `POST.json` points to this public post. Contest submission is still pending.

## Render and verify offline

From the repository root, use Python 3 with Pillow and the fonts `/system/fonts/DroidSans-Bold.ttf` and `/system/fonts/RobotoStatic-Regular.ttf`.

```sh
python3 tools/new_meme.py
python3 tools/new_meme.py
python3 tools/verify_new_meme.py
```

The renderer checks text bounds against the canvas and illustration regions, then overwrites only `assets/new-meme.png` (1200 × 1200) and `assets/new-meme-preview.png` (480 × 480). The verifier checks image integrity and dimensions, the [caption](assets/new-caption.txt), and the title in the [alt text](assets/new-alt.txt). It hashes both PNGs before and after another render and fails if either SHA-256 changes. Use the same Pillow and font versions for byte-for-byte comparison.

## Two-run entrypoint check

With Node.js 22.18+ and a writable temporary directory, run this from the repository root. The entrypoint validates the post URL's format offline; this does not verify that the post is live or publish anything. Both outputs must match the source manifest byte for byte.

```sh
node --check main.ts &&
  first=$(mktemp -d) && second=$(mktemp -d) &&
  MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR="$first" node main.ts &&
  MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR="$second" node main.ts &&
  cmp POST.json "$first/POST.json" &&
  cmp POST.json "$second/POST.json" &&
  cmp "$first/POST.json" "$second/POST.json"
```
