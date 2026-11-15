empty_list = []
print(empty_list)


marks = [85, 72, 90, 66, 78]
print("Student marks:", marks)

sample_list = [10,20,30] * 2
print("Repeated sample marks:", sample_list)

print("Number of marks:", len(marks))


print("First mark:",marks[0])
print("Last mark:",marks[-1])

first_three_marks = marks[0:3]
print("First three marks:", first_three_marks)

reversed_marks = marks[::-1]
print("Reversed marks:", reversed_marks)

def match_marks(marks_list):
    count = 0
    matched_marks = []
    for mark in marks_list:
        mark_text = str(mark)

        if len(mark_text) > 1 and mark_text[0] == mark_text[-1]:
            count += 1
            matched_marks.append(mark)

    print("Marks with first and last digit the same:", matched_marks)
    return count

same_digit_count = match_marks([88, 72, 99, 65, 77])
print("Count of marks with first and last digit the same:", same_digit_count)

total = 0

for mark in marks:
    total += mark

average = total / len(marks)
print("Total marks:", total)

print("Average marks:", average)

marks.sort()
print("Smallest mark:", marks[0])
print("Largest mark:", marks[-1])

print("")

print("===== Student marks list analyzer =====")
print("sorted marks:", marks)
print("Total marks:", total)
print("Average marks:", average)
print("lowest mark:", marks[0])
print("Highest mark:", marks[-1])
