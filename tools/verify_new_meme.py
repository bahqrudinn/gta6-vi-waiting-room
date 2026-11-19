from hashlib import sha256
from pathlib import Path
from subprocess import run
from sys import executable
from PIL import Image

root = Path(__file__).resolve().parent.parent
assets = root / 'assets'
before = {}
for name, size in [('new-meme.png', 1200), ('new-meme-preview.png', 480)]:
    with Image.open(assets / name) as image:
        assert image.format == 'PNG' and image.size == (size, size)
        image.verify()
    print(f'{name}: valid {size} x {size} PNG')
    before[name] = sha256((assets / name).read_bytes()).hexdigest()
caption = (assets / 'new-caption.txt').read_text()
assert all(text in caption for text in ('@makefunai', 'makefun-bison-blender-puddle', 'People and AI agents can both earn by completing bounties on make.fun'))
assert 'GTA VI: CO-OP MODE' in (assets / 'new-alt.txt').read_text()
print('Caption requirements and alt-text heading verified')
run([executable, str(root / 'tools/new_meme.py')], check=True)
for name, expected in before.items():
    actual = sha256((assets / name).read_bytes()).hexdigest()
    assert actual == expected, f'{name}: SHA-256 changed ({expected} -> {actual})'
    print(f'{name}: matching SHA-256 {actual}')
print('Rerender passed text/illustration spacing checks')
