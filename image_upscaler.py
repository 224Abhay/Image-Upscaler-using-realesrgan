import os
import subprocess
from datetime import datetime
from tqdm import tqdm
import shutil

class ImageUpscaler:
    def __init__(self, input_dir="inputs", base_output_dir="outputs"):
        self.input_dir = input_dir
        self.base_output_dir = base_output_dir

        # Create a timestamped output folder
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.output_dir = os.path.join(self.base_output_dir, timestamp)

        # Ensure required directories exist
        os.makedirs(self.input_dir, exist_ok=True)
        os.makedirs(self.output_dir, exist_ok=True)

    def check_input_folder(self):
        """Checks if the input folder contains any images."""
        images = [f for f in os.listdir(self.input_dir) if f.lower().endswith((".jpg", ".jpeg", ".webp", ".png"))]
        if not images:
            print("❌ No images found in 'inputs/' folder. Please add images and try again.")
            return False
        return True

    def clean_filenames(self):
        """Removes spaces and parentheses from filenames."""
        for image in os.listdir(self.input_dir):
            new_image = image.replace("(", "").replace(")", "").replace(" ", "")
            if new_image != image:
                try:
                    os.rename(os.path.join(self.input_dir, image), os.path.join(self.input_dir, new_image))
                except Exception as e:
                    print(f"Warning: Could not rename {image} to {new_image}: {e}")

    def detect_gpu(self):
        """Detects and prints which GPU is being used for Real-ESRGAN."""
        try:
            result = subprocess.run(["realesrgan-ncnn-vulkan.exe", "-v"], capture_output=True, text=True)
            lines = result.stdout.splitlines()
            for line in lines:
                if "NVIDIA" in line or "Intel" in line or "AMD" in line:
                    print(f"🔹 Using GPU: {line.strip()}")
                    break
        except FileNotFoundError:
            print("⚠️ Real-ESRGAN not found! Make sure it's installed and in the system PATH.")

    def upscale_images(self):
        """Runs Real-ESRGAN upscaling on images with a progress bar. Moves successful images to 'inputs/success'."""
        success_dir = os.path.join("success")
        os.makedirs(success_dir, exist_ok=True)
        images = [img for img in os.listdir(self.input_dir) if img.lower().endswith((".jpg", ".jpeg", ".webp", ".png"))]

        # Display GPU info before starting
        self.detect_gpu()

        # Progress bar
        for image in tqdm(images, desc="Upscaling images", unit="image"):
            input_path = os.path.join(self.input_dir, image)
            output_path = os.path.join(self.output_dir, image)
            if not os.path.exists(output_path):  # Avoid re-processing
                command = f'realesrgan-ncnn-vulkan.exe -i "{input_path}" -o "{output_path}"'
                result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                if result.returncode == 0:
                    # Move the successfully upscaled image to the success folder
                    try:
                        shutil.move(input_path, os.path.join(success_dir, image))
                    except Exception as e:
                        print(f"Warning: Could not move {image} to success folder: {e}")
                # If failed, leave the image in the input folder

    def run_pipeline(self):
        """Executes the full image processing pipeline."""
        if not self.check_input_folder():
            return  # Stop execution if no images are found

        print(f"📂 Output folder: {self.output_dir}")
        print("🧹 Cleaning filenames...")
        self.clean_filenames()
        
        print("🚀 Upscaling images...")
        self.upscale_images()

        print("✅ Processing complete! Upscaled images are saved in:", self.output_dir)
