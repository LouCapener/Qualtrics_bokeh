#!/usr/bin/env python
# coding: utf-8
# Set environment variable to inline 
# Tells Python program to package all the things needed to display our Bokeh plots inside the HTML file itself
os.environ['BOKEH_RESOURCES'] = "inline"
# In[1]:


# used to manipulate dataframes
import pandas as pd

# used to create visualisations
import seaborn as sns
import matplotlib.pylab as plt

# used to create interactive visualisations
from bokeh.io import show, curdoc, output_notebook
from bokeh.layouts import column, row
from bokeh.models import (
    ColumnDataSource,
    ColorBar,
    BasicTicker,
    PrintfTickFormatter,
    LinearColorMapper,
    Select,
    HTMLTemplateFormatter,
)
from bokeh.models.annotations import LabelSet
from bokeh.palettes import Category10
from bokeh.plotting import figure


# In[2]:


import os

os.getcwd()


# In[3]:


# Read-in pre-processed data for religion

rel = pd.read_csv('Data/religion_gi_cleaned.csv')


# In[4]:


# Prepare data

rel['selected_religion'] = rel['Christian_Percentage']
rel['selected_percentages'] = rel['Christian_NR']


# In[5]:


source = ColumnDataSource(rel)


# In[6]:


# Create select widget

options = ['Christian', 'Muslim', 'Jewish', 'Buddhist', 'Hindu', 'Sikh', 'Other religion', 'No religion']  # Update with all available religious groups
select_religion = Select(title="Religious Group:", value='Christian', options=options)


# In[7]:


# Define callback for updating data source

def update_plot(attr, old, new):
    selected_religion = select_religion.value
    rel['selected_religion'] = rel[f'{selected_religion}_Percentage']
    rel['selected_percentages'] = rel[f'{selected_religion}_NR']
    source.data = source.from_df(rel)

    
# Attach callback to the select widget
# Update the plot when the value in the dropdown changes
select_religion.on_change('value', update_plot)


# In[9]:


# Create figure
p4 = figure(title="Relationship between % of religious group in given LA, and their non-response rate",
            y_axis_label="Non-response Rate", x_axis_label="Percentage of religious group in given LA")

# Scatter plot
p4.scatter("selected_religion", "selected_percentages", source=source, fill_alpha=0.5, size=10)


# In[14]:


from bokeh.plotting import figure, ColumnDataSource
from bokeh.models import Select
from bokeh.layouts import column
from bokeh.io import curdoc
import pandas as pd

# Your existing code for reading data, creating source, etc.

# Define a function for your application
def modify_doc(doc):
    # Include your plotting code here (without output_notebook and show)

    # Layout
    layout = column(select_religion, p4)
    doc.add_root(layout)

# Link the function to curdoc
modify_doc(curdoc())

