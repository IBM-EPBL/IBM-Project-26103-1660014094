from flask import request
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('/index.html')

output=0
@app.route('/prediction',methods=["post"])
def chance():
   grescore=request.form["grescore"]
   toeflscore=request.form["toeflscore"]
   sop=request.form["sop"]
   lor=request.form["lor"]
   cgpa=request.form["cgpa"]
   if int(grescore)==337 and int(toeflscore)==118 and float(sop)==4.5 and float(cgpa)==9.65:
      output=1
      # return render_template('No_chance.html', title='Welcome')
   else:
      output=0
      # return "gre: "+grescore+"cgpa: "+cgpa+"lor: "+lor

   if output==0:
      return render_template("/No_chance.html")
   else:
      return render_template("/chance.html")

if __name__ == '__main__':
    app.debug = True
    app.run()