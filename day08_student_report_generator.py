from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

# STUDENT INFORMATION

name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
semester = input("Enter semester: ")

print("\nEnter marks:")

python_marks = float(input("Python: "))
database_marks = float(input("Database: "))
statistics_marks = float(input("Probability & Statistics: "))
computer_marks = float(input("Computer Organization: "))



# CALCULATIONS


total = (
    python_marks
    + database_marks
    + statistics_marks
    + computer_marks
)

average = total / 4

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# CREATE PDF

file_name = "student_report.pdf"

pdf = SimpleDocTemplate(
    file_name,
    pagesize=A4
)

# STYLES

styles = getSampleStyleSheet()

title_style = styles["Title"]
title_style.alignment = TA_CENTER

normal_style = styles["Normal"]

# PDF CONTENT

content = []

content.append(
    Paragraph("STUDENT REPORT", title_style)
)

content.append(Spacer(1, 20))

content.append(
    Paragraph(f"<b>Name:</b> {name}", normal_style)
)

content.append(
    Paragraph(f"<b>Roll Number:</b> {roll_no}", normal_style)
)

content.append(
    Paragraph(f"<b>Semester:</b> {semester}", normal_style)
)

content.append(Spacer(1, 20))



# SUBJECT TABLE


table_data = [
    ["Subject", "Marks"],
    ["Python", python_marks],
    ["Database", database_marks],
    ["Probability & Statistics", statistics_marks],
    ["Computer Organization", computer_marks],
    ["Total", total],
    ["Average", f"{average:.2f}%"],
    ["Grade", grade]
]


table = Table(table_data, colWidths=[300, 100])

table.setStyle(
    TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (1, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, -3), (-1, -1), "Helvetica-Bold"),
        ("BACKGROUND", (0, -3), (-1, -1), colors.lightgrey),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
        ("TOPPADDING", (0, 0), (-1, 0), 10),
    ])
)


content.append(table)

content.append(Spacer(1, 30))

content.append(
    Paragraph(
        "Generated automatically using Python.",
        normal_style
    )
)



# SAVE PDF


pdf.build(content)

print(f"\nPDF generated successfully: {file_name}")