student_data = {"id1" : {"name" : "gowtham", "class":"IX", "subject_integration": "maths,physics,chemistry"},
                "id2" : {"name" : "abhinav", "class": "IX", "subject_integration" : "biology,physics,chemistry"},
                "id3" : {"name" : "gowtham", "class":"IX", "subject_integration": "maths,physics,chemistry"},
                "id4" : {"name" : "surya", "class" : "IX", "subject_integration":"maths,physics,chemistry"},}

result = {}
seen_keys = []

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_integration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)