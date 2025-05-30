from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from PIL import Image

#Coordinate (0,0) is bottom left. Every coordinate points to the bottom left.

filename = "請求書.pdf"
title = "請求書"

quantities = []
descriptions = []
totals = []

#Given data coordinates
y_offset = 30
y_offset_2 = 20
y_offset_3 = 5
x_offset_1 = 5
x_offset_2 = 150
table_coords = [72,590]
full_name_coords = [152,650]
date_coords = [452,650]
invoice_coords = [152,630]
due_date_coords = [452,630]
image_size = [240,80]

#Skeleton Coordinates
invoice_front_coords = [249,710]
billed_to_coords = [72,650]
issue_date_coords = [372,650]
invoice_coords_skel = [72,630]
due_date_coords_skel = [372,630]
image_coords = [177,735]

def createTable(n,descs,quants,tots,currency,tax):
	c.rect(table_coords[0],table_coords[1]-y_offset*(n+1),x_offset_2*3,y_offset*(n+1))
	for i in range(0,n):
		c.line(table_coords[0],table_coords[1]-(i+1)*y_offset,table_coords[0]+3*x_offset_2,table_coords[1]-(i+1)*y_offset)
	for i in range(0,2):
		c.line(table_coords[0]+x_offset_2*(i+1),table_coords[1],table_coords[0]+x_offset_2*(i+1),table_coords[1]-(n+1)*y_offset)
	c.drawString(table_coords[0]+x_offset_1,table_coords[1]-y_offset_2,"Description")
	c.drawString(table_coords[0]+x_offset_1+x_offset_2,table_coords[1]-y_offset_2,"Quantity")
	c.drawString(table_coords[0]+x_offset_1+x_offset_2*2,table_coords[1]-y_offset_2,"Total " + currency)
	for i in range(0,n):
		c.drawString(table_coords[0]+x_offset_1,table_coords[1]-y_offset_3-y_offset*(i+3/2),descs[i])
		c.drawString(table_coords[0]+x_offset_1+x_offset_2,table_coords[1]-y_offset_3-y_offset*(i+3/2),quants[i])
		c.drawString(table_coords[0]+x_offset_1+x_offset_2*2,table_coords[1]-y_offset_3-y_offset*(i+3/2),tots[i])
	a = 0
	for i in totals:
		a += int(i)
	c.drawString(table_coords[0]+x_offset_1+x_offset_2*2,table_coords[1]-y_offset_3-y_offset*(n+3/2),str(a))
	c.line(table_coords[0]+x_offset_2*2,table_coords[1]-(n+2)*y_offset,table_coords[0]+x_offset_2*3,table_coords[1]-(n+2)*y_offset)
	c.drawString(table_coords[0]+x_offset_1+x_offset_2*2,table_coords[1]-y_offset_3-y_offset*(n+5/2),str(tax)+"%")
	c.line(table_coords[0]+x_offset_2*2,table_coords[1]-(n+3)*y_offset,table_coords[0]+x_offset_2*3,table_coords[1]-(n+3)*y_offset)
	c.drawString(table_coords[0]+x_offset_1+x_offset_2*2,table_coords[1]-y_offset_3-y_offset*(n+7/2),str(a*(1+tax/100)))	
	c.line(table_coords[0]+x_offset_2*2,table_coords[1]-(n+4)*y_offset,table_coords[0]+x_offset_2*3,table_coords[1]-(n+4)*y_offset)
	c.drawString(table_coords[0]+x_offset_1+x_offset_2,table_coords[1]-y_offset_3-y_offset*(n+3/2),"Sum Total")
	c.drawString(table_coords[0]+x_offset_1+x_offset_2,table_coords[1]-y_offset_3-y_offset*(n+5/2),"Tax (%)")
	c.drawString(table_coords[0]+x_offset_1+x_offset_2,table_coords[1]-y_offset_3-y_offset*(n+7/2),"Sum Total with tax")	
	c.drawString(table_coords[0],table_coords[1]-y_offset_3-y_offset*(n+12/2),"Payment Instructions (TBC):")
	c.drawString(table_coords[0],table_coords[1]-y_offset_3-y_offset*(n+12/2)-y_offset_2,"JSC TBC Bank")
	c.drawString(table_coords[0],table_coords[1]-y_offset_3-y_offset*(n+12/2)-y_offset_2*2,"TBCBGE22")
	c.drawString(table_coords[0],table_coords[1]-y_offset_3-y_offset*(n+12/2)-y_offset_2*3,"GE41TB7002536170100002 (USD)")
	c.drawString(table_coords[0],table_coords[1]-y_offset_3-y_offset*(n+12/2)-y_offset_2*4,"Prime Management LLC")
	c.drawString(table_coords[0]+x_offset_2*2,table_coords[1]-y_offset_3-y_offset*(n+12/2),"Payment Instructions (BOG):")
	c.drawString(table_coords[0]+x_offset_2*2,table_coords[1]-y_offset_3-y_offset*(n+12/2)-y_offset_2,"JSC Bank of Georgia")
	c.drawString(table_coords[0]+x_offset_2*2,table_coords[1]-y_offset_3-y_offset*(n+12/2)-y_offset_2*2,"BAGAGE22")
	c.drawString(table_coords[0]+x_offset_2*2,table_coords[1]-y_offset_3-y_offset*(n+12/2)-y_offset_2*3,"GE93BG0000000607816171")
	c.drawString(table_coords[0]+x_offset_2*2,table_coords[1]-y_offset_3-y_offset*(n+12/2)-y_offset_2*4,"Prime Management LLC")
	c.drawString(table_coords[0],table_coords[1]-y_offset_3-y_offset*(n+16/2)-y_offset_2*4,"Company address:")
	c.drawString(table_coords[0],table_coords[1]-y_offset_3-y_offset*(n+16/2)-y_offset_2*5,"Georgia, Tbilisi, Krtsanisi district, Rustavi highway,")
	c.drawString(table_coords[0],table_coords[1]-y_offset_3-y_offset*(n+16/2)-y_offset_2*6,"N19, building N3, floor N1, storeroom")
	c.drawString(table_coords[0],table_coords[1]-y_offset_3-y_offset*(n+16/2)-y_offset_2*7,"Company postal code: 0114")
