import datetime
import json
import os

from interfase.Edit_window import Edit_Box


def initJson():
    with open("resources/affairs.json","r", encoding='utf-8') as fp:
        if os.stat("resources/affairs.json").st_size != 0:
            sort_json_prior()
            affairs_json = fp.read()
            affairs = json.loads(affairs_json)
        else:
            affairs_json = {
                          "affairs": [
                            {
                              "name": "Накормить кота",
                              "text": "Вчера кот мало ел, поэтому нужно не забыть его покормить!",
                              "data": "21.09.2002",
                              "priority": 3
                            }
                          ]
                        }
            affairs = json.dumps(affairs_json)
            affairs = json.loads(affairs)
        return affairs

def new_affairs_json(affairs, name, text, data, priority):
    item = json.dumps(
        {
            "name": name,
            "text": text,
            "data": data,
            "priority": priority,
            "meta": [
                {
                    "add_data": datetime.datetime.now().strftime("%d.%m.%Y"),
                    "add_time": datetime.datetime.now().strftime("%H:%M"),
                    "del_data": ""
                 }
            ]
        })
    item = json.loads(str(item))
    affairs["affairs"].append(item)
    affairs = json.dumps(affairs)
    affairs = json.loads(str(affairs))
    with open("resources/affairs.json","w", encoding='utf-8') as fp:
        json.dump(affairs, fp, ensure_ascii=False, indent=2)
    return affairs

def del_affairs_json(n):
    with open("resources/affairs.json", "r", encoding='utf-8') as fp:
        affairs_json = fp.read()
        affairs = json.loads(affairs_json)
    load_affairs_in_story(affairs["affairs"][n])
    affairs["affairs"].pop(n)
    affairs = json.dumps(affairs)
    affairs = json.loads(str(affairs))
    with open("resources/affairs.json","w", encoding='utf-8') as fp:
        json.dump(affairs, fp, ensure_ascii=False, indent=2)

def sort_json_prior():
    with open("resources/affairs.json","r", encoding='utf-8') as fp:
        affairs = json.load(fp)
        affairs["affairs"].sort(key = lambda x: (-x['priority']))
    with open("resources/affairs.json", "w", encoding='utf-8') as fp:
        json.dump(affairs, fp, ensure_ascii=False, indent=2)
        return affairs

def sort_json_data():
    with open("resources/affairs.json","r", encoding='utf-8') as fp:
        affairs = json.load(fp)
        affairs["affairs"].sort(key=lambda x: datetime.strptime(x['data'], '%d.%m.%Y'))
    with open("resources/affairs.json", "w", encoding='utf-8') as fp:
        json.dump(affairs, fp, ensure_ascii=False, indent=2)
        return affairs

def sort_json_name():
    with open("resources/affairs.json","r", encoding='utf-8') as fp:
        affairs = json.load(fp)
        affairs["affairs"].sort(key=lambda x: x['name'])
    with open("resources/affairs.json", "w", encoding='utf-8') as fp:
        json.dump(affairs, fp, ensure_ascii=False, indent=2)
        return affairs

def update_json():
    with open("resources/affairs.json","r", encoding='utf-8') as fp:
        affairs_json = fp.read()
        affairs = json.loads(affairs_json)
    return affairs

def load_affairs_in_story(affair):
    with open("resources/affairs_story.json", "r", encoding='utf-8') as fp:
        affair_story = json.load(fp)
    affair_story["affairs"].append(affair)
    with open("resources/affairs_story.json", "w", encoding='utf-8') as fp:
        json.dump(affair_story, fp, ensure_ascii=False, indent=2)


def init_story_json():
    with open("resources/affairs_story.json", "r", encoding='utf-8') as fp:
        affair_story = json.load(fp)
    return affair_story


def update_story_json():
    with open("resources/affairs_story.json", "r", encoding='utf-8') as fp:
        affairs_json = fp.read()
        affairs = json.loads(affairs_json)
    return affairs

def del_story_json():
    with open("resources/affairs_story.json", "w", encoding='utf-8') as fp:
        affair = {
            "affairs": []
        }
        json.dump(affair, fp, ensure_ascii=False, indent=2)

def settings_button_clicked(self):
    edit = Edit_Box(self)

    edit.button_apply.clicked.connect(lambda: self.button_add_cliched(edit))

    edit.exec()