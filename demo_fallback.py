from PIL import Image

# Create a synthetic image (solid color) to demonstrate the local fallback caption generator
img = Image.new('RGB', (160, 206), color=(90, 120, 160))

# Fallback generator copied from app.py
def generate_local_caption(pil_img: Image.Image) -> str:
    try:
        w, h = pil_img.size
        aspect = "portrait" if h > w else "landscape"
        thumb = pil_img.convert("RGB").resize((1, 1))
        r, g, b = thumb.getpixel((0, 0))
        if r > 200 and g > 200 and b > 200:
            color = "light"
        elif r > 160 and g > 160 and b > 160:
            color = "pale"
        elif r > 100:
            color = "warm-toned"
        else:
            color = "dark"
        size_desc = "small" if max(w, h) < 300 else "photo"
        caption = f"A {color} {aspect} {size_desc}, head-and-shoulders portrait-style image of a person."
        return caption
    except Exception:
        return "A photo of a person."

print("Demo fallback caption:\n", generate_local_caption(img))
