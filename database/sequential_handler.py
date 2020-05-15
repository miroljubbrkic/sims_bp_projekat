from database.data_handler import DataHandler
import json
import pickle


class SequentialHandler(DataHandler):
    def __init__(self, filepath, meta_filepath):
        super().__init__()
        self.filepath = "database/data/" + filepath
        self.meta_filepath = "database/metadata/" + meta_filepath
        self.data = []
        self.metadata = {}
        self.load_data()

    def load_data(self):
        try:
            with open(self.filepath, "rb") as dfile:
                self.data = pickle.load(dfile)
        except FileNotFoundError:
            print(self.filepath)
            print("File nije pronadjen!")
            self.save_data()
            print("File kreiran!")
        
        try:
            with open(self.meta_filepath, "rb") as meta_file:
                self.metadata = json.load(meta_file)
        except FileNotFoundError:
            print(self.meta_filepath)
            print("Meta file nije pronadjen!")

    def save_data(self):
        with open(self.filepath, "wb") as f:
            pickle.dump(self.data, f)

    def get_one(self, id):
        temp_object = self.data[self.binary_search(id, 0, (len(self.data)))]
        if temp_object is not None:
            return temp_object
        else:
            print("Objekat nije pronadjen!")

    def get_all(self):
        return self.data

    def insert(self, obj):
        location = self.find_location_for_insert(obj)
        if (location == None):
            self.data.append(obj)
        else:
            self.data.insert(location-1, obj)
        self.save_data()

    def insert_many(self, obj_list):
        if len(obj_list) > 0:
            if not isinstance(obj_list, list):
                return
            for obj in obj_list:
                self.insert(obj)

    def edit(self, id, obj):
        self.data[self.binary_search(id, 0, (len(self.data)))] = obj
        self.save_data()

    def delete_one(self, id):
        temp_object = self.data[self.binary_search(id, 0, (len(self.data)))]
        if temp_object is not None:
            self.data.remove(temp_object)
            self.save_data()

    def binary_search(self, id, start, end):
        while start <= end:
            middle = start + (end - start)//2
            if getattr(self.data[middle], (self.metadata["key"])) == getattr(id, (self.metadata["key"])):
                return middle
            elif getattr(self.data[middle], (self.metadata["key"])) < getattr(id, (self.metadata["key"])):
                start = middle + 1
            else:
                end = middle - 1
        return None

    def find_location_for_insert(self, obj):
        for i in range(len(self.data)):
            if getattr(self.data[i], (self.metadata["key"])) > getattr(obj, (self.metadata["key"])):
                return i
        return None

    def selection_sort(self):
        for i in range(len(self.data)-1):
            j_min = i
            for j in range(i+1, len(self.data)):
                if getattr(self.data[j], (self.metadata["key"])) < getattr(self.data[j_min], (self.metadata["key"])):
                    j_min = j
            if i != j_min:
                self.data[i], self.data[j_min] = self.data[j_min], self.data[i]