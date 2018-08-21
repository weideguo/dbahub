#!/bin/env python

def dict_to_file(dict_name,output_file,output_method='w'):
    output_dir=os.path.dirname(output_file)
    if os.path.exists(output_dir)!=True:
        os.makedirs(output_dir)
    with open(output_file,output_method) as f:
        for item in dict_name.keys():
            item_value = "%s %s \n" % (item,dict_name[item])
            f.write(item_value)
