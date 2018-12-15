class Object:
    def __init__(self, name, number, confidence):
        self.name = name.lower()
        self.number = number
        self.confidence = confidence

class ListHandler:
    # Converts from a list of tuples to a list of objects
    def tuple_list_to_object_list(self, tuple_list):
        object_list = [Object(*item_params)  for item_params in tuple_list]
        return object_list

    # Converts from a list of objects to a list of tuples
    def object_list_to_tuple_list(self, object_list):
        tuple_list = [(obj.name,obj.number,obj.confidence) for obj in object_list]
        return tuple_list

    # Combines a list of lists to a single list
    def combine_lists(self,list_of_lists):
        combined_list = []
        for each_list in list_of_lists:
            combined_list.extend(each_list)
        return combined_list

class MergingAlgorithm:
    # Returns a list of objects having the highest confidence for each unique object number
    def merge_objects(self,list_of_object_lists):
        combined_object_list = ListHandler().combine_lists(list_of_object_lists)
        merged_object_list = []
        while combined_object_list:
            sensor_reading = combined_object_list.pop()
            reading_params = [sensor_reading.name, sensor_reading.number, sensor_reading.confidence]
            index = 0
            while index < len(combined_object_list):
                if reading_params[1] == combined_object_list[index].number:
                    new_reading = combined_object_list.pop(index)
                    if new_reading.confidence > reading_params[2]:
                        reading_params[0], reading_params[2] = new_reading.name, new_reading.confidence
                else:
                    index += 1
            merged_object_list.append(Object(*reading_params))
        return merged_object_list

class ObjectListMerger:
#args: takes in readings from sensors as lists of tuples
    def __init__(self,*args):
        self.sensors_object_list = []
        for arg in args:
            self.sensors_object_list.append(ListHandler().tuple_list_to_object_list(arg))

    # Merges the lists of objects from the sensor and creates output as a list of objects
    def merge_objects(self,merging_algorithm):
        return merging_algorithm.merge_objects(self.sensors_object_list)

    # Calls the merge_objects method and returns output as a list of tuples
    def combined_tuple_list(self):
        merged_object_list = self.merge_objects(MergingAlgorithm())
        tuple_list = ListHandler().object_list_to_tuple_list(merged_object_list)
        return tuple_list

sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
sensor_2 = [('knife',1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95) ]

actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print '\n'
print 'For the sensor readings'
print sensor_1
print sensor_2
print 'we obtained:'
print actual

sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
sensor_2 = [('keys', 5, 95), ('spoon', 4, 99), ('fork', 3, 99), ('scissor', 2, 95), ('knife',1, 55)]

actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print '\n'
print 'For the sensor readings'
print sensor_1
print sensor_2
print 'we obtained:'
print actual

sensor_1 = []
sensor_2 = []

actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print '\n'
print 'For the sensor readings'
print sensor_1
print sensor_2
print 'we obtained:'
print actual

sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33)]
sensor_2 = []

actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print '\n'
print 'For the sensor readings'
print sensor_1
print sensor_2
print 'we obtained:'
print actual

sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33)]
sensor_2 = [('KNIFE',1, 99), ('SCISSOR', 2, 65), ('SPOON', 3, 33)]

actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print '\n'
print 'For the sensor readings'
print sensor_1
print sensor_2
print 'we obtained:'
print actual

sensor_1 = [('knife',1, 99), ('scissor', 2, 65)]
sensor_2 = [('fork', 3, 99), ('spoon', 4, 99)]

actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print '\n'
print 'For the sensor readings'
print sensor_1
print sensor_2
print 'we obtained:'
print actual

sensor_1 = [('knife',1, 94),('knife',1, 69),('knife',1, 89)]
sensor_2 = [('knife',1, 99),('fork', 3, 99)]

actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print '\n'
print 'For the sensor readings'
print sensor_1
print sensor_2
print 'we obtained:'
print actual

sensor_1 = [('knife',1, 89)]
sensor_2 = [('knife',1, 35)]
sensor_3 = [('knife',1, 69)]
sensor_4 = [('knife',1, 80)]

actual = ObjectListMerger(sensor_1,sensor_2,sensor_3,sensor_4).combined_tuple_list()
print '\n'
print 'For the sensor readings'
print sensor_1
print sensor_2
print 'we obtained:'
print actual
print '\n'
