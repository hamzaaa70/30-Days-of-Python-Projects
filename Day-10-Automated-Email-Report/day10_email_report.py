import smtplib
from email.message import EmailMessage

print("     AUTOMATED EMAIL REPORT")

# Read the report
def read_report():

    report_file = open("sales_report.txt", "r")

    report = report_file.read()

    report_file.close()

    return report


# Get the report
report = read_report()


# Create email object
email = EmailMessage()


# Email information
email["From"] = "your_email@gmail.com"
email["To"] = "manager@example.com"
email["Subject"] = "Daily Sales Report"


# Email body
email.set_content(
    "Hello,\n\n"
    "Please find today's sales report below.\n\n"
    + report
)


# Read attachment
with open("sales_report.txt", "rb") as file:

    file_data = file.read()


# Add attachment
email.add_attachment(
    file_data,
    maintype="text",
    subtype="plain",
    filename="sales_report.txt"
)


print()
print("Email created successfully!")
print("Recipient:", email["To"])
print("Subject:", email["Subject"])
print("Attachment: sales_report.txt")