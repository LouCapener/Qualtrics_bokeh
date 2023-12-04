#!/usr/bin/env python
# coding: utf-8

import pandas as pd
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure

# Read-in pre-processed data for religion
rel = pd.read_csv('Data/religion_gi_cleaned.csv')

# Prepare initial data
rel['selected_religion'] = rel['Christian_Percentage']
rel['selected_percentages'] = rel['Christian_NR']
source = ColumnDataSource(rel)

# Create select widget
options = ['Christian', 'Muslim', 'Jewish', 'Buddhist', 'Hindu', 'Sikh', 'Other religion', 'No religion']
select_religion = Select(title="Religious Group:", value='Christian', options=options)

# Define callback for updating data source
def update_plot(attr, old, new):
    selected_religion = select_religion.value
    rel['selected_religion'] = rel[f'{selected_religion}_Percentage']
    rel['selected_percentages'] = rel[f'{selected_religion}_NR']
    source.data = ColumnDataSource.from_df(rel)

# Attach callback to the select widget
select_religion.on_change('value', update_plot)

# Create figure
p4 = figure(title="Relationship between % of religious group in given LA, and their non-response rate",
            y_axis_label="Non-response Rate", x_axis_label="Percentage of religious group in given LA")

# Scatter plot
p4.scatter("selected_religion", "selected_percentages", source=source, fill_alpha=0.5, size=10)

# Layout
layout = column(select_religion, p4)

# Add the layout to curdoc
curdoc().add_root(layout)

