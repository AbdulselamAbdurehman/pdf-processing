
import pdfplumber
def run():
    pdf_path = '2017_batch.pdf'
    output = open('2017.txt', 'w')

    widths = [10, 15, 50, 15, 30]

    output.write("SNO".ljust(widths[0]) + "ID No.".ljust(widths[1]) + "Full Name".ljust(widths[2]) + "Gender".ljust(widths[3]) + "Section".ljust(widths[4]))

    names = [['SNO', 'ID No.', 'Full Name', 'Gender', 'Section']]

    with pdfplumber.open(pdf_path) as pdf:
        pages = pdf.pages
        for page in pages:
            table = page.extract_table()
            for row in table:
                try:
                    if row[1] != None:
                        index = id_no = full_name = gender = section = None

                        for field in row:
                            if field == None:
                                continue
                            elif field.replace(" ", "").isnumeric():
                                index = field
                            elif field.replace(" ", "").startswith("UGR"):
                                id_no = field
                            elif field.replace(" ", "").isalpha() and len(field) == 1:
                                gender = field
                            elif field.startswith("English"):
                                section = field.split()[-1][:-1]
                            elif field.replace(" ", "").isalpha():
                                full_name = field
                        if None in [index, id_no, full_name, gender, section]:
                            continue

                        decision = input(f"{full_name} : (d = yes, f = maybe, _ = no): ")

                        # if there is selection strategy, you can add it here
                        if decision != "d":
                            output.write(index.ljust(widths[0]) + id_no.ljust(widths[1]) + full_name.ljust(widths[2]) + gender.ljust(widths[3]) + section.ljust(widths[4]) + "\n")
                        elif decision == "f":
                            output.write(("*" + index).ljust(widths[0]) + id_no.ljust(widths[1]) + full_name.ljust(widths[2]) + gender.ljust(widths[3]) + section.ljust(widths[4]) + "\n")

                except Exception as e:
                    print(e)

    output.close()


run()