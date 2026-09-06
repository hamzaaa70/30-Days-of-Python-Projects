import pandas as pd

print("MESSY EXCEL DATA CLEANER")


#Messy company data

data = {
    'name':[
        "UMER KHAN",
        "ZAKRIA",
        "AYAN ali",
        "SHAHAB mutail",
        "WADOOD KHAN",
        "WISAL khan",
        "WISAL KHAN",
            None
    ],


"Email":[
    "umer1@gmail.com",
    "zakria3@gmail.com",
    "ayanali33@gmail.com",
    "shahzab5672@gmail.com",
    "wadoodkhan33@gmail.com",
    "wisal0837@gmail.com",
    "dawood232088@gmail.com",
    None


],

"Age": [
        "22",
        "25",
        "28",
        "22",
        "30",
        "28",
        "23",
        None
],
  "Salary": [
        "80000",
        "95000",
        "110000",
        "80000",
        "120000",
        "110000",
        None
    ]

}

#create datafram

df = pd.DataFrame(data)

#Save the messy data

df.to_excel("messy_dataa.xlsx",index=False)

print("messy excel file created")

import pandas as pd


print("=== COMPANY DATA CLEANER ===")


# Read Excel file
df = pd.read_excel("messy_data.xlsx")


print("\nOriginal Data:")
print(df)


# Remove completely empty rows
df = df.dropna(how="all")


# Clean names
df["Name"] = df["Name"].str.strip()


# Clean emails
df["Email"] = df["Email"].str.strip().str.lower()


# Convert Age to numbers
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")


# Convert Salary to numbers
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")


# Remove duplicate records
df = df.drop_duplicates()


# Remove rows where important information is missing
df = df.dropna(subset=["Name", "Email"])


# Save cleaned data
df.to_excel("cleaned_data.xlsx", index=False)


print("\nCleaned Data:")
print(df)


print("\nData cleaning completed!")
print("Cleaned file saved as cleaned_data.xlsx")