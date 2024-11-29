import streamlit as st
import pandas as pd
import numpy as np
#import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.figure_factory as ff



# # Title and description
# st.title('Tourism in the World')

# # Plot - total volume inbound per year
# df_in_peryear = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/inbound_per_year.csv')

# st.subheader('Total inbound volume per year')
# st.text('\n')
# st.text('\n')
# st.bar_chart(df_in_peryear, x ='index')
# st.text('\n')
# st.text('\n')

# # Plot - total volume inbound per year, including regions
# st.subheader('Total inbound volume per year, visualization per regions')
# st.text('\n')
# st.text('\n')
# df_year_region = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/inbound_year_region.csv')
# st.bar_chart(df_year_region, x ='index')
# st.text('\n')
# st.text('\n')

# df = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/total_inbound.csv')


# # Plot - Pie chart
# df_regions = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/regions.csv')
# st.subheader('Inbound volume distribution per region')


# fig1, ax1 = plt.subplots()
# ax1.pie(df_regions['percentage'],labels=df_regions['regions'], autopct="%1.1f%%", labeldistance=1.2, wedgeprops={"linewidth": 1, "edgecolor": "white"})
# ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
# plt.xticks(rotation=45)   
# st.pyplot(fig1)
# st.text('\n')
# st.text('\n')

# # Plot  - Top 20
# df_in_country = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/inbound_per_country.csv')
# df_in_country = df_in_country.sort_values(by = 'total per country', ascending=False)
# st.subheader('Top 20 countries, volume for all years')
# st.bar_chart(df_in_country.sort_values(by = 'total per country', ascending=False).head(20), x = 'Country', horizontal = True)

# # Plot  - selected countries
# # Sidebar for user input
# st.sidebar.header('Select the country and the year')

# top_five = ['FRANCE','UNITED STATES OF AMERICA','MEXICO','SPAIN','POLAND']
# country_filter = st.sidebar.multiselect("Select Country", options= df['Country'].unique(), default = top_five)

# y= df.columns.tolist()
# year_list=y[1:-1]
# year_filter = st.sidebar.multiselect("Select year", options=year_list, default=year_list)

# # Filter dataset based on selections
# items = year_filter
# #items.insert(0,'Country')
# df_temp = df[df['Country'].isin(country_filter)]
# filtered_df = df_temp[[i for i in items]]


# transposed_viz = filtered_df.set_index('Country')
# transposed_viz = transposed_viz.transpose()

# filtered_df['Total']=filtered_df.sum(axis=1, numeric_only=True)


# st.subheader('Volume per selected country and year')
# st.bar_chart(transposed_viz)

# Data
# df_in_peryear = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/inbound_per_year.csv')
# df_year_region = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/inbound_year_region.csv')
# df = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/total_inbound.csv')
# df_regions = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/regions.csv')
# df_in_country = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/inbound_per_country.csv')
# df_in_country = df_in_country.sort_values(by = 'total per country', ascending=False)
# df_in_country = df_in_country.drop('Unnamed: 0', axis=1)
# #heat_region = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/heat_region.csv')
# sum_expenditure = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/sum_expenditure.csv')
# gdp_pcap = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/gdp_pcap_table.csv')
# global_employment = pd.read_csv('/Users/marjoriefalcon/Desktop/Bootcamp DS-22/M4P3-Final_Project-main/Tourism/Out/global_employment.csv')

df_in_peryear = pd.read_csv('inbound_per_year.csv')
df_year_region = pd.read_csv('inbound_year_region.csv')
df = pd.read_csv('total_inbound.csv')
df_regions = pd.read_csv('regions.csv')
df_in_country = pd.read_csv('inbound_per_country.csv')
df_in_country = df_in_country.sort_values(by = 'total per country', ascending=False)
df_in_country = df_in_country.drop('Unnamed: 0', axis=1)
sum_expenditure = pd.read_csv('sum_expenditure.csv')
gdp_pcap = pd.read_csv('gdp_pcap_table.csv')
global_employment = pd.read_csv('global_employment.csv')



# Plot - total volume inbound per year
def show_volume_year():
  st.text('\n')
  st.text('\n')
  st.bar_chart(df_in_peryear, x ='index', x_label = '', y_label = 'Thousands')
  st.text('\n')
  st.text('\n')

# # Plot - total volume inbound per year, including regions
def show_volume_year_region():
  st.write('Regions defined according to the World Bank')
  st.text('\n')
  st.text('\n')
  st.bar_chart(df_year_region, x ='index', x_label = '', y_label = 'Thousands')
  st.text('\n')
  st.text('\n')

  # Plot - Pie chart
  st.subheader('Inbound volume distribution per region')
  fig1, ax1 = plt.subplots()
  ax1.pie(df_regions['percentage'],labels=df_regions['regions'], autopct="%1.1f%%", labeldistance=1.2, wedgeprops={"linewidth": 1, "edgecolor": "white"} )
  ax1.axis("equal")  # Equal aspect ratio ensures that pie is drawn as a circle.
  plt.xticks(rotation=45)
  st.pyplot(fig1)
  st.text('\n')
  st.text('\n')

# Plot  - selected countries 
def explore_per_country():
  # Sidebar for user input
  #st.sidebar.header('Select the country and the year')

  top_five = ['FRANCE','UNITED STATES OF AMERICA','MEXICO','SPAIN','POLAND']
  
  y= df.columns.tolist()
  year_list=y[1:-1]
  
  
  country_filter = st.multiselect("Select Countries", options= df['Country'].unique(), default = top_five, key='ms1')
  year_filter = st.multiselect("Select years", options=year_list, default=year_list, key='ms2')

  items = year_filter
  items.insert(0,'Country')
  df_temp = df[df['Country'].isin(country_filter)]

  
  filtered_df = df_temp[[y for y in items]]

  filtered_df = filtered_df.set_index('Country')
  transposed_viz = filtered_df.transpose()
  st.text('\n')
  st.text('\n')
  st.text('\n')
  st.text('\n')
  st.bar_chart(transposed_viz, y_label = 'Thousands')

