# Separate each module grade from the string e.g C+, A, C, D- 

# ================= Method 1 - Me =================
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


# ================= Method 2 - Most efficient By Andy the coder =================
string = "C+ACD-"
grades = []
for i in range(0,len(string)):
    if((i+1) < len(string) and string[i+1] in '+-*'):
        grades.append("{}{}".format(string[i],string[i+1]))
    elif(string[i]  in '+-*' ):
        continue
    else:
        grades.append(string[i])
    
print(grades)
        
# ================= Method 3 - GW Senior =================
ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
grades = []

current_grade = ""

string = "C+ACD-"

for char in string:
    if char == "+" or char == "-":
        current_grade += char
        grades.append(current_grade)
        current_grade = ""
        
    elif len(current_grade) == 1 and ALPHABETS.find(char) > -1:
        grades.append(current_grade)
        current_grade = ""
        current_grade += char
        
    else:
        current_grade += char

print(grades)
        
        
    
    
    
    
