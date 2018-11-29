class TupleList:
    # Creates an object from a list of tuples
    def __init__(self, tuple_list):
        self.tuple_list = tuple_list

    # Converts from a list of tuples to a list of objects
    def to_object_list(self):
        return None

class Object:
    def __init__(self, name, number, confidence):
        pass

class ObjectListMerger:
    # args: takes in readings from sensors as lists of tuples and converts to lists of objects
    def __init__(self,*args):
        pass

    # Merges the lists of objects from the sensor and creates output as a list of objects
    def merge_objects(self):
	pass
      
    # Calls the merge_objects method and returns output as a list of tuples            
    def combined_tuple_list(self):
        return None
