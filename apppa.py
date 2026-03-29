from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html>
<head>
<title>AASHTO</title>
<style>
body{background:#0b1220;color:white;font-family:Arial;text-align:center}
input{padding:5px;margin:5px}
button{padding:10px}
</style>
</head>

<body>

<h2>AASHTO 1993 Pavement</h2>

a1 <input id="a1" value="0.40"><br>
m1 <input id="m1" value="1.1"><br>
d1(cm) <input id="d1" value="20"><br>

<button onclick="calc()">Calculate</button>

<h3 id="result"></h3>

<script>
function calc(){
let a1=parseFloat(document.getElementById('a1').value)
let m1=parseFloat(document.getElementById('m1').value)
let d1=parseFloat(document.getElementById('d1').value)/2.54

let SN=a1*m1*d1

document.getElementById('result').innerHTML="SN = "+SN.toFixed(3)
}
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run()
