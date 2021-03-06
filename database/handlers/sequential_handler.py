import json
import pickle
import os

class SequentialHandler:
    def __init__(self, meta_filepath, filepath):
        super().__init__()
        self.filepath = "database/data/" + filepath
        self.meta_filepath = "database/metadata/" + meta_filepath
        self.metadata = {}
        self.load_metadata()

    def load_metadata(self):
        try:
            with open(self.meta_filepath, "r") as meta_file:
                self.metadata = json.load(meta_file)
        except FileNotFoundError:
            print("Meta file nije pronadjen!")

    def get_all(self):
        try:
            with open(self.filepath, "r") as f:
                lines = f.read().splitlines()
                data = []
                for d in lines:
                    data.append(self.to_dict(d))
                return data
        except FileNotFoundError:
            print("Meta file nije pronadjen!")

    def insert(self, obj): 
        if os.path.exists(self.filepath):
            counter = 0
            at_end = False
            found = False
            with open(self.filepath, "r") as fr:
                while True:
                    line = fr.readline().strip()
                    if line == "":
                        break
                    current_line = self.to_dict(line)
                    if self.concat(obj) < self.concat(current_line):
                        found = True
                        break
                    counter += 1
                if found == False:
                    at_end = True
            c_counter = 0
            with open(self.filepath, "r") as fr:
                with open(self.filepath+"_temp", "w") as tempfw:
                    while True:
                        line = fr.readline().strip()
                        if line == "":
                            break
                        current_line = self.to_dict(line)
                        if c_counter == counter:
                            tempfw.write(self.to_text(obj))
                        tempfw.write(line + "\n")
                        c_counter += 1
                    if at_end:
                        tempfw.write(self.to_text(obj))
            os.remove(self.filepath)
            os.rename(self.filepath+"_temp", self.filepath)

    def edit(self, obj, attr, value):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as fr:
                with open(self.filepath+"_temp", "w") as tempfw:
                    found = False
                    while True:
                        line = fr.readline().strip()
                        if line == "":
                            break
                        current_line = self.to_dict(line)
                        if obj == current_line and found == False:
                            found = True
                            new_value = obj
                            new_value[attr] = value
                            tempfw.write(self.to_text(new_value))
                            continue
                        tempfw.write(line + "\n")
            os.remove(self.filepath)
            os.rename(self.filepath+"_temp", self.filepath)

    def delete_one(self, obj):
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as fr:
                with open(self.filepath+"_temp", "w") as tempfw:
                    deleted = False
                    while True:
                        line = fr.readline().strip()
                        if line == "":
                            break
                        current_line = self.to_dict(line)
                        if obj == current_line and deleted == False:
                            deleted = True
                            continue
                        tempfw.write(line + "\n")
            os.remove(self.filepath)
            os.rename(self.filepath+"_temp", self.filepath)
                 
    def to_dict(self, line):
        return dict(zip(self.metadata["collumns"], list(line.split(" <|> "))))

    def to_text(self, current_dict):
        return str(" <|> ".join(current_dict.values())) + '\n'

    def concat(self, keys):
        primary_key = ""
        for i in range(len(self.metadata["key"])):
            primary_key += str(keys[self.metadata["key"][i]])
        return primary_key

    def is_database(self):
        return False