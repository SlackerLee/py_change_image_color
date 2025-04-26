from PIL import Image

# Open the image file
image = Image.open("icons8-garden-gloves-96.png")
image = image.convert("RGBA")

# Load pixel data
data = image.getdata()

# Define the threshold for dark colors
threshold = 100  # Adjust this value as needed

# Modify the pixel data
new_data = []
for item in data:
    # Change dark colors to white
    if item[0] < threshold and item[1] < threshold and item[2] < threshold:
        new_data.append((255, 255, 255, item[3]))  # White color with original alpha
    else:
        new_data.append(item)

# Update image data and save the result
image.putdata(new_data)
image.save("output_icons8-garden-gloves-96.png")
