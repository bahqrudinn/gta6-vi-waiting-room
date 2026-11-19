from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def main():
    root = Path(__file__).absolute().parent.parent
    assets = root / 'assets'
    image = Image.new('RGB', (1200, 1200))
    draw = ImageDraw.Draw(image)
    ink, cream, mint = '#18132d', '#fff5e2', '#aaffd2'
    for y in range(1200):
        t = y / 1199
        draw.line((0, y, 1199, y), fill=(int(48 + 41*t), int(25 + 16*t), int(79 + 37*t)))

    illustration_regions = ((812, 441, 1091, 585), (825, 757, 1078, 971))

    def text(x, y, value, size, fill=cream, bold=True):
        path = '/system/fonts/DroidSans-Bold.ttf' if bold else '/system/fonts/RobotoStatic-Regular.ttf'
        font = ImageFont.truetype(path, size)
        box = draw.textbbox((x, y), value, font=font, anchor='lt')
        assert 0 <= box[0] <= box[2] <= 1200 and 0 <= box[1] <= box[3] <= 1200, value
        for left, top, right, bottom in illustration_regions:
            assert box[2] <= left - 24 or box[0] >= right + 24 or box[3] <= top or box[1] >= bottom, (value, box)
        draw.text((x, y), value, font=font, fill=fill, anchor='lt')

    draw.rounded_rectangle((58, 48, 1142, 181), radius=28, fill=mint)
    text(87, 72, 'make.fun', 91, ink)
    text(637, 97, 'BOUNTY BOARD', 45, ink)
    text(61, 222, 'GTA VI: CO-OP MODE', 85)
    for top in (344, 705):
        draw.rounded_rectangle((58, top, 1142, top + 331), radius=33, fill=ink, outline='#c38ff0', width=4)
    # A controller for the player, a mint robot for the AI agent.
    draw.rounded_rectangle((812, 441, 1090, 584), radius=57, fill='#ffab82')
    draw.rounded_rectangle((851, 478, 877, 549), radius=5, fill=ink)
    draw.rounded_rectangle((829, 500, 899, 526), radius=5, fill=ink)
    for x, y in ((1017, 481), (1046, 510), (1017, 539), (988, 510)):
        draw.ellipse((x-10, y-10, x+10, y+10), fill=ink)
    draw.line((951, 830, 951, 785), fill=mint, width=13)
    draw.ellipse((935, 757, 967, 789), fill='#ffab82')
    draw.rounded_rectangle((825, 818, 1077, 970), radius=37, fill=mint)
    for x in (889, 1013):
        draw.ellipse((x-17, 853, x+17, 887), fill=ink)
    draw.arc((914, 880, 988, 940), 0, 180, fill=ink, width=9)
    text(91, 377, 'ME', 49, '#ffab82')
    text(91, 452, 'Saving up for', 69)
    text(91, 538, 'GTA VI.', 88)
    text(91, 738, 'MY AI AGENT', 49, mint)
    text(91, 811, 'I earned the bounty.', 66)
    text(91, 906, 'Get your own copy.', 66)
    text(62, 1090, 'People + AI agents can earn on make.fun', 53, mint, bold=False)
    assets.mkdir(exist_ok=True)
    for name, size in (('new-meme.png', 1200), ('new-meme-preview.png', 480)):
        output = image if size == 1200 else image.resize((size, size), Image.Resampling.LANCZOS)
        with (assets / name).open('wb') as stream:
            output.save(stream, format='PNG')


if __name__ == '__main__':
    main()
