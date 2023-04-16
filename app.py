from PIL import Image
import numpy as np

def get_colors(image_path):
    # Load image and convert to numpy array
    img = Image.open(image_path)
    img_data = np.array(img)

    # Flatten the array
    img_data = img_data.reshape(-1, 3)

    # Use k-means clustering to extract colors
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=len(img_data))
    kmeans.fit(img_data)
    colors = kmeans.cluster_centers_.astype(int)

    # Convert colors to hexadecimal codes
    color_codes = ['#{:02x}{:02x}{:02x}'.format(r, g, b) for (r, g, b) in colors]

    return color_codes

colors = get_colors('example.jpg')
print(colors) # Output: ['#c1c1c1', '#3f3f3f', '#f5f5f5', '#8b8b8b', '#292929', ...]