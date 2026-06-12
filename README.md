# intelligent-document-extraction-platform
Python-based Intelligent Document Extraction Platform using EasyOCR, Gemini AI, Flask, SQLite, OOP and Factory Design Pattern.

# Intelligent Document Extraction Platform

## Project Overview

An AI-powered document extraction system that automatically extracts structured information from document images using OCR and Google Gemini AI.

---

## Problem Statement

Manually reading and entering information from documents is time-consuming and error-prone. This project automates the extraction process and converts document images into structured data.

---

## Key Features

* Upload document images
* Extract text using EasyOCR
* Extract important fields using Gemini AI
* Convert unstructured text into JSON format
* Store extracted data in SQLite database
* Display extracted information through a web interface
* Support multiple document types

---

## Supported Documents

* Aadhaar Card
* Passport
* Driving License
* Invoice
* Resume

---

## Technologies Used

### Backend

* Python
* Flask

### OCR

* EasyOCR

### AI / LLM

* Google Gemini API

### Database

* SQLite

### Frontend

* HTML
* CSS

### Design Principles

* Object-Oriented Programming (OOP)
* Factory Design Pattern
* Modular Architecture

---

## Project Workflow

1. User uploads a document image.
2. EasyOCR extracts text from the image.
3. Gemini AI identifies important fields.
4. Extracted information is converted into JSON.
5. Data is stored in SQLite database.
6. Results are displayed on the web page.

---

## Folder Structure

* `models/` → Document classes
* `factory/` → Factory Pattern implementation
* `processors/` → OCR and Gemini processing
* `database/` → Database operations
* `templates/` → HTML pages
* `app.py` → Flask application

---

## Sample Output

```json
{
  "name": "SAMARTH SHARMA",
  "aadhaar_number": "1234 5678 9012",
  "gender": "Male",
  "dob": "20-06-1986"
}
```

---

## Skills Demonstrated

* Python Development
* Object-Oriented Programming
* Design Patterns
* OCR Integration
* AI/LLM Integration
* Database Management
* Flask Web Development
* JSON Processing

---

## Future Enhancements

* PostgreSQL Integration
* PDF Support
* Document Classification
* User Authentication
* Export to Excel/PDF
* Cloud Deployment

---

