from object_merger import *

sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
sensor_2 = [('knife',1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95) ]
actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print ('Input sensor readings:\n' , sensor_1 , '\n' , sensor_2)
print ('Obtained merged result:\n' , actual, '\n')

sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
sensor_2 = [('keys', 5, 95), ('spoon', 4, 99), ('fork', 3, 99), ('scissor', 2, 95), ('knife',1, 55)]
actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print ('Input sensor readings:\n' , sensor_1 , '\n' , sensor_2)
print ('Obtained merged result:\n' , actual, '\n')

sensor_1 = []
sensor_2 = []
actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print ('Input sensor readings:\n' , sensor_1 , '\n' , sensor_2)
print ('Obtained merged result:\n' , actual, '\n')

sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33)]
sensor_2 = []
actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print ('Input sensor readings:\n' , sensor_1 , '\n' , sensor_2)
print ('Obtained merged result:\n' , actual, '\n')

sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33)]
sensor_2 = [('KNIFE',1, 99), ('SCISSOR', 2, 65), ('SPOON', 3, 33)]
actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print ('Input sensor readings:\n' , sensor_1 , '\n' , sensor_2)
print ('Obtained merged result:\n' , actual, '\n')

sensor_1 = [('knife',1, 99), ('scissor', 2, 65)]
sensor_2 = [('fork', 3, 99), ('spoon', 4, 99)]
actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print ('Input sensor readings:\n' , sensor_1 , '\n' , sensor_2)
print ('Obtained merged result:\n' , actual, '\n')

sensor_1 = [('knife',1, 94),('knife',1, 69),('knife',1, 89)]
sensor_2 = [('knife',1, 99),('fork', 3, 99)]
actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print ('Input sensor readings:\n' , sensor_1 , '\n' , sensor_2)
print ('Obtained merged result:\n' , actual, '\n')

sensor_1 = [('knife',1, 89)]
sensor_2 = [('knife',1, 35)]
sensor_3 = [('knife',1, 69)]
sensor_4 = [('knife',1, 80)]
actual = ObjectListMerger(sensor_1,sensor_2,sensor_3,sensor_4).combined_tuple_list()
print ('Input sensor readings:\n' , sensor_1 , '\n' , sensor_2 , '\n', sensor_3 , '\n', sensor_4)
print ('Obtained merged result:\n' , actual, '\n')
