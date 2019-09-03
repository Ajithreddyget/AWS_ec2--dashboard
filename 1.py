import base64
from io import BytesIO

from flask import Flask
from matplotlib.figure import Figure
region=['eu-north-1','ap-south-1','eu-west-3','eu-west-2','eu-west-1','ap-northeast-2','ap-northeast-1','sa-east-1','ca-central-1','ap-east-1','ap-southeast-1','ap-southeast-2','eu-central-1','us-east-1','us-east-2','us-west-2','us-west-1']
ec2count=[0, 9, 0, 3, 23, 0, 0, 0, 0, 0, 4, 9, 0, 62, 32, 278, 12]
app = Flask(__name__)

@app.route("/")
def hello():
   #Generate the figure **without using pyplot**.
   fig = Figure()
   ax = fig.subplots(figsize=(13, 10), subplot_kw=dict(aspect="equal"))
   ax.plot(ec2count, labels=region,
   autopct='%1.1f%%', shadow=False, startangles=140)
   #ax.plt.axis('equal')
   # Save it to a temporary buffer.
   buf = BytesIO()
   fig.savefig(buf, format="png")
   # Embed the result in the html output.
   data = base64.b64encode(buf.getbuffer()).decode("ascii")
   print(data)
   return "<img src='data:image/png;base64,{}'/>".format(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3000, debug=True)