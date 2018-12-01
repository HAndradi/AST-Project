class TupleList:
    # Creates an object from a list of tuples
    def __init__(self, tuple_list):
        self.tuple_list = tuple_list

    # Converts from a list of tuples to a list of objects
    def to_object_list(self):
        object_list = [Object(*item_parameters)  for item_parameters in self.tuple_list]
        return object_list

class Object:
    def __init__(self, name, number, confidence):
        self.name = name
        self.number = number
        self.confidence = confidence

class ObjectListMerger:
#args: takes in readings from sensors as lists of tuples
    def __init__(self,*args):
        self.sensors_object_list = []
        self.merged_object_list = []
        for arg in args:        
            sensor_readings = TupleList(arg)
            self.sensors_object_list.append(sensor_readings.to_object_list())

    # Merges the lists of objects from the sensor and creates output as a list of objects
    def merge_objects(self):
        for sensor_num,sensor in enumerate(self.sensors_object_list):
            while len(sensor)>0:
                sensor_reading = sensor.pop()
                reading_parameters = [sensor_reading.name, sensor_reading.number, sensor_reading.confidence]
                for remaining_sensor in self.sensors_object_list[sensor_num + 1:]:
                    for remaining_sensor_reading in remaining_sensor:
                        if reading_parameters[1] == remaining_sensor_reading.number:
                            if remaining_sensor_reading.confidence > reading_parameters[2]:
                                reading_parameters[2] = remaining_sensor_reading.confidence
                                reading_parameters[0] = remaining_sensor_reading.name
                            remaining_sensor.remove(remaining_sensor_reading)
                self.merged_object_list.append(Object(*reading_parameters))
      
    # Calls the merge_objects method and returns output as a list of tuples            
    def combined_tuple_list(self):
        self.merge_objects()
        tuple_list = [(obj.name,obj.number,obj.confidence) for obj in self.merged_object_list]
        return tuple_list
