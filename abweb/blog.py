from flask import Flask,render_template,flash,redirect,url_for,request
from flask_mysqldb import MySQL
from wtforms import Form,StringField,validators


#Mail girdisi

class MailsForm(Form):
    email = StringField("Mail Adresi",validators=[validators.Email(message = "Lütfen geçerli bir email adresi girin...")])

app = Flask(__name__)
app.secret_key = "akboge"

app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "akboge"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/references")
def references():
    return render_template("references.html")

@app.route("/send",methods = ["GET","POST"])
def send():
    form = MailsForm(request.form)

    if request.method == "POST" and form.validate():
        email = form.email.data
        cursor = mysql.connection.cursor()

        sorgu = "INSERT into mails(mails) VALUES(%s)"

        cursor.execute(sorgu,(email,))
        mysql.connection.commit()

        cursor.close()
        flash("Mail başarıyla gönderildi...","success")
        return redirect(url_for("index"))
    else :
        return render_template("send.html",form = form)


if __name__=="__main__":
    app.run(host="0.0.0.0", port=8000)





