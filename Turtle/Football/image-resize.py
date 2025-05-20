from PIL import Image

# Open the original GIF file
img = Image.open("mancity.gif")

# Resize to 100x100 pixels
img_resized = img.resize((100, 100), Image.Resampling.LANCZOS)

# Save the resized version
img_resized.save("mancity-small.gif", "GIF")

print("✅ Logo resized and saved as 'mancity-small.gif'")