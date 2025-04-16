from io import BytesIO

from cairosvg import svg2png
from PIL import Image

from utils.constants import DEFAULT_SVG


def svg2pil(svg: str):
    try:
        res = Image.open(BytesIO(svg2png(svg)))
    except Exception:
        res = Image.open(BytesIO(svg2png(DEFAULT_SVG)))
    return res
