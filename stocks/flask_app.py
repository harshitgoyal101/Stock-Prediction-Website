from flask import Flask, render_template, request,send_file
from io import BytesIO
import base64
from datetime import datetime
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
import datetime
import time

fig,ax = plt.subplots(figsize=(8,16))
ax = sns.set_style(style="darkgrid")

import pickle
import matplotlib.pyplot as plt



app = Flask(__name__)


stocks = ["BSESN","INFY","NSEI","RELIANCE","SBI","TATASTEEL","TCS","TTM"]

@app.route('/', methods=['GET', 'POST'])
def index():
    text = "null"
    sdate = ""
    index=-1;
    for i in range(len(stocks)):
        if stocks[i]==text:
            index=i+1;
    if request.method == 'POST':
        text = request.form['text']
    if text in stocks:
        stock = text
        valid = pickle.load(open("results/"+stock+".pickle","rb"))
        

        x = list(range(len(valid['train'])))
        x2 = list(range(120))
        x2 = [x+len(valid['train'])-1 for x in x2]
        

        date1 = []

        start_date = datetime.datetime.strptime(valid['TDate'][0][0], '%Y-%m-%d')+ relativedelta(months=+8)
     
        for i in range(len(valid['train'])):
            date1.append(start_date)
            start_date += datetime.timedelta(days=1)

        date2 = []
        for i in range(180):
            date2.append(start_date)
            start_date += datetime.timedelta(days=1)


        fig = Figure(figsize=(9.49,5.55))
        
        ax = fig.subplots()
        ax.set_title(stock)

        ax.set_xlabel('Date',fontsize=18)
        ax.set_ylabel('Price',fontsize=18)
        
        ax.plot(date1,valid['train'])
        ax.plot(date2,valid['Prediction'])
            
        ax.legend([['Train'],['Prediction']],loc='lower right')
        buf = BytesIO()

        fig.savefig(buf, format="png")
        data = base64.b64encode(buf.getbuffer()).decode("ascii")
        return render_template("index.html",data=f"<img src='data:image/png;base64,{data}'/>",index=index,thing=text)
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':  
    app.run(debug=True)
