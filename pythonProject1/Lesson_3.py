ll = [0, 1, 2, 3, 4, 5, 'qw', True, False, [12, 'sw'], {'nn': 55}]

dict_data = {
    'name' : 'Aleksei',
    'age': 32,
    'weight' : 85,
    'food' : {'milk' : ['Sirnichki', 'milk', 'protein', 'tvorog'],
              'meat' : ['pelmeni', 'meat', 'sosiska v teste'] },
    'salary' : [250, 320, 700, 1100, 1200, 1500, 2000]
    }
count = 0
key_list = []
for key, value in dict_data.items():
    if value == 'food':
        key_list = value['milk']
   # print(key, '==', value)

        print('==================')
        print(key_list)

#for i in key_list:
 #   print(i)
