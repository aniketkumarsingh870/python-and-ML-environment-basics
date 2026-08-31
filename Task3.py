import pandas as pd

# Create data for 10 students
data = {
    "student_name": ["Rahul", "Priya", "Amit", "Sneha", "Ravi","Anjali", "Vikash", "Neha", "Arjun", "Pooja"],
    "roll no": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "marks": [85, 78, 92, 67, 88, 95, 73, 81, 79, 90],
    "attendance": [90, 85, 95, 80, 92, 98, 88, 91, 84, 96]
}

# Create DataFrame
df = pd.DataFrame(data)
#function to calculate grade.
def cal_grade(marks):
    if marks > 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    else:
        return "D"

# dynamically calculated grade column
df["grade"] = df["marks"].apply(cal_grade)

# Display DataFrame
print(df)