def show_top20():
   # Plot  - Top 20
   
   st.bar_chart(df_in_country.head(20), x = 'Country', x_label= 'Volume in thousands', horizontal = True)

# def volume_change():
#   fig, ax = plt.subplots()
#   sns.heatmap(heat_region, annot=True, cbar_kws={'label': 'Percentage Change (%)'}, ax=ax)
#   st.pyploy(fig)
# #   ax5=sns.heatmap(heat_region, annot=True, cmap='rocket_r', fmt='.2f', linewidths=0.5, cbar_kws={'label': 'Percentage Change (%)'})
#   ax5.set(xlabel=""); 

def expenditure_volume():
 
  y_list= list(range(1995,2022))
  year = st.selectbox('Select a year',y_list, placeholder='Select a year', key = 'sel1')
  st.write("You selected:", year)

  
  year = str(year)
  expenditure = sum_expenditure.set_index('country')
  expenditure = expenditure[[year]]
  expenditure['expenditure']=expenditure[year]
  expenditure = expenditure.drop(year,axis =1)
  
  inbound = df.set_index('Country')
  inbound = inbound[[year]]
  inbound['Inbound Volume']=inbound[year]
  inbound = inbound.drop(year,axis =1)
  

  df_country_year = inbound.join(expenditure, how='left')
  
  fig = px.scatter(
      df_country_year,
      x='Inbound Volume',
      y='expenditure',
      hover_name=df_country_year.index,
      size_max=60)
  st.plotly_chart(fig, theme="streamlit")
  

def expenditure_gdp():
  
  y_list= list(range(1995,2022))
  year = st.selectbox('Select a year',y_list, placeholder='Select a year', key = 'sel2')
  st.write("You selected:", year)
  
  
  year = str(year)
  gdp = gdp_pcap.set_index('Country')
  gdp = gdp[[year]]
  gdp['GDP per capita']=gdp[year]
  gdp = gdp.drop(year,axis =1)

  expenditure = sum_expenditure.set_index('country')
  expenditure = expenditure[[year]]
  expenditure['expenditure']=expenditure[year]
  expenditure = expenditure.drop(year,axis =1)
  
  df_gdp_expenditure = expenditure.join(gdp, how='left')

  
  fig2 = px.scatter(
      df_gdp_expenditure,
      x='expenditure',
      y = 'GDP per capita',
      hover_name=df_gdp_expenditure.index,
      size_max=60)
  st.plotly_chart(fig2, theme="streamlit")
  

def expenditure_employment():
  
  y_list= list(range(2014,2023))
  year = st.selectbox('Select a year',y_list, placeholder='Select a year', key = 'sel3')
  st.write("You selected:", year)
  
  year = str(year)
  employment = global_employment.set_index('Country')
  employment = employment[[year]]
  employment['Employment rate']=employment[year]
  employment = employment.drop(year,axis =1)


 

  expenditure = sum_expenditure.set_index('country')
  expenditure = expenditure[[year]]
  expenditure['expenditure']=expenditure[year]
  expenditure = expenditure.drop(year,axis =1)
  
  
  df_empl_expenditure = expenditure.join(employment, how='left')

  
  fig2 = px.scatter(
      df_empl_expenditure,
      x='expenditure',
      y = 'Employment rate',
      hover_name=df_empl_expenditure.index,
      size_max=60)
  st.plotly_chart(fig2, theme="streamlit")
  
  



def show_explore_page():
  # st.title('Tourism in the World')
  # st.write('Tourism plays a vital role in the global economy, contributing to employment, cultural exchange, and the development of infrastructure. Tourism statistics are essential for understanding the patterns and dynamics of travel and tourism, helping stakeholders such as governments, businesses, and policymakers make informed decisions.')
  # st.write('These statistics encompass a wide range of data, including the number of visitors to a destination, their spending and the impacts of tourism on local economy.')
  # st.write('The following anaylisis aims to explore tourism data to uncover insights and understand emerging trends.')

  #tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Explore','Volume per year','Regions','Top 20','Volume vs Revenue','Revenue vs. GDP', 'Revenue vs. Employment rate'])
  tab1, tab3, tab4, tab5, tab6, tab7 = st.tabs(['Explore','Regions','Top 20','Volume vs Revenue','Revenue vs. GDP', 'Revenue vs. Employment rate'])
  
  with tab1:
   st.subheader('Number of visitors')
   st.write('(Inbound Volume)')
   explore_per_country()
   
  # with tab2:
  #   st.subheader('Volume of visitors, for all the countries, per year')
  #   show_volume_year()
  
  with tab3:
    st.subheader('Number of visitors per region')
    show_volume_year_region()
  
  with tab4:
    st.subheader('Top 20 countries that had  most visits overall')
    show_top20()
  
  with tab5:
    st.subheader('Tourism volume vs. Revenue from tourism')
    expenditure_volume()

  with tab6:
    st.subheader('Revenue from tourism vs. GDP')
    st.write('GDP data source : The World Bank')
    expenditure_gdp()

  with tab7:
    st.subheader('Revenue from tourism vs. Employment rate')
    st.write('Employment rate source : The World Bank')
    expenditure_employment()
  
    
   
   
show_explore_page()

