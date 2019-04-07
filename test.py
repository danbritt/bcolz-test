import os
import pandas
import numpy
import bcolz


project_path = os.path.abspath(os.path.dirname(__file__))
data_dir_path = os.path.join(project_path, 'data')
in_file_path = os.path.join(data_dir_path, 'TEST_DATA.txt')

df = pandas.read_csv(
    in_file_path, 
    engine='c',
    header=None, 
    names=[
        'date', 
        'col_1', 
        'col_2', 
        'col_3', 
        'col_4', 
        'col_5', 
        'col_6', 
        'col_7',
        'col_8',
        'col_9',
        'col_10',
        'col_11',
        'col_12',
        'col_13'
    ],
    dtype={
        'date': numpy.int32,
        'col_1': numpy.int32, 
        'col_2': numpy.int32,
        'col_3': numpy.int32,
        'col_4': numpy.int32,
        'col_5': numpy.int32,
        'col_6': numpy.int32,
        'col_7': numpy.int32,
        'col_8': numpy.int32,
        'col_9': numpy.int32,
        'col_10': numpy.int32,
        'col_11': numpy.int32,
        'col_12': numpy.int32,
        'col_12': numpy.int32
    }
)

print('pandas dataframe size (bytes)')
print(df.memory_usage().sum())

ct = bcolz.ctable.fromdataframe(df)

# Can use this code instead to override default compression params
# It should throw an error, because a compression level of 11 is not valid for blosclz compression method, but it doesn't
# test_compression_params = bcolz.cparams(clevel=11, cname='blosclz')
# ct = bcolz.ctable.fromdataframe(df, cparams=test_compression_params)

print('ctable uncomressed size (btyes)')
print(ct.nbytes)
print('ctable compressed size (bytes)')
print(ct.cbytes)
print('ctable compression params')
print(ct.cparams)