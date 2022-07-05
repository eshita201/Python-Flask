from flask import Flask
import os
import io
import random
from flask import Flask, Response, request
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.backends.backend_svg import FigureCanvasSVG
import numpy as np
import pandas as pd
from matplotlib.figure import Figure
app = Flask(__name__)

@app.route("/")
def hello():
  return """<h2>random points as png</h2>
        <h2><img src="/namegender.png"
         alt="random points as png"
         height="200"> <h2>
        
        <h2>random points as svg<h2><h2><img src="/nameage.svg"
         alt="random points as svg"
         height="200"> <h2>
         """

@app.route("/namegender.png")
def namegender():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    df = pd.read_csv("D:\Learning\PythonProject\ETL - Flask\Files\Sample.csv")
    df.rename(columns={'A':'Position1'},inplace=True)
    df.rename(columns={'C':'Position2'},inplace=True)
    df.rename(columns={'D':'Position3'},inplace=True)
    df.index.names =['SNo']
    df.index+=1
    df.to_csv("D:\Learning\PythonProject\ETL - Flask\Files\SampleFile.csv")
    Name_array=np.array(df['Name'])
    Gender_array=np.array(df['Gender'])
    Age_array=np.array(df['Age'])
    axis.plot(Name_array, Gender_array)
    output = io.BytesIO()
    FigureCanvasAgg(fig).print_png(output)
    return Response(output.getvalue(), mimetype="image/png")

@app.route("/nameage.svg")
def nameage():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    df = pd.read_csv("D:\Learning\PythonProject\ETL - Flask\Files\Sample.csv")
    df.rename(columns={'A':'Position1'},inplace=True)
    df.rename(columns={'C':'Position2'},inplace=True)
    df.rename(columns={'D':'Position3'},inplace=True)
    df.index.names =['SNo']
    df.index+=1
    df.to_csv("D:\Learning\PythonProject\ETL - Flask\Files\SampleFile.csv")
    Name_array=np.array(df['Name'])
    Gender_array=np.array(df['Gender'])
    Age_array=np.array(df['Age'])
    axis.plot(Name_array, Age_array)
    output = io.BytesIO()
    FigureCanvasSVG(fig).print_svg(output)
    return Response(output.getvalue(), mimetype="image/svg+xml")


#os.system('taskkill /F /IM chrome.exe')
if __name__ == "__main__":
    #import webbrowser
#
    #webbrowser.open("http://127.0.0.1:5000/")
    #app.run(debug=True)
  app.run(host="localhost", port=8000, debug=True)