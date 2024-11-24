from PyQt6.QtWidgets import QApplication, QGridLayout, QVBoxLayout, QWidget, QLabel, QLineEdit, \
    QPushButton, QMainWindow, QTableWidget, QTableWidgetItem, QDialog, QComboBox, QToolBar, \
    QStatusBar, QMessageBox, QTextEdit, QListWidget
from PyQt6.QtGui import QAction, QIcon, QDesktopServices, QTextCursor
from PyQt6.QtCore import QUrl, QEvent
import sys, requests
import news_sources

class Main_Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Search results")
        self.setMinimumSize(800, 400)

        self.results_area = QTextEdit(self)
        self.results_area.setGeometry(10, 10, 480, 320)
        self.results_area.setReadOnly(True)
        self.results_area.viewport().installEventFilter(self)

        # Options to change results
        # Topic
        self.topic_chooser = QLineEdit(self)
        self.topic_chooser.setPlaceholderText("Topic")
        self.topic_chooser.setGeometry(500, 10, 200, 50)
        # From date
        self.fromdate_chooser = QLineEdit(self)
        self.fromdate_chooser.setPlaceholderText("From Date (yyyy-mm-dd)")
        self.fromdate_chooser.setGeometry(500, 70, 200, 50)
        # To date
        self.todate_chooser = QLineEdit(self)
        self.todate_chooser.setPlaceholderText("To Date (yyyy-mm-dd)")
        self.todate_chooser.setGeometry(500, 130, 200, 50)

        # Source chooser
        self.list_widget = QListWidget(self)
        self.list_widget.setSelectionMode(QListWidget.SelectionMode.MultiSelection)
        self.list_widget.setGeometry(500, 190, 200, 50)

        items = ["all"] + news_sources.general_source_ids + news_sources.business_source_ids + news_sources.tech_source_ids + \
                news_sources.science_source_ids
        self.list_widget.addItems(items)


        # Submit button
        self.submit_button = QPushButton("Submit", self)
        self.submit_button.setGeometry(500, 250, 80, 35)
        self.result = self.submit_button.clicked.connect(self.search_result2)


        self.show()


    def search_result2(self):
        # selected_items = [item.text() for item in self.list_widget.selectedItems()]
        selected_items = ""
        for item in self.list_widget.selectedItems():
            item = item.text()
            selected_items = selected_items + "," + item
        # print(selected_items)

        topic = self.topic_chooser.text()
        from_date = self.fromdate_chooser.text()
        to_date = self.todate_chooser.text()
        API_KEY = "###"

        if "all" in selected_items:
            request = requests.get(
                f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&searchIn=content&sortBy=popularity&language=en&apiKey={API_KEY}")
        else:
            request = requests.get(f"https://newsapi.org/v2/everything?q={topic}&from={from_date}&to={to_date}&sources={selected_items}searchIn=content&sortBy=popularity&language=en&apiKey={API_KEY}")

        response = request.json()
        required_articles = response["articles"][:20]
        articles_string2 = f""
        for article_dict in required_articles:
            articles_string2 = articles_string2 + f"<b>Title:</b> {article_dict["title"]}<br>" \
                                                  f"<b>Description:</b> {article_dict["description"]}<br>" \
                                                  f"<b>URL:</b> <a href='{article_dict["url"]}'>{article_dict["url"]}</a><br><br>"

        # print(articles_string2)
        self.results_area.setHtml(articles_string2)


    def eventFilter(self, obj, event):

        # Checks if event (e.g. mouse scroll, mouse click etc.) is a mouse click and stores that as the cursor.
        if obj == self.results_area.viewport() and event.type() == QEvent.Type.MouseButtonPress:
            cursor = self.results_area.cursorForPosition(event.pos())
            anchor = cursor.block().text()

            # If the cursor is on top of a link, then open the link.
            if cursor.charFormat().isAnchor():
                url = cursor.charFormat().anchorHref()
                QDesktopServices.openUrl(QUrl(url))
                # print("True")
                return False

        else:
            return super().eventFilter(obj, event)


app = QApplication(sys.argv)
window = Main_Window()
sys.exit(app.exec())

