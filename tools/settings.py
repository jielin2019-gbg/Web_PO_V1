import os

rootdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

pageshots_dir = os.path.join(rootdir,"outputs","page_shots")

logs_dir = os.path.join(rootdir,"outputs","logs")

allure_dir = os.path.join(rootdir,"outputs","report_files")

#=============================  admin_info  ============================

admin_info = ("student","123456a","lemon")