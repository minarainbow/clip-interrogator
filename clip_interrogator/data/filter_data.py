lighting = ["light", "dark", "bright", "shadow", "glow"]
camera_shot = ["angle", "shot", "view"]
with open('flavors.txt') as source_file:
    with open('lighting.txt', 'a') as dest_file:
        for line in source_file:
            for word in lighting:
                if word in line and not "slight" in line :
                    dest_file.write(line)
    