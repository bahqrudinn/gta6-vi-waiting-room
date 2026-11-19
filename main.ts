// Validate the public post reference locally, then hand the original manifest to the grader.

import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join } from 'node:path';

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
const source = join(BOT_DIR, 'POST.json');
const destination = join(OUTPUT_DIR, 'POST.json');
const statusUrl = /^https:\/\/x\.com\/[A-Za-z0-9_]{1,15}\/status\/[1-9][0-9]*$/;

/** @param {string} message @param {unknown} err */
function fail(message, err) {
  console.error(`${message}: ${err instanceof Error ? err.message : String(err)}`);
  process.exitCode = 1;
}

function main() {
  let bytes;
  try {
    bytes = readFileSync(source);
  } catch (err) {
    return fail(`Cannot read manifest ${source}`, err);
  }

  try {
    const manifest = JSON.parse(new TextDecoder('utf-8', { fatal: true, ignoreBOM: true }).decode(bytes));
    if (manifest === null || typeof manifest !== 'object' || Array.isArray(manifest)
        || !Object.hasOwn(manifest, 'url') || typeof manifest.url !== 'string'
        || !statusUrl.test(manifest.url)) {
      throw new Error('expected a JSON object with a canonical https://x.com/<handle>/status/<id> URL in "url"');
    }
  } catch (err) {
    return fail(`Invalid manifest ${source}`, err);
  }

  try {
    mkdirSync(OUTPUT_DIR, { recursive: true });
    writeFileSync(destination, bytes);
  } catch (err) {
    fail(`Cannot write output ${destination}`, err);
  }
}

main();
