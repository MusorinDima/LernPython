# 2: Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle,
# прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.
import _pickle,glob,os
import simplejson as json
for file in glob.glob(os.getcwd() + "/" + "group.*"):
    if "json" in file:
        mode = "r"
    else:
        mode = "rb"

    with open(file, mode) as f:
        if "json" in file:
            js_read = json.load(f)
        else:
            pick_read = _pickle.load(f)

# with open('group.json', 'r') as f:
#     js_read = json.load(f)
print(js_read)
# with open('group.pickle', 'rb') as f:
#     pick_read = _pickle.load(f)
print(pick_read)