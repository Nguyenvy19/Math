import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px
import urllib.parse
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt

# Read the data from CSV
data = pd.read_csv('archive.csv')

# Set the page configuration
st.set_page_config(page_title = "Project Python 2", page_icon = ":tada:", layout="wide")

# HEADER SECTION
with st.container():
    st.subheader("Hi:wave: we're from Math IT 2-Group 9")
    st.title("What is there more to know about Nobel Prize Winners?")
    st.write("Apart from their achievements, join us today on this app to get to know the Laureates' Birth Countries and Average Lifespan!" ) 

# OUR DATASET
url = "https://www.kaggle.com/datasets/nobelfoundation/nobel-laureates?resource=download"
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column: st.header("Our dataset :sparkles:")
    st.markdown(f"[Click here to see the original dataset]({url})")
    st.write("##")
    st.markdown(
        """ ##### Data description:
        \n - This dataset contains the data representing the spending habits of <span style='color:green'>**1000**</span> students across various demographic groups and academic backgrounds.
        \n - In our report, we plotted <span style='color:green'>**13**</span> charts: Column charts,  Bar charts, Box plots, Violin chart, Ratio chart, Density chart.
        \n - Link: https://www.kaggle.com/datasets/sumanthnimmagadda/student-spending-dataset """,
        unsafe_allow_html=True
    )
    st.markdown(
        """ ##### Information:
        \n - The dataset includes information such as age, gender, year in school, major, monthly income, financial aid received, and expenses in different spending categories.""",
        unsafe_allow_html=True
    )
    st.markdown(
        """ ##### Spending category:
        \n - Spending categories include tuition, housing, food, transportation, books & supplies, entertainment, personal care, technology, health & wellness, and miscellaneous expenses.""",
        unsafe_allow_html=True
    )
    st.markdown(
        """ ##### Preferred payment method:
        \n - Credit, debit, cash, or mobile payment app.""",
        unsafe_allow_html=True
    )

st.divider()
st.header("Students speeding")

# Add Sidebar
st.sidebar.write('**:bulb: Reporting to Dr. Tan Duc Do**')
st.sidebar.write('**:bulb: Group 2 Members:**')

# Add content to the main area
with st.sidebar:
    st.write('Nguyen Pham Phuong Vy')
    st.write('Nguyen Mai Ky Duyen')
    st.write('Mai Huong Xuan')
    st.write('Nguyen Le Mai')
    st.write('Nguyen Tran Doan Thi')

# Initial 10 tabs for each interactive graph
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(["Plot 1", "Plot 2", "Plot 3", "Plot 4", "Plot 5", "Plot 6", "Plot 7", "Plot 8", "Plot 9", "Plot 10"])

# TAB 1: BAR CHART

# Read the data from CSV
Mydata = pd.read_csv('student_spending.csv', sep=';')
Mydata.columns = Mydata.columns.str.strip()

# Set the style and palette of the plot
sns.set(style="whitegrid", palette="pastel")

# Create a layout with columns
col1, col2 = st.columns([3, 8])  # adjust the numbers to change the width ratio of the columns

# Place the multiselect widget in the first column
with col1:
    selected_years = st.multiselect('Select years in school', options=Mydata['year_in_school'].unique(), default=Mydata['year_in_school'].unique())

# Filter the DataFrame based on the selected years
filtered_data = Mydata[Mydata['year_in_school'].isin(selected_years)]

# Create a new figure with smaller size
fig, ax = plt.subplots(figsize=(8, 4))  # adjust the numbers to change the size of the plot

# Create a countplot with the filtered data
bar_plot = sns.countplot(data=filtered_data, x='major', hue='year_in_school', dodge=True, ax=ax)

# Add annotations to the bars
for p in bar_plot.patches:
  height = p.get_height()
  bar_plot.annotate(f'{int(height)}',
           (p.get_x() + p.get_width() / 2., height),
           ha='center', va='center',
           xytext=(0, 5),
           textcoords='offset points')

# Set the title and labels of the plot
plt.title('The number of students in each major')
plt.xlabel('Major')
plt.ylabel('Count')

# Add a legend to the plot
legend = plt.legend(title='Year In School', prop={'size': 8}, loc='upper left', bbox_to_anchor=(1, 1), handlelength=2, handletextpad=0.4, borderpad=1.5, shadow=True)
frame = legend.get_frame()
frame.set_edgecolor('black') # Set legend border color
frame.set_linewidth(1.5)   # Set legend border width

# Display the plot in Streamlit
st.pyplot(fig)

### TAB 2: BOXPLOT CHART
  
