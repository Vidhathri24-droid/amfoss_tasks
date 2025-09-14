#  CineScope – Movie Database Visualizer (Solution)

CineScope is a desktop application that integrates **MySQL**, **PySide6**, and **Python** to create an interactive movie database dashboard. 
This solution demonstrates end-to-end functionality — from **data import** and **SQL integration** to **searching, filtering, exporting, and UI visualization**.

---

##  Features
- **Import CSV → MySQL**: Import movie records from `movies.csv` into a normalized MySQL table.
- **Dynamic Dashboard**: Powered by PySide6, the dashboard displays movies interactively.
- **Search & Filter**: Query movies by title, genre, year, etc.
- **Column Selection**: Choose which columns to display dynamically.
- **Export to CSV**: Save currently filtered/visualized results to a new `.csv` file.
- **Enhanced UI**: Redesigned for a cleaner and more intuitive movie browsing experience.

---

##  Setup Instructions

###  Clone Repository

```bash
git clone https://github.com/AadarshM07/CineScope-S3.git
cd CineScope-S3
````

###  Set Up Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

###  Install Requirements

```bash
pip install -r requirements.txt
```

###  Configure MySQL

* Ensure MySQL server is running.
* Create a new database:

```sql
CREATE DATABASE cinescope;
```

* Update **DB credentials** inside `import_csv.py` and `dashboard.py`.

###  Import Data into MySQL

```bash
python import_csv.py
```

###  Run the Application

```bash
python main.py
```

---

##  Technologies Used

* **Python 3.9+**
* **MySQL / PyMySQL (or mysql-connector-python)**
* **PySide6 (Qt for Python)**
* **Pandas** (for CSV handling)

---
```

