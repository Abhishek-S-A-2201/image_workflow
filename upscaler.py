from super_image import DrlnModel, ImageLoader
from PIL import Image
import os
import glob


class Upscaler:

    def __init__(self, image_dir, save_dir) -> None:
        self.model = self.load_model()
        self.image_dir = os.path.join(image_dir, "")
        self.save_dir = save_dir

    def load_model(self):
        model = DrlnModel.from_pretrained('eugenesiow/drln-bam', scale=3)
        return model

    def save_image(self, preds, image_path):
        head_tail = os.path.split(image_path)
        image_name = head_tail[1].split(".")[0]
        save_path = os.path.join(self.save_dir, f"{image_name}.png")
        ImageLoader.save_image(preds, save_path)

    def upscale_image(self, image_path):
        image = Image.open(image_path)
        inputs = ImageLoader.load_image(image)
        preds = self.model(inputs)
        self.save_image(preds, image_path)

    def upscale_bulk_images(self):
        head_tail = os.path.split(self.image_dir)
        for image_path in glob.glob(os.path.join(head_tail[0], "*g")):
            self.upscale_image(image_path)
