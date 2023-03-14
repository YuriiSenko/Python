file_from = "../person_data.txt"  # file where data is stored
file_to = "../saltivskiy.txt"  # file to create

# Opening files and assignment of permissions
file1 = open(file_from, mode='r',encoding='ascii')
file2 = open(file_to, mode='a', encoding='ascii')

district_to_look_for = "Saltivskiy"

# Find and move data of people from Saltivskiy district to the created file
for dom in file1:
    if district_to_look_for in dom:
        file2.write(dom)


