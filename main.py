from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Get current Y position
    line_y_position = pdf.get_y()

    while line_y_position < pdf.h - 10:  # Stop before reaching the bottom
        pdf.line(10, line_y_position, 200, line_y_position)
        line_y_position += 10  # Spacing of 10mm between lines

    # Set the Footer
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        # Get current Y position
        line_y_position = pdf.get_y()

        while line_y_position < pdf.h - 10:  # Stop before reaching the bottom
            pdf.line(10, line_y_position, 200, line_y_position)
            line_y_position += 10  # Spacing of 10mm between lines

    # Set the Footer
    pdf.ln(277)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("output.pdf")
