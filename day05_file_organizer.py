from pathlib import Path
import shutil

folder = Path("test_files")

pdf_folder = folder / "PDFs"
excel_folder = folder / "Excel"
csv_folder = folder / "CSV"
image_folder = folder / "Images"
powerpoint_folder = folder / "PowerPoint"

pdf_folder.mkdir(exist_ok=True)
excel_folder.mkdir(exist_ok=True)
csv_folder.mkdir(exist_ok=True)
image_folder.mkdir(exist_ok=True)
powerpoint_folder.mkdir(exist_ok=True)


for file in folder.iterdir():

    if file.is_dir():
        continue

    extension = file.suffix.lower()

    if extension == ".pdf":
        shutil.move(str(file), str(pdf_folder / file.name))

    elif extension == ".xlsx":
        shutil.move(str(file), str(excel_folder / file.name))

    elif extension == ".csv":
        shutil.move(str(file), str(csv_folder / file.name))

    elif extension in [".jpg", ".jpeg", ".png"]:
        shutil.move(str(file), str(image_folder / file.name))

    elif extension == ".pptx":
        shutil.move(str(file), str(powerpoint_folder / file.name))


print("Files organized successfully! ")