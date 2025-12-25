import os

# مسیر فولدر روی دسکتاپ
folder_path = os.path.join(os.path.expanduser("~"), "desktop", "tayebeh1404")

# گرفتن لیست پوشه ها
projects = [f for f in os.listdir(
    folder_path)if os.path.isdir(os.path.join(folder_path, f))]
# چاپ تعداد پروژه ها
print("tedad project:", len(projects))
# چاپ اسم هر پروژه
print("name project:")
for project in projects:
    print("-", project)
