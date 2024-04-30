import textwrap
from PyPDF2 import PdfReader


def parse_pdf(pdf_file):
    pdf_reader = PdfReader(pdf_file)
    pdf_text = ""

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_text += page.extract_text()

    return pdf_text


def wrap_text(text, wrap_width=35):
    wrapped_text = textwrap.fill(
        textwrap.dedent(text),
        width=wrap_width,
        initial_indent="• ",
        subsequent_indent=" " * 2,
    )
    return wrapped_text
