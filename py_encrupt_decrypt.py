#!/usr/bin/python
from PyPDF2 import PdfFileWriter, PdfFileReader
import pyfiglet


class Encrypt(object):
	"""docstring for Encrypt"""
	def __init__(self):
		self.Banner("PDF Protecter")
		self.main()

	


	def Banner(self,name):
		banner = pyfiglet.figlet_format(name, font = "bulbhead" )
		print(banner)

	def option(self,option):
		print("Available options")
		for x in range(len(option)):
			print(f"{x} . {option[x]}")

		try:
			o = int(input("Choose any one option: "))
			return o
		except:
			print("Enter 0 for Encrypt, 1 for Decrypt")
		

	def selection(self,choice):

		if self.choice == 0:
			print(self.choice)
			input_pdf = input("Enter the PDF name which you want to encrypt: ")
			output_pdf = input("Enter the file name which you want to save as output: ")
			password = input("Enter the Strong password: ")
			self.encruption(input_pdf,output_pdf,password)
			


		elif self.choice == 1:
			input_pdf = input("Enter the PDF name which you want to decrypt: ")
			output_pdf = input("Enter the file name which you want to save as output: ")
			password = input("Enter the password to Decrypt: ")
			self.decruption(input_pdf,output_pdf,password)
			

		

	def encruption(self,input_pdf,output_pdf,password):
		pdf_writer = PdfFileWriter()
		pdf_reader = PdfFileReader(input_pdf)
		num_pages = pdf_reader.getNumPages()
		for page in range(num_pages):
			pdf = pdf_reader.getPage(page)
			pdf_writer.addPage(pdf)

		pdf_writer.encrypt(password)

		with open(output_pdf,'wb') as f:
			pdf_writer.write(f)
		print("File encrypted Successfully")

	def decruption(self,input_pdf,output_pdf ,password):
		pdf_writer = PdfFileWriter()
		pdf_reader = PdfFileReader(input_pdf)

		if pdf_reader.isEncrypted:
			pdf_reader.decrypt(password)

			for o in range(pdf_reader.numPages):
				page = pdf_reader.getPage(o)
				pdf_writer.addPage(page)

			with open(output_pdf, "wb") as f:
				pdf_writer.write(f)

			print("File decrypted Successfully.")

		else:
			print("File already decrypted.") 


	def main(self):
		self.options = ["Encrypt","Decrypt"]
		self.choice = self.option(self.options)
		self.selection(self.choice)




encrypt = Encrypt()



		
		
