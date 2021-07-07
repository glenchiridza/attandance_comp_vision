from datetime import datetime

a = ["Glen Chiridza", "Wendy Chiridza"]

if "Glen Chiridza" in a:
    print("He is present")
else:
    print("not present")


def attandance_record(name):
    with open('students.csv', 'r+') as file:
        contents = file.readlines()
        student_names = []
        print(contents)
        for line in contents:
            item = line.split(",")
            student_names = item[0]

        if name in student_names:
            print(name,"is already present")
        else:
            date = datetime.now()
            date_string = date.strftime('%H:%M:%S')
            file.writelines(f"\n{name} , {date_string}")
            print("yooo", name)


attandance_record("Wendy Chiridza")

if __name__ == "__main__":
    pass
