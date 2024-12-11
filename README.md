# DAB111 Group 9 Project : Retail Data Insights

## Project Overview
This project demonstrates the process of collecting data, storing it in a SQLite database, and presenting it through a Flask-based website. The project aims to showcase practical skills in Python, database management, and web development.

---

## Features
1. **Data Collection**
   - Data with at least 5 variables and 2 or more data types collected from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail).
   - Preprocessed and stored in CSV format for further use.

2. **Database**
   - Data stored in a SQLite database using Python's `sqlite3` module.
   - Database contains a single table with columns matching the dataset's variables.

3. **Website**
   - Developed using Flask.
   - Contains two main pages:
     - **About Page**: Describes the dataset, its source, and variable definitions.
     - **Data Page**: Displays the dataset (or a sample thereof).

---

## Project Structure
The project is organized into the following directory structure:

```
main folder
├── database
│   ├── create_db.py       # Code for database creation and data insertion
│   └── data.db            # SQLite database file
├── website
│   ├── app.py             # Flask application
│   ├── app.ipynb             # Flask application
│   ├── templates
│   │   ├── Home.html      # Home HTML template
│   │   ├── about.html     # About page template
│   │   └── data.html      # Data page template
│   │   └── details.html   # Group page template
├── Readme.md              # Project description
├── requirements.txt       # List of required Python packages
└── data                   # Optional folder for raw or processed data files
```

---

## How to Run the Project

### Step 1: Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/faridcharania1987/DAB111_Project_Group_9
cd <repository_folder>
```

### Step 2: Install Required Packages
Install the necessary Python packages using `requirements.txt`:
```bash
pip install -r requirements.txt
```

### Step 3: Set Up the Database
Navigate to the `database` folder and run the `create_db.py` script to create the SQLite database and insert data:
```bash
python database/create_db.py
```

### Step 4: Run the Flask Application
Navigate to the `website` folder and run the Flask application:
```bash
python website/app.py
```

### Step 5: Open the Website
Once the Flask application is running, open your browser and go to:
```
http://127.0.0.1:5000/
```

---

## Dataset Information
**Source**: [Online Retail Dataset - UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online+retail)  
**Variables**:
- `InvoiceNo`: Invoice number for the transaction
- `StockCode`: Product (item) code
- `Description`: Product description
- `Quantity`: Quantity of each product (item) per transaction
- `InvoiceDate`: Invoice date and time
- `UnitPrice`: Unit price of the product
- `CustomerID`: Customer number
- `Country`: Country of the customer

---

## Contact
For any questions or issues, please contact the group members

