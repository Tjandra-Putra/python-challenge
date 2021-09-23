# Separate each module grade from the string e.g C+, A, C, D- 

grade = "C+ACD-"

grade_char_list = list(grade)
print(grade_char_list)

formatted_grade_list = []

for index in range(0, len(grade_char_list)):
    prev_char = ''
    current_char = grade_char_list[index]
    
    if current_char in "-+*":
        if index > 0 :
            prev_char = grade_char_list[index-1]
            formatted_char = prev_char + grade_char_list[index]
            
            formatted_grade_list.append(formatted_char)
    else:
        next_char = grade_char_list[index+1]
        
        if next_char not in "-+*":
            formatted_grade_list.append(current_char)


print(formatted_grade_list)
    
    
    
    