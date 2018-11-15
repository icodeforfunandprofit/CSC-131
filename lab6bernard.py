#User Defined Functions
#------------------------


#main
#------------------------
def main():
    print("This program calculates semester and cumulative GPAs \n")

    total_credits = int(input("Enter total number of earned credits: "))
    cumulative_gpa = float(input("Enter your current cumulative GPA: "))

    cumulative_gpa_info = (cumulative_gpa, total_credits)

main()
