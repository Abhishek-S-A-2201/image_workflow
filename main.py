from upscaler import *
import os

image_dir = input("Please provide image directory: ")
image_dir = os.path.join(image_dir, "")
head_tail = os.path.split(image_dir)

upsacled_dir = f"{head_tail[0]}_upscaled"
os.makedirs(upsacled_dir, exist_ok=True)

upsacler = Upscaler(image_dir, upsacled_dir)
upsacler.upscale_bulk_images()