print("==========================================")
print("   APEX AUTOMATED DATA ENTRY TERMINAL     ")
print("==========================================\n")

# Use input() to capture live typing from your keyboard into RAM variables
student_name = input("Enter Student Name: ")
comp_score = int(input("Enter Computer Studies Mark (0-100): "))
math_score = int(input("Enter Mathematics Mark (0-100): "))

# Dynamic array calculations
total = comp_score + math_score
average = total / 2

if average >= 80:
    grade = "Grade A (Excellent Code Logic)"
elif average >= 60:
    grade = "Grade B"
else:
    grade = "Pass"

print("\n" + "-" * 42)
print(f"Processing Report Card for: {student_name}")
print(f"Final Calculated Average: {average:.2f}%")
print(f"Academic Standing: {grade}")
print("-" * 42)

# Exporting the user-inputted data safely to your desktop
with open("Live_Report.txt", "w") as report:
    report.write(f"OFFICIAL REPORT FOR: {student_name}\n")
    report.write(f"Computer Studies: {comp_score}%\n")
    report.write(f"Mathematics: {math_score}%\n")
    report.write(f"Calculated Outcome: {grade}\n")

print("\nSuccess! Custom data compiled into 'Live_Report.txt' on Desktop.")

