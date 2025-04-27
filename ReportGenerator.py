from fpdf import FPDF
import csv


def read_sales_data(file):
    sales_data = []
    with open(file, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"Row: {row}")  
            row['Quantity'] = int(row['Quantity'])
            row['Price'] = int(row['Price'])
            sales_data.append(row)
    return sales_data

def generate_pdf_report(sales, total_revenue, top_product, product_sales):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Sales Report", ln=True, align='C')
    pdf.ln(10)

    pdf.cell(200, 10, "Sales Data:", ln=True)
    for sale in sales:
      
        line = f"{sale['Date']} - {sale['Product']} x {sale['Quantity']} @ Rs{sale['Price']} = Rs{sale['Quantity'] * sale['Price']}"
        pdf.cell(200, 10, line, ln=True)

    pdf.ln(10)
    pdf.cell(200, 10, f"Total Revenue: Rs{total_revenue:.2f}", ln=True)
    pdf.cell(200, 10, f"Top Product: {top_product[0]} (Rs{top_product[1]:.2f})", ln=True)

    pdf.output("sales_report.pdf")
    print("Report generated: sales_report.pdf")


file = file = "C:/Users/Bharath/Documents/Lovely's Documents/SalesData.csv"  
sales = read_sales_data(file)


total_revenue = sum([sale['Quantity'] * sale['Price'] for sale in sales])
product_sales = {}
for sale in sales:
    if sale['Product'] not in product_sales:
        product_sales[sale['Product']] = 0
    product_sales[sale['Product']] += sale['Quantity'] * sale['Price']

top_product = max(product_sales.items(), key=lambda x: x[1])

generate_pdf_report(sales, total_revenue, top_product, product_sales)
