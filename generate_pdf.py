from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Python Learning Documentation', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1)
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_learning_topic(self, title, content):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(content)


def create_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(0, 10, 'Welcome to Python Learning', 0, 1, 'C')
    pdf.ln(10)

    # Add learning topics
    topics = {
        'Introduction to Python': 'Content about Python basics.'
        'Data Structures': 'Details about lists, tuples, dictionaries, sets.'
        'Control Flow': 'Information on if statements, loops, and comprehensions.'
        'Functions and Modules': 'Info on defining functions and using modules.'
        'Object-Oriented Programming': 'Overview of classes and objects.'
        'File Handling': 'How to read and write files in Python.'
    }

    for title, content in topics.items():
        pdf.add_learning_topic(title, content)

    pdf.output('Python_Learning_Documentation.pdf')

if __name__ == '__main__':
    create_pdf()