lighting = ["light", "dark", "bright", "shadow"]
camera_shot = ["angle", "shot", "view"]
with open('flavors.txt') as source_file:
    with open('camera_shot.txt', 'a') as dest_file:
        for line in source_file:
            for word in camera_shot:
                if word in line:
                    dest_file.write(line)
    