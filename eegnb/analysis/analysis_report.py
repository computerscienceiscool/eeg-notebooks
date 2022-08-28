"""
File that has the functions to generate the analysis report pdf from the images

Usage Instructions typically ::

from eegnb.analysis.analysis_report import PDF
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
# Do whatever you want to add to the pdf
pdf.save_as_report()


# Work that needs to be done
1. Add boilerplate text
2. Figure stretching for raw plot
3. Add subject and session info
"""

from fpdf import FPDF
import matplotlib.pyplot as plt
import numpy as np
import os

class PDF(FPDF):
    def header(self):
        
        # Arial bold 15
        self.set_font('Arial', 'B', 25)
        self.set_text_color(183, 208, 332)
        # Move to the right
        #self.cell(80)
        # Title
        self.cell(0, 10, 'Analysis Report')
        # Line break
        self.ln(20)
    
    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

    def add_figure(self, fig_path, x, y, w, h, title):

        #self.cell(w=100,h=10, txt=title, ln=0, align='C')
        self.set_font('Times', 'B', 20)
        
        # Add figure to document
        self.cell(0, 10, txt=title, ln=2, align='C')
        self.image(fig_path, x=x, y=y, w=w, h=h)
        self.ln(h+10)
        # Delete figure from memory
        os.remove(fig_path)

