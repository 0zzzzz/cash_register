import pdfkit
from django.template.loader import render_to_string


def create_pdf(items, template, pdf_name):
    print(1)
    html = render_to_string(template, context=items)

    pdf_path = f'media/pdf/{pdf_name}.pdf'
    config = pdfkit.configuration(wkhtmltopdf=r"/usr/bin/wkhtmltopdf")
    pdfkit.from_string(html, pdf_path, configuration=config)