# data[['Birth_Year', 'Birth_Month', 'Birth_Day']] = data['Birth_Date'].str.split("-", expand=True)
# data[['Death_Day', 'Death_Month', 'Death_Year']] = data['Death_Date'].str.split("/", expand=True)
# data["Birth_Year"] = pd.to_numeric(data["Birth_Year"], errors='coerce')
# data["Death_Year"] = pd.to_numeric(data["Death_Year"], errors='coerce')
# data["Year"] = pd.to_numeric(data["Year"], errors='coerce')
# data['Age'] = data['Death_Year'] - data['Birth_Year']
#
#
# # Sort the data by Age in ascending order
# data_sorted = data.sort_values(by='Age', ascending=True)
# # Create a subset of data for Physics, Medicine, and Chemistry categories
# nat = data_sorted[data_sorted['Category'].isin(['Chemistry', 'Physics', 'Medicine'])]
# # Create a subset of data for Literature, Peace, and Economics categories
# soc = data_sorted[data_sorted['Category'].isin(['Literature', 'Peace', 'Economics'])]
#
# # Create a palette color for categories
# category_colors = {
#     'Physics': '#7DEFA1',
#     'Chemistry': '#FF2B2B',
#     'Medicine': '#A5D7E8',
#     'Literature': '#0068C9',
#     'Peace': '#D4ADFC',
#     'Economics': '#29B09D'
# }
#
# # Add the title of the plot
# tab2.subheader("Lifespan of Nobel Winners")
#
# # Store the initial value of widgets in session state
# if "disabled" not in st.session_state:
#     st.session_state.disabled = False
#
# col1, col2, col3 = tab2.columns([2,2,3])
# with col1:
#     overview = st.checkbox("Overview of all categories", key="disabled")
#     age_type = st.radio("Choose a value you want to look for 👇",
#                         ["Oldest age", "Median age", "Youngest age"],
#                         key="visibility",
#                         # label_visibility= "visible",
#                         disabled= st.session_state.disabled)
# with col2:
#     rank = st.selectbox("Rank", ("Maximum", "Minimum"), key="rank",
#                         # label_visibility= "visible",
#                         disabled= st.session_state.disabled)
# with col3:
#     if overview:
#         st.write("Below is all categories.")
#     else:
#         st.write("Below are all categories with")
#         st.write("the {} value of the {} in each group.".format(rank.lower(), age_type.lower()))
#         st.write(":green[**Note: Outlier values are accepted.**]")
#
# # Create a container for displaying the boxplots
# with tab2.container():
#
#     # define a function to find the category as requested
#     def find_category(data, age_type, rank):
#         if age_type == "Oldest age":
#             if rank == "Maximum":
#                 category = data.groupby('Category')['Age'].max().idxmax()
#             else:
#                 category = data.groupby('Category')['Age'].max().idxmin()
#         elif age_type == "Median age":
#             if rank == "Maximum":
#                 category = data.groupby('Category')['Age'].median().idxmax()
#             else:
#                 category = data.groupby('Category')['Age'].median().idxmin()
#         elif age_type == "Youngest age":
#             if rank == "Maximum":
#                 category = data.groupby('Category')['Age'].min().idxmax()
#             else:
#                 category = data.groupby('Category')['Age'].min().idxmin()
#         return category
#
#    # Create two columns for displaying the boxplots
#     box1, box2 = tab2.columns(2)
#     with box1:
#         # Add label above the first boxplot
#         st.subheader("Natural Sciences")
#
#         # Display the first boxplot
#         if overview:
#             fig1 = px.box(nat, y="Age", x="Category", color="Category", color_discrete_map=category_colors)
#             fig1.update_layout(showlegend=False)  # Remove legend from the first plot
#         else:
#             nat_cat = find_category(nat, age_type, rank)
#             nat_display_cat = nat[nat['Category'].isin([nat_cat])]
#             fig1 = px.box(nat_display_cat, y="Age", x="Category", color="Category", color_discrete_map=category_colors)
#             fig1.update_layout(showlegend=False)  # Remove legend from the first plot
#
#         st.plotly_chart(fig1, use_container_width=True)
#
#
#     with box2:
#         # Add label above the second boxplot
#         st.subheader("Social Sciences")
#
#         # Display the second boxplot
#         if overview:
#             fig2 = px.box(soc, y="Age", x="Category", color="Category", color_discrete_map=category_colors)
#             fig2.update_layout(showlegend=False)  # Remove legend from the second plot
#         else:
#             soc_cat = find_category(soc, age_type, rank)
#             soc_display_cat = soc[soc['Category'].isin([soc_cat])]
#             fig2 = px.box(soc_display_cat, y="Age", x="Category", color="Category", color_discrete_map=category_colors)
#             fig2.update_layout(showlegend=False)  # Remove legend from the second plot
#
#         st.plotly_chart(fig2, use_container_width=True)
