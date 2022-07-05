from distutils.core import setup # Need this to handle modules
import py2exe 
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

setup(windows=['D:\Learning\PythonProject\ETL - Flask\Task.py']) 