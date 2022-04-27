# This function creates a dictionary from a list.
def create_dict(input_list):
    output_dict = {}
    for i,j in enumerate(input_list):
        temp_dict = {i:j}
        output_dict.update(temp_dict)
    return output_dict

# Sample print statement
print(create_dict(['jimmy','jimi','hendrix']))