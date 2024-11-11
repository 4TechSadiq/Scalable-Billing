from docxtpl import DocxTemplate, InlineImage #Document updation and adding data
from docx.shared import Mm #Defining size of logo 
import fitz #used for converting PDF to image
from docx2pdf import convert #For converting docx to pdf
import os #For removing files



#Function to make invoice
def invoice(template, name, logo, date, invoice_number, company_address, invoice_to, amount):
    document = DocxTemplate(template)

    #Datas inside the Invoice
    #Customize as required. The name of the keys in the values must be same as the keys in the invoice.
    #The values must follow Order.
    # context = {
    #     'logo': InlineImage(document, logo, width=Mm(25)),#To set Logo or images in the invoice.
    #     'date': date,
    #     'invoice_number': invoice_number,
    #     'company_address': company_address,
    #     'invoice_to': invoice_to,
    #     'amount': amount
    # }

    context = {
        'billing_date': date,
        'billing_time': billing_time,
        'invoice_no': invoice_number,
        'biller_name': biller_name,
        'business_name': business_name,
        'customer_name': customer_name,
        'customer_address': customer_address,
        'mode_of_payment': mode_of_payment,
        'service_desc': service_name,
        'service_cost'
    }

    #Rendering Document
    document.render(context)

    #Saving Document
    document.save(f'{name}.docx')
    #Converting docx to pdf
    convert(f'{name}.docx', f'{name}.pdf')
    #Converting PDF to Image
    with fitz.open(f'{name}.pdf') as pdf_doc:
        for pg in range(pdf_doc.page_count):
            page = pdf_doc.load_page(pg)
            #Scalling Resolution of Image
            mat = fitz.Matrix(2, 2)
            pix = page.get_pixmap(matrix=mat)
            image = f"{name}.png"
            pix.save(image)
        print(f"Saved {image}")


    #Removing Temp Files
    if image: #f'{name}.png': #in os.listdir():
        os.remove(f'{name}.docx')
        os.remove(f'{name}.pdf')

    return image
        

#Tesing Function
# invoice("invoice.docx", "demo", "image.png", "July 8, 2019", "1234", "company address", "invoice to address", "1000.00")