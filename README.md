spot_ec2_ocr
============

Amazon Spot EC2 OCR Example

What is it?

Python Boto based example to create a Amazon EC2 spot instance backed OCR system in the cloud.

What does it show?

Shows object-oriented programming.
Shows an understanding of the Boto library.
The Amazon Machine Image (AMI) ami-f26d18c2 shows how to configure a RedHat 6.4 x86_64 system in EC2.
The AMI contains Tesseract (OCR), pdftk (split PDF pages), ImageMagick (convert), ExactCode (hocr2pdf) and
Python with Fabric/Paramiko and PostgreSQL.

Shortcomings?

It's not a complete project.  It processes images and makes PDF pages with the search working.

What does it need?

Written in Python 2.6.6.  It needs the Amazon Boto library (PIP).
