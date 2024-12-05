# PDF Processing with pdfplumber

#### **What It Does**

This script processes a tabular PDF file (e.g., `2017_batch.pdf`) to extract and filter student data. It writes the selected records into a formatted text file (`2017.txt`) based selection strategy ( user choice in this case).

---

#### **How It Works**

0. **Install pdfplumber**
   - `pip install pdfplumber`
1. **PDF Parsing**:
   - Uses the `pdfplumber` library to extract tables from the PDF.
2. **Field Extraction**:
   - Extracts fields like SNO, ID No., Full Name, Gender, and Section from each row.
3. **Interactive Filtering**:

   - Prompts the user to decide for each record:
     - **`d`**: Include in the output.
     - **`f`**: Mark as "maybe" (adds `*` to the record).
     - **Any other key**: Exclude the record.

4. **Formatted Output**:
   - Saves selected records to `2017.txt` in a neatly formatted table with column widths.

---

#### **Usage**

1. Place the input PDF (`2017_batch.pdf`) in the same directory or provide its path in the script.
2. Run the script: `python <script_name>.py`.
3. Follow the prompts to filter records.
4. The processed data will be saved to `2017.txt`.
