import os
from docx2pdf import convert

# === 1. Define your input and output paths ===
input_path = r"C:\Users\OJ 001\Downloads\NWH - Optometrists Specialist RCO Contract Revised Nov 2022 (1).docx"
output_folder = r"C:\Users\OJ 001\Desktop\Converted"
output_path = os.path.join(output_folder, "Contract.pdf")

# === 2. Create output folder if it doesn't exist ===
os.makedirs(output_folder, exist_ok=True)

# === 3. Convert the .docx to .pdf ===
try:
    convert(input_path, output_path)
    print(f"✅ PDF successfully saved at:\n{output_path}")
except Exception as e:
    print("❌ Conversion failed:")
    print(e)