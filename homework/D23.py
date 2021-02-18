from bokeh.plotting import figure,output_file,show
from bokeh.models import widgets,ColumnDataSource,HoverTool
from bokeh.io import output_notebook
from bokeh.palettes import Spectral6
import numpy as np

import bokeh.sampledata
bokeh.sampledata.download()

fruits=['apple','pears','banana','orange','grapes','tomato']
counts=[5,3,4,2,4,6]
source=ColumnDataSource(data=dict(fruits=fruits,counts=counts,color=Spectral6))
p=figure(x_range=fruits,plot_height=250,y_range=(0,9),title='fruit counts')
p.vbar(x='fruits',top='counts',width=0.9,color='color',legend_field='fruits',source=source)
p.xgrid.grid_line_color=None
p.legend.orientation='horizontal'
p.legend.location='top_center'
show(p)

import bokeh.io
from bokeh.models import HoverTool
from bokeh.palettes import Spectral4
from bokeh.sampledata.stocks import AAPL, GOOG, IBM, MSFT
import pandas as pd
hover=HoverTool(tooltips=[('data','@data'),('close','@close'),('close','@open'),('high','@high'),('low','@low'),('volume','@volume')],formatters={"@date":"datetime"})
q=figure(plot_width=1000,plot_height=400,x_axis_type="datetime",tools=[hover,"pan,box_zoom,reset,save"])
q.title.text='Stock_Price--Click on legend entries to mute the corresponding lines and show daily details in hover'
for data,name,color in zip([AAPL,IBM,MSFT,GOOG],["AAPL","IBM","MSFT","GOOG"],Spectral4):
    df=pd.DataFrame(data)
    df['date']=pd.to_datetime(df['date'])
    source=ColumnDataSource(df)
    p.line(x="date",y="close",line_width=2,color=color,alpha=0.8,muted_color=color,muted_alpha=0.2,legend_label=name,source=source)
p.legend.location="top_left"
p.legend.click_policy="mute"
show(p)
