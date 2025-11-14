import os

folder_path = r"C:\Users\USER\Desktop\gomycode\Gomycode_Projects_And_Assignments\Checkpoint 1_ Virtualization, Networking & Web Service Discovery\images"   # change to your folder path

# Allowed image extensions
extensions = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")

count = 1

for filename in os.listdir(folder_path):
    if filename.lower().endswith(extensions):
        old_path = os.path.join(folder_path, filename)

        # Keep original extension
        ext = os.path.splitext(filename)[1]
        new_name = f"file{count}{ext}"
        new_path = os.path.join(folder_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed: {filename} → {new_name}")

        count += 1

print("Completed renaming all images.")
