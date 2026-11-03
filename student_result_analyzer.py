def collect_students():
    students=[]
    i=1
    while True:
        number=input("How many students should be added?: ")
        if number.replace(" ","").isdigit():
            number=int(number.replace(" ",""))
            if number>0:
                while i<=number:
                    name=input("Student's Name: ")
                    if name.replace(" ","").isalpha():
                        while True:
                            try:
                                marks=int(input("Enter Marks: "))
                            except ValueError:
                                print("Invalid Input")
                            else:
                                if marks<0 or marks>100:
                                    print("Invalid Marks")
                                    continue
                                else:
                                    students.append([name,marks])
                                    break
                    else:
                        print("Invalid Input")
                        continue
                    i+=1
            else:
                print("Invalid Input")
                continue
        else:
            print("Invalid Input")
            continue
        break
    return students
data=collect_students()
def analyze_students(data):
    passed=[]
    failed=[]
    for score in data:
        if score[1]>=40:
            passed.append(score)
        elif score[1]<40:
            failed.append(score)
    return passed,failed
passed_students,failed_students=analyze_students(data)
print(f"Passed:\n{passed_students}\n\nFailed:\n{failed_students}")

     

                


