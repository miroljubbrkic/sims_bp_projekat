from database.data_handler import DataHandler
import json
import pickle


class FileHandler(DataHandler):
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
        if self.metadata["type"] == "sequential":
            return self.data[self.binary_search(id, 0, len(self.data))]
        else:
            for d in self.data:
                if getattr(d, (self.metadata["key"])) == id:
                    return d
            return None

    def get_all(self):
        return self.data

    def insert(self, obj):
        if self.metadata["type"] == "sequential":
            location = self.find_location_for_insert(obj)
            if (location == None):
                self.data.append(obj)
            else:
                self.data.insert(location-1, obj)
        else:
            self.data.append(obj)
        self.save_data()

    def insert_many(self, obj_list):
        if len(obj_list) > 0:
            if not isinstance(obj_list, list): #mozda radi 
                return
            if self.metadata["type"] == "sequential":
                for obj in obj_list:
                    self.insert(obj)
            else:
                for obj in obj_list:
                    self.insert(obj)
        self.save_data()

    def edit(self, id, obj):
        for d in self.data:
            if getattr(d, (self.metadata["key"])) == id:
                self.data[d] = obj
        self.save_data()

    def delete_one(self, id):
        for d in self.data:
            if getattr(d, (self.metadata["key"])) == id:
                self.data.remove(self.get_one(id))
        self.save_data()

    def binary_search(self, id, start, end):
        while start <= end:
            mid = start + (end - start)//2
            if getattr(self.data[mid], (self.metadata["key"])) == id:
                return mid
            elif getattr(self.data[mid], (self.metadata["key"])) < id:
                start = mid + 1          
            else:
                end = mid - 1
    
    def find_location_for_insert(self, obj):
        #todo alternativni nacin binarna pretraga
        for i in range(len(self.data)):
            if getattr(self.data[i], (self.metadata["key"])) > getattr(obj, (self.metadata["key"])):
                return i
        return None
