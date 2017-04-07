from flask import *
import pymysql as pm
app = Flask(__name__)

@app.route('/')
def quiz():
    #return render_template('1.html')
    return """
    
    <html>
<body>  
<style>
form {
  /* Just to center the form on the page */
  margin: 0 auto;
  width: 400px;
  /* To see the outline of the form */
  padding: 1em;
  border: 1px solid #CCC;
  border-radius: 1em;
}

form div + div {
  margin-top: 1em;
}

label {
  /* To make sure that all labels have the same size and are properly aligned */
  display: inline-block;
  width: 90px;
  text-align: right;
}

input, textarea {
  /* To make sure that all text fields have the same font settings
     By default, textareas have a monospace font */
  font: 1em sans-serif;

  /* To give the same size to all text fields */
  width: 300px;
  box-sizing: border-box;

  /* To harmonize the look & feel of text field border */
  border: 1px solid #999;
}

input:focus, textarea:focus {
  /* To give a little highlight on active elements */
  border-color: #000;
}

textarea {
  /* To properly align multiline text fields with their labels */
  vertical-align: top;

  /* To give enough room to type some text */
  height: 5em;
}

.button {
  /* To position the buttons to the same position of the text fields */
  padding-left: 90px; /* same size as the label elements */
}

button {
  /* This extra margin represent roughly the same space as the space
     between the labels and their text fields */
  margin-left: .5em;
}
</style>


<form action='/quiz_answers' method="POST">
    <div>
    <label for="name">Name:</label>
    <input type="text" id="name" name="user_name" />
  <div>
  <div>
    <label for="mail">E-mail:</label>
    <input type="email" id="mail" name="user_email" />
  </div>
  <div>
    <label for="msg">Message:</label>
    <textarea id="msg" name="user_message"></textarea>
     <input  type="submit" value="Submit!" />
  </div>
  
   
  
</div>
</div>
</form>
</body>
</html>
    """

@app.route('/quiz_answers', methods=['POST'])
def quiz_answers():

    q1 = request.form['user_name']
    q2 = request.form['user_email']
    q4 = request.form['user_message']
    #q5 = request.form['q5']
    #return (q1,q2,q4,q5)
    db = pm.connect("localhost","root","","temp")
    cur = db.cursor()
    cur.execute("select * from logtab")

    res = cur.fetchall()

    return "hello world"+str(q1)+str(q2)+str(q4)+"     data  "+str(res[150])+"      data"


if __name__ == "__main__":
    app.run()