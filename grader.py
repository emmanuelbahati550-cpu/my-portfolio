# ==============================================================================
# APEX AUTOMATED DATA ENTRY TERMINAL (GRADER ENGINE)
# ==============================================================================

def get_valid_score(subject_name):
    """Ensures the user inputs a valid integer between 0 and 100."""
    while True:
        try:
            score = int(input(f"Enter {subject_name} Mark (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("❌ Invalid Range! Please enter a score between 0 and 100.")
        except ValueError:
            print("❌ Invalid Input! Please enter a whole number (e.g., 85).")

print("==========================================")
print("    APEX AUTOMATED DATA ENTRY TERMINAL    ")
print("==========================================\n")

# Use input() to capture live typing from your keyboard into RAM variables
student_name = input("Enter Student Name: ").strip()
if not student_name:
    student_name = "Anonymous Student"

# Safely get scores using our new function
comp_score = get_valid_score("Computer Studies")
math_score = get_valid_score("Mathematics")

# Calculations
total = comp_score + math_score
average = total / 2

# Grade logic
if average >= 80:
    grade = "Grade A (Excellent Code Logic)"
elif average >= 60:
    grade = "Grade B"
else:
    grade = "Pass"

# Terminal Output Display
print("\n" + "-" * 42)
print(f"Processing Report Card for: {student_name}")
print(f"Final Calculated Average: {average:.2f}%")
print(f"Academic Standing: {grade}")
print("-" * 42)

# Safely exporting report card to Desktop/Local Directory
try:
    with open("Live_Report.txt", "w") as report:
        report.write(f"OFFICIAL REPORT FOR: {student_name}\n")
        report.write(f"Computer Studies: {comp_score}%\n")
        report.write(f"Mathematics: {math_score}%\n")
        report.write(f"Calculated Outcome: {grade}\n")
    print("\n⚡ Success! Custom data compiled into 'Live_Report.txt' on Desktop.")
except Exception as e:
    print(f"\n⚠️ Could not write file. Error details: {e}")
