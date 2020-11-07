# a = 10, a adalah variable dengan nilai 10

# tipe data: angka satuan (integer) tidak ada komanya
data_integer = 10000

print(type(data_integer))  # untuk menampilkan tipe data di terminal
print('data : ', data_integer, 'bertipe : ', type(data_integer))

# tipe data: angka dengan koma (float)
data_float = 1.5
print('data : ', data_float, 'bertipe : ', type(data_float))

# tipe data: kumpulan karakter (string)
data_string = 'arif budiman arrosyid'
print('data : ', data_string, 'bertipe : ', type(data_string))

# tipe data: biner true false (boolean)
data_bool = True
print('data : ', data_bool, 'bertipe : ', type(data_bool))

# tipe data khusus
# bilangan kompleks
data_complex = complex(5, 6)
print('data : ', data_complex, 'bertipe : ', type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double
data_c_double = c_double(10.5)
print('data : ', data_c_double, 'bertipe : ', type(data_c_double))