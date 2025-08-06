total = 0 
count = 0

while True:
    marks = input("Marks (or 'avrg' for average): ")
    
    if marks.lower() == 'avrg':
        break
    
    marks = int(marks)
    total += marks
    count += 1

average = total / count
print("Average:", average)

