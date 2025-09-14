import sys
import csv
import mysql.connector
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QTableWidget, QTableWidgetItem, QGridLayout, 
    QTextEdit, QSizePolicy, QLineEdit, QFileDialog, QMessageBox
)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",        
        password="Vidha3@poluru",  
        database="cinescope"
    )

def fetch_movies(query="SELECT * FROM movies"):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    cursor.close()
    conn.close()
    return columns, rows


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CineScope – Dashboard")
        self.setMinimumSize(1200, 800)
        self.setStyleSheet("background-color: #121212; color: white; padding: 20px;")

        self.search_mode = None
        self.active_columns = set(["Series_Title", "Released_Year", "Genre", "IMDB_Rating", "Director", "Star1", "Star2", "Star3"])
        
        self.init_ui()
        self.load_all_movies()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        header = QLabel("🎬 CineScope Dashboard")
        header.setFont(QFont("Arial", 24, QFont.Bold))
        header.setAlignment(Qt.AlignCenter)
        header.setFixedHeight(80)
        main_layout.addWidget(header)

        split_layout = QHBoxLayout()

        left_container = QVBoxLayout()
        left_container.setSpacing(10)
        left_container.setAlignment(Qt.AlignTop)

        search_heading = QLabel("Search By")
        search_heading.setFont(QFont("Arial", 18, QFont.Bold))
        left_container.addWidget(search_heading)

        search_buttons = [
            ("Genre", "Genre"),
            ("Year", "Released_Year"),
            ("Rating", "IMDB_Rating"),
            ("Director", "Director"),
            ("Actor", "Star1")  
        ]

        search_grid = QGridLayout()
        for index, (label, mode) in enumerate(search_buttons):
            btn = QPushButton(label)
            btn.setStyleSheet(self.get_button_style(False))
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(lambda _, m=mode: self.set_search_mode(m))
            row, col = divmod(index, 2)
            search_grid.addWidget(btn, row, col)
        left_container.addLayout(search_grid)

        column_heading = QLabel("Select Columns")
        column_heading.setFont(QFont("Arial", 18, QFont.Bold))
        left_container.addWidget(column_heading)

        column_buttons = [
            ("Title", "Series_Title"),
            ("Year", "Released_Year"),
            ("Genre", "Genre"),
            ("Rating", "IMDB_Rating"),
            ("Director", "Director"),
            ("Stars", "Star1, Star2, Star3"),
        ]

        column_grid = QGridLayout()
        for index, (label, col) in enumerate(column_buttons):
            btn = QPushButton(label)
            btn.setStyleSheet(self.get_button_style(False))
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            btn.clicked.connect(lambda _, c=col: self.toggle_column(c))
            row, colpos = divmod(index, 2)
            column_grid.addWidget(btn, row, colpos)
        left_container.addLayout(column_grid)

        self.query_input = QLineEdit()
        self.query_input.setPlaceholderText("Enter search term")
        self.query_input.setStyleSheet("background-color: #1e1e1e; color: white; padding: 5px; border: 1px solid #444;")
        left_container.addWidget(self.query_input)

        action_layout = QHBoxLayout()
        search_btn = QPushButton("Search")
        search_btn.setStyleSheet("background-color: #e50914; color: white; padding: 6px; border-radius: 5px;")
        search_btn.clicked.connect(self.execute_search)
        action_layout.addWidget(search_btn)

        export_btn = QPushButton("Export CSV")
        export_btn.setStyleSheet("background-color: #1f1f1f; color: white; padding: 6px; border-radius: 5px;")
        export_btn.clicked.connect(self.export_csv)
        action_layout.addWidget(export_btn)
        left_container.addLayout(action_layout)

        right_side_layout = QVBoxLayout()
        right_side_layout.setSpacing(10)

        self.table = QTableWidget()
        self.table.setStyleSheet("""
            QTableWidget {
                color: white;
                font-family: Arial, sans-serif;
                font-size: 14px;
            }
            QHeaderView::section {
                background-color: white;
                color: black;
                padding: 4px;
            }
        """)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.output_console = QTextEdit()
        self.output_console.setPlaceholderText("Results will appear here...")
        self.output_console.setStyleSheet("""
            QTextEdit {
                background-color: #1e1e1e;
                color: white;
                border: 1px solid #444;
                padding: 5px;
            }
        """)
        self.output_console.setFixedHeight(100)

        right_side_layout.addWidget(self.table)
        right_side_layout.addWidget(self.output_console)

        split_layout.addLayout(left_container, 2)
        split_layout.addLayout(right_side_layout, 8)
        main_layout.addLayout(split_layout)
        self.setLayout(main_layout)


    def get_button_style(self, is_selected):
        if is_selected:
            return """
                QPushButton {
                    background-color: #ffcc00;
                    border: 1px solid #ff9900;
                    border-radius: 3px;
                    padding: 6px;
                }
            """
        else:
            return """
                QPushButton {
                    background-color: #1f1f1f;
                    border: 1px solid #333;
                    border-radius: 3px;
                    padding: 6px;
                }
                QPushButton:hover {
                    background-color: #333;
                }
            """

    def set_search_mode(self, mode):
        self.search_mode = mode
        self.output_console.append(f"Search mode set to: {mode}")

    def toggle_column(self, column):
        if "," in column:  
            cols = column.split(", ")
        else:
            cols = [column]

        for col in cols:
            if col in self.active_columns:
                self.active_columns.remove(col)
                self.output_console.append(f"Column hidden: {col}")
            else:
                self.active_columns.add(col)
                self.output_console.append(f"Column shown: {col}")

    def execute_search(self):
        keyword = self.query_input.text().strip()
        if not keyword:
            self.load_all_movies()
            return

        if self.search_mode is None:
            self.output_console.append(" Please select a search mode first")
            return

        if self.search_mode == "Star1":
            query = f"""
                SELECT * FROM movies 
                WHERE Star1 LIKE '%{keyword}%' 
                   OR Star2 LIKE '%{keyword}%'
                   OR Star3 LIKE '%{keyword}%'
            """
        else:
            query = f"SELECT * FROM movies WHERE {self.search_mode} LIKE '%{keyword}%'"

        columns, rows = fetch_movies(query)
        self.display_data(columns, rows)
        self.output_console.append(f"✅ Search completed: {len(rows)} results")

    def load_all_movies(self):
        columns, rows = fetch_movies("SELECT * FROM movies")
        self.display_data(columns, rows)
        self.output_console.append("📥 Loaded all movies")

    def display_data(self, columns, rows):
        filtered_cols = [c for c in columns if c in self.active_columns]
        col_indices = [columns.index(c) for c in filtered_cols]

        self.table.setRowCount(len(rows))
        self.table.setColumnCount(len(filtered_cols))
        self.table.setHorizontalHeaderLabels(filtered_cols)

        for r_idx, row in enumerate(rows):
            for c_idx, col_index in enumerate(col_indices):
                self.table.setItem(r_idx, c_idx, QTableWidgetItem(str(row[col_index])))

    def export_csv(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save CSV", "", "CSV Files (*.csv)")
        if path:
            try:
                with open(path, "w", newline="", encoding="utf-8") as file:
                    writer = csv.writer(file)
                    # Write headers
                    headers = [self.table.horizontalHeaderItem(i).text() for i in range(self.table.columnCount())]
                    writer.writerow(headers)
                    for row in range(self.table.rowCount()):
                        writer.writerow([self.table.item(row, col).text() if self.table.item(row, col) else "" 
                                         for col in range(self.table.columnCount())])
                QMessageBox.information(self, "Success", f"Data exported successfully to {path}")
                self.output_console.append(f"📤 Exported table to {path}")
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to export: {str(e)}")
                self.output_console.append(f"❌ Export failed: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dashboard = Dashboard()
    dashboard.show()
    sys.exit(app.exec())

