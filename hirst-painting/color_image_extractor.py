import colorgram

# Extract 6 colors from an image.
colors = colorgram.extract('art.jpg', 35)
colors_list=[(color.rgb.r,color.rgb.g,color.rgb.b) for color in colors]
print(colors_list)