def askForData():
	surname = input("Surname: ")
	name = input("Name: ")
	s = input("1 for Mr., 2 for Ms.: ")
	date = input("Date (dd/mm/yyyy): ")
	invoice_number = input("Invoice Number: ")
	due_date_sel = input("Due date (dd/mm/yyyy): ")
	currency_selection = input("1 For USD, 2 for GEL: ")
	tax_rate = int(input("Tax rate (%): "))
	number_of_descriptions = int(input("Number of Descriptions: "))
	match currency_selection:
		case "1":
			currency_selection = "(USD)"
			filename = "請求書(USD)"
		case "2":
			currency_selection = "(GEL)"
		
	for i in range(0,number_of_descriptions):
		a = input(f"Description {i+1}: ")
		descriptions.append(a)
		q = input(f"Quantity {i+1}: ")
		quantities.append(q)
		t = input(f"Total {i+1}: ")
		totals.append(t)
	full_name = ""
	match s:
		case "1":
			full_name = "Mr. " + surname + " " + name
		case "2":
			full_name = "Ms. " + surname + " " + name
	c.drawString(full_name_coords[0],full_name_coords[1],full_name)
	c.drawString(date_coords[0],date_coords[1],date)
	createTable(number_of_descriptions,descriptions,quantities,totals,currency_selection,tax_rate)											
	c.drawString(invoice_coords[0],invoice_coords[1],createInvoiceID(deslashify(date),createSurnameShortform(surname),invoice_number))
	c.drawString(due_date_coords[0],due_date_coords[1],due_date_sel)
	
def createSurnameShortform(surn):
	vowels = {'a','e','i','o','u'}
	res = str()
	for i in surn:
		if((i not in vowels) and (i.lower() not in vowels) ):
			res += i
			if(len(res) >= 2):
				break
	return res.upper()
			
def deslashify(date):
	res = str()
	for i in date:
		if (i != '/'):
			res += i
	return res
		
def createInvoiceID(date,ss,num):
	return date+ss+num
	 
def createSkeleton():
	billed_to = "Billed To:"
	issue_date = "Issue date:"
	invoice_id = "Invoice ID:"
	due_date = "Due date:"
	invoice_front = "I N V O I C E"
	c.drawString(billed_to_coords[0],billed_to_coords[1], billed_to)
	c.drawString(issue_date_coords[0],issue_date_coords[1],issue_date)
	c.drawString(invoice_coords_skel[0],invoice_coords_skel[1],invoice_id)
	c.drawString(due_date_coords_skel[0],due_date_coords_skel[1],due_date)
	c.drawImage("logo.png",image_coords[0],image_coords[1],image_size[0],image_size[1])
	c.setFont("Times-Roman",20)
	c.drawString(invoice_front_coords[0],invoice_front_coords[1],invoice_front)

c = canvas.Canvas(filename)
askForData()
createSkeleton()
c.save()
