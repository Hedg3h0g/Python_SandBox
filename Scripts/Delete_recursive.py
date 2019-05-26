import os
from datetime import datetime, timedelta

for root, dirs, files in os.walk(r'C:\py\dir_for_remove', topdown=False):
    for file in files:
        curpath = os.path.join(root, file)
        file_modified = datetime.fromtimestamp(os.path.getmtime(curpath))
        if datetime.now() - file_modified > timedelta(minutes=5):
            os.remove(curpath)

    # Проходим по директориями и удаляем пустые
    for d in dirs:
        curpath = os.path.join(root, d)
        if not os.listdir(curpath):
            os.rmdir(curpath)