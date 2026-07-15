student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#looping through dictionary
# for key, value in student_dict.items():
#     print (value)

import pandas

student_data_frame = pandas.DataFrame(student_dict)

#loop through a data frame
# for (key, value) in student_data_frame.items():
#     print


#loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row.student)
    if row.student == "Angela":
        print(row.score)


# {new_key:new_value for (index, row) in df.iterrows()}