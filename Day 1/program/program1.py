def main():
    grade = float(input("Enter Grade:"))

    score(grade)

def score(grade):

    if grade > 4:
        print("Invalid Grade")

    elif (grade >= 3.5):
        print ("Grade A+")

    elif (grade >= 3):
        print ("Grade B")

    elif (grade >= 2):
        print ("Grade C")

    elif (grade < 2):
        print ("Grade D")

if __name__ == "__main__":
    main()

