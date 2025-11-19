import email

from flask import Flask, request, render_template, session
import pandas as pd
import PyPDF2
import io

app = Flask(__name__, template_folder="templates")
app.secret_key = '1234567890'


# @app.route("/")
# def home():
#     new_value= "THIS IS AHSAM'S CODING JOURNEY"
#
#     return render_template("index.html")

# @app.route("/about")
# def about():
#     return render_template("other.html")
# #
# @app.route("/redirect")
# def redirect():
#     return render_template("redirect.html")

# @app.route("/about", methods=["GET", "POST"])
# def about():
#
#     if request.method == "GET":
#         return "GET METHOD CALLED\n"
#     elif request.method == "POST":
#         return "POST METHOD CALLED\n"
#     else:
#         return 'About Us'
#
# @app.route('/contact/<rabta>')
# def contact(rabta):
#     return f"<h1>Contact Us at {rabta} </h1>"
#
# # @app.route('/sum/<int:num1>/<int:num2>')
# # route parameters
# @app.route('/sum/<num1>/<num2>')
# def rabta(num1,num2):
#     num1 = int(num1)
#     num2 = int(num2)
#     return f"Sum of {num1} and {num2} = {num1+num2}"
#
# @app.route('/url_params')
# def url_params():
#     name = request.args.get('name')
#     age = request.args.get('age')
#     if name and age:
#         return f"<h1>{name} is {age}</h1>"
#     elif name:
#         return f"<h1>NAME is {name}</h1>"
#     elif age:
#         return f"<h1>AGE {age}</h1>"
#     else:
#         return f"<h1>NAME and AGE are required</h1>"
#
#
#
# @app.route("/login", methods=["GET", "POST"])
# def login():
#
#     if request.method == "GET":
#         return render_template("login.html")
#     elif request.method == "POST":
#         username = request.form.get("username")
#         password = request.form.get("password")
#
#         if username == 'admin' and password:
#             return render_template("index.html")
#         else:
#             return render_template("failure.html")

# @app.route("/upload", methods=["POST"])
# def upload():
#     if request.method == "POST":
#         file = request.files["file"]
#
#         if file.content_type == "application/pdf":
#             return file.read().decode()
#         elif file.content_type == "xls,doc,docs,xlsx":
#             df = pd.read_excel(file)
#             return pd.to_html()


# @app.route("/upload", methods=["POST"])
# def upload():
#     if 'file' not in request.files:
#         return "<h2>No file selected</h2>"
#
#     file = request.files['file']
#
#     if file.filename == '':
#         return "<h2>No file selected</h2>"
#
#     try:
#         # PDF Files
#         if file.content_type == "application/pdf":
#             # Read PDF and extract text
#             pdf_reader = PyPDF2.PdfReader(file)
#             text_content = ""
#             for page_num in range(len(pdf_reader.pages)):
#                 page = pdf_reader.pages[page_num]
#                 text_content += page.extract_text() + "\n\n--- Page {} ---\n\n".format(page_num + 1)
#
#             return f"""
#             <h2>📄 PDF File Content</h2>
#             <p><strong>File Name:</strong> {file.filename}</p>
#             <p><strong>Total Pages:</strong> {len(pdf_reader.pages)}</p>
#             <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; max-height: 500px; overflow-y: auto;'>
#                 <pre>{text_content if text_content.strip() else 'No extractable text found in PDF'}</pre>
#             </div>
#             """
#
#         # Excel Files
#         elif file.content_type in ["application/vnd.ms-excel",
#                                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]:
#             df = pd.read_excel(file)
#             return f"""
#             <h2>📊 Excel File Content</h2>
#             <p><strong>File Name:</strong> {file.filename}</p>
#             <p><strong>Shape:</strong> {df.shape[0]} rows x {df.shape[1]} columns</p>
#             <div style='overflow-x: auto;'>
#                 {df.to_html(classes='table table-striped', index=False)}
#             </div>
#             """
#
#         # Text Files
#         elif file.content_type == "text/plain":
#             content = file.read().decode('utf-8')
#             return f"""
#             <h2>📝 Text File Content</h2>
#             <p><strong>File Name:</strong> {file.filename}</p>
#             <p><strong>Content Length:</strong> {len(content)} characters</p>
#             <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; max-height: 500px; overflow-y: auto;'>
#                 <pre>{content}</pre>
#             </div>
#             """
#
#         # Word Documents (basic support)
#         elif file.content_type in ["application/msword",
#                                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
#             try:
#                 from docx import Document
#                 doc = Document(file)
#                 text_content = ""
#                 for paragraph in doc.paragraphs:
#                     text_content += paragraph.text + "\n"
#
#                 return f"""
#                 <h2>📄 Word Document Content</h2>
#                 <p><strong>File Name:</strong> {file.filename}</p>
#                 <div style='background: #f8f9fa; padding: 20px; border-radius: 10px; max-height: 500px; overflow-y: auto;'>
#                     <pre>{text_content if text_content.strip() else 'No text content found'}</pre>
#                 </div>
#                 """
#             except ImportError:
#                 return "<h2>Word document support requires python-docx library</h2><p>Install with: pip install python-docx</p>"
#
#         else:
#             return f"<h2>Unsupported file type:</h2> <p>{file.content_type}</p>"
#
#     except Exception as e:
#         return f"<h2>Error processing file:</h2> <p>{str(e)}</p>"# if app.name == "__main__":

@app.route("/set_session_data")
def set_session_data():
    session['name'] = 'AHSAM YOUSAF'
    session['email'] = "ahsamyousaf01@gmail.com"
    return render_template("session.html", message="SESSION SET")

@app.route("/get_session_data")
def get_session_data():
    if 'name' in session and 'email' in session:
        name = session['name']
        email = session['email']
        return render_template("session.html", message=f'Name: {name}, Email: {email}')
    else:
        return render_template("session.html", message="SESSION NOT FOUND")

@app.route("/clear")
def clear():
    session.clear()
    return render_template("session.html", message="Session cleared!")  # ✅ FIXED

if __name__ == "__main__":
    app.run(debug=True)