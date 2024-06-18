import random

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from joypy import joyplot
import matplotlib
from matplotlib import cm

# Set the page configuration
st.set_page_config(page_title = "Project Python 2", page_icon = ":tada:", layout="wide")

# HEADER SECTION
with st.container():
    st.subheader("Hi:wave: we're from Math IT 2-Group 9")
    st.title("Students speeding")

# OUR DATASET
url = "https://www.kaggle.com/datasets/sumanthnimmagadda/student-spending-dataset"
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column: st.header("Our dataset :sparkles:")
    st.markdown(f"[Click here to see the original dataset]({url})")
    st.write("##")
    st.markdown(
        """ ##### Data description:
        \n - This dataset contains the data representing the spending habits of <span style='color:green'>**1000**</span> students across various demographic groups and academic backgrounds.
        \n - In our report, we plotted <span style='color:green'>**10**</span> charts: Column charts,  Bar charts, Box plots, Violin chart, Ratio chart, Density chart.
         """,
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

# Read the data from CSV
Mydata = pd.read_csv('student_spending.csv', sep=';')
Mydata.columns = Mydata.columns.str.strip()
data_1 = Mydata.copy()
data_2 = Mydata.copy()
data_3 = Mydata.copy()
data_4 = Mydata.copy()
data_5 = Mydata.copy()
data_6 = Mydata.copy()
data_7 = Mydata.copy()
data_8 = Mydata.copy()
data_9 = Mydata.copy()
data_10 = Mydata.copy()

# TAB 1
with tab1:
    df = data_1
    # Set the style and palette of the plot
    sns.set(style="whitegrid", palette="pastel")

    # Create a layout with columns
    col1, col2 = st.columns([3, 8])  # adjust the numbers to change the width ratio of the columns

    # Place the multiselect widget in the first column
    with col1:
        selected_years = st.multiselect('Select years in school', options=df['year_in_school'].unique()
                                        , default=df['year_in_school'].unique())

    # Filter the DataFrame based on the selected years
    filtered_data = df[df['year_in_school'].isin(selected_years)]

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

    st.markdown("<h3 style='text-align: center;'>Explanation</h3>", unsafe_allow_html=True)

    # Create an expander for the explanation content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The stacked bar chart visualizes the distribution of students across different majors: biology, computer science, economics, engineering, and psychology, categorized by academic level (freshmen, sophomores, juniors, and seniors). Among freshmen, biology emerges as the most popular major with 57 students, while economics attracts the fewest freshmen with only 44 students. Moving to juniors, biology retains its popularity, with 61 students opting for it, while psychology garners the least interest, with only 44 junior students. Interestingly, seniors show a shift in preferences, with engineering emerging as the most chosen major, attracting 57 students, while psychology remains the least favored choice, with only 41 senior students opting for it. Among sophomores, biology maintains its appeal as the most chosen major, with 57 students, whereas engineering attracts the fewest sophomores, with only 40 students selecting it. 
            </font>
            """, unsafe_allow_html=True)

    # Display the "Conclusion" title
    st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)

    # Create an expander for the conclusion content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            This stacked bar chart offers a clear visual representation of the varying popularity of majors across different academic levels, providing insights into student preferences and trends within the academic community.
            </font>
            """, unsafe_allow_html=True)

### TAB 2

with tab2:
    df = data_2
    df.columns = df.columns.str.strip()
    df.iloc[:, 7:] = df.iloc[:, 7:].apply(pd.to_numeric, errors='coerce')
    selected_gender = 'Female'  # Example gender selection
    filtered_df = df[df["gender"].str.strip() == selected_gender]
    data_by_age = filtered_df.groupby("age")[
        ["technology", "entertainment", "books_supplies", "personal_care"]].mean().reset_index()
    data_by_age.columns = data_by_age.columns.str.replace("_", " ").str.title()
    fig = go.Figure()
    categories = ["Technology", "Entertainment", "Books Supplies", "Personal Care"]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
    dash_styles = ['solid', 'dash', 'dot', 'dashdot']
    hover_labels = ['Technology: $', 'Entertainment: $', 'Books & Supplies: $', 'Personal Care: $']
    marker_symbols = ['circle', 'square', 'diamond', 'triangle-up']
    for i, category in enumerate(categories):
        fig.add_trace(go.Scatter(x=data_by_age["Age"], y=data_by_age[category],
                                 mode='lines+markers+text',
                                 name=category,
                                 text=[f'${val:.0f}' for val in data_by_age[category]],
                                 textposition="top center",
                                 textfont=dict(size=12, color=colors[i]),
                                 line=dict(color=colors[i], width=3, dash=dash_styles[i]),
                                 marker=dict(size=8, line=dict(width=2, color=colors[i])),
                                 marker_symbol=marker_symbols[i],
                                 hoverinfo='text',
                                 hovertext=[f'Age: {age}<br>{hover_labels[i]}{val:.0f}' for age, val in
                                            zip(data_by_age["Age"], data_by_age[category])]))
    fig.update_layout(title='Spending Trends by Age',
                      plot_bgcolor='white', paper_bgcolor='white', font_color='#333333', width=1500, height=800,
                      legend_title_text='Category',
                      xaxis_title='Age',
                      yaxis_title='Amount',
                      title_font_color='#333333',
                      legend_title_font_color='#333333',
                      legend_font_color='#333333',
                      xaxis_title_font=dict(color='#333333'),  # Set x-axis title font color
                      yaxis_title_font=dict(color='#333333'))  # Set y-axis title font color
    fig.update_xaxes(gridcolor='#CCCCCC', tickfont=dict(color='#333333'))
    fig.update_yaxes(gridcolor='#CCCCCC', dtick=50, range=[0, data_by_age[categories].values.max() + 50],
                     tickfont=dict(color='#333333'))
    st.plotly_chart(fig)

    st.markdown("<h3 style='text-align: center;'>Explanation</h3>", unsafe_allow_html=True)

    # Create an expander for the explanation content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The chart depicts spending trends across different age groups (18 to 24 years old) in four categories: Technology, Entertainment, Books and Supplies, and Personal Care. The data reveals that 21-year-olds spend the most on Technology, averaging $193, while 20-year-olds spend the least at $155. In the Entertainment category, 20-year-olds are the highest spenders with $91, whereas 23-year-olds spend the least at $79. For Books and Supplies, 20-year-olds again lead with $191, contrasted by 24-year-olds who spend the least at $171. In Personal Care, 18-year-olds allocate the most funds at $67, while 21-year-olds spend the least at $54. This chart highlights the diverse spending priorities among different age groups, with 20-year-olds generally showing higher expenditures in multiple categories.
            </font>
            """, unsafe_allow_html=True)

    # Display the "Conclusion" title
    st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)

    # Create an expander for the conclusion content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            This chart highlights the diverse spending priorities among different age groups, with 20-year-olds generally showing higher expenditures in multiple categories.
            </font>
            """, unsafe_allow_html=True)
### TAB 3
with tab3:
    df = data_3
    df.iloc[:, 5:] = df.iloc[:, 5:].apply(pd.to_numeric, errors='coerce')
    df = df.dropna(subset=["financial_aid"])
    avg_financial_aid = df.groupby("year_in_school")["financial_aid"].mean().reset_index()
    year_mapping = {'Freshman': 1, 'Sophomore': 2, 'Junior': 3, 'Senior': 4}
    avg_financial_aid['year_in_school'] = avg_financial_aid['year_in_school'].str.strip().str.capitalize()
    avg_financial_aid['year_in_school_numeric'] = avg_financial_aid['year_in_school'].map(year_mapping)

    sns.set_style("whitegrid")
    sns.set_palette("pastel")
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.scatterplot(x="year_in_school", y="financial_aid", data=avg_financial_aid, s=100, color='#6baed6',
                    edgecolor='black', ax=ax)
    z = np.polyfit(avg_financial_aid["year_in_school_numeric"], avg_financial_aid["financial_aid"], 1)
    p = np.poly1d(z)
    ax.plot(avg_financial_aid["year_in_school"], p(avg_financial_aid["year_in_school_numeric"]), "r--",
            label='Trendline')
    for i in range(avg_financial_aid.shape[0]):
        ax.text(avg_financial_aid["year_in_school"][i], avg_financial_aid["financial_aid"][i] + 0.5,
                f"${avg_financial_aid['financial_aid'][i]:.2f}", horizontalalignment='center', color='black',
                fontsize=10)
    ax.set_title('Average Financial Aid by Year in School', fontsize=18, color='#333333')
    ax.set_xlabel('Year in School', fontsize=14, color='#333333')
    ax.set_ylabel('Average Financial Aid', fontsize=14, color='#333333')
    ax.legend()

    st.pyplot(fig)

    st.markdown("<h3 style='text-align: center;'>Explanation</h3>", unsafe_allow_html=True)

    # Create an expander for the explanation content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The line chart illustrates the average financial aid received by students at different academic levels: Freshman, Sophomore, Junior, and Senior. Freshmen receive an average of $504.31 in financial aid, indicating strong initial support for students beginning their college education. Sophomores see a slight decrease in average aid to $492.15, representing the lowest level of financial support among the four years. The financial aid peaks during the Junior year at $518.83, suggesting increased support as students advance in their studies, likely due to higher costs or greater eligibility for aid at this stage. Seniors receive an average of $503.78, slightly less than Freshmen and Juniors but more than Sophomores, reflecting a balance between the nearing completion of degree requirements and available financial support. Overall, the trend shows that financial aid is most substantial at the beginning and near the end of the college journey, with a notable peak in the Junior year. 
            </font>
            """, unsafe_allow_html=True)

    # Display the "Conclusion" title
    st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)

    # Create an expander for the conclusion content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            Overall, the trend shows that financial aid is most substantial at the beginning and near the end of the college journey, with a notable peak in the Junior year. 
            </font>
            """, unsafe_allow_html=True)


### TAB 4
with tab4:
    df = data_4
    df.columns = df.columns.str.strip()
    df.iloc[:, 5:] = df.iloc[:, 5:].apply(pd.to_numeric, errors='coerce')
    df = df.dropna(subset=["financial_aid"])
    avg_financial_aid = df.groupby("year_in_school")["financial_aid"].mean().reset_index()
    pastel_colors = px.colors.qualitative.Pastel1
    fig = px.pie(avg_financial_aid, values="financial_aid", names="year_in_school",
                 title="Average Financial Aid by Year in School",
                 color_discrete_sequence=pastel_colors,
                 hover_data={"financial_aid": ":.2f"},
                 labels={"financial_aid": "Financial Aid", "year_in_school": "Year in School"})
    fig.update_traces(textposition='inside', textinfo='percent+label', textfont=dict(size=12, color='#333333'),
                      hovertemplate="Year in School: %{label}<br>Financial Aid: $%{value:.2f}")
    fig.update_layout(plot_bgcolor='#F0E2E2',  # Pastel pink background color
                      paper_bgcolor='#F0E2E2',  # Pastel pink background color
                      font_color='#333333',  # Dark gray font color for better contrast
                      width=1000, height=800,
                      legend_title_text='Year in School',
                      title_font_color='#333333',  # Dark gray color for the plot title
                      legend_title_font_color='#333333',  # Dark gray color for the legend title
                      legend_font_color='#8E7CC3')  # Pastel purple color for the legend text
    st.plotly_chart(fig)

    st.markdown("<h3 style='text-align: center;'>Explanation</h3>", unsafe_allow_html=True)

    # Create an expander for the explanation content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The pie chart offers a breakdown of the average financial aid distribution across different academic years: Freshman, Sophomore, Junior, and Senior. Freshmen and Seniors each account for a quarter of the total financial aid, indicating comparable levels of support at the beginning and end of the college journey. This suggests that institutions prioritize assisting students as they enter and prepare to graduate from college. Juniors receive the largest share at 25.7%, indicating a slight increase in financial aid during this pivotal year. This could reflect heightened educational costs or increased eligibility for aid as students progress toward their degree completion. Conversely, Sophomores receive the smallest share at 24.4%, indicating a slight decrease in aid during the second year of study.
            </font>
            """, unsafe_allow_html=True)

    # Display the "Conclusion" title
    st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)

    # Create an expander for the conclusion content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            This distribution underscores a relatively equitable allocation of financial assistance throughout the academic years, with a notable emphasis on support during the critical Junior year. 
            </font>
            """, unsafe_allow_html=True)
### TAB 5
with tab5:
    df = data_5
    np.random.seed(2)
    random.seed(2)
    matplotlib.rcParams[
        'font.family'] = 'DejaVu Sans'  # replace 'DejaVu Sans' with the name of a font available on your system
    matplotlib.rcParams['font.sans-serif'] = "Comic Sans Ms"

    df['year_in_school'] = df['year_in_school'].astype(str)
    plt.figure(figsize=(5, 3.5))  # replace 10 and 7.5 with the width and height you want

    joyplot(df, by='year_in_school', colormap=cm.summer, column='age', fade=True, range_style='own', figsize=(35, 18),
            title='THE PEAK OF EACH YEAR IN SCHOOL'
            )
    plt.xlabel("AGE")
    plt.rc('font', size=20)
    st.pyplot(plt.gcf())

    # Create an expander for the explanation content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The ridgeline plot captures the ebb and flow of academic progression over the years of schooling, with each peak representing the pinnacle of a particular academic year. 

At the forefront of the plot, the highest peaks symbolize the influx of freshmen, typically aged 19 and 24, as they embark on their inaugural year of higher education. This surge reflects the excitement and anticipation that often accompanies the transition to college or university life. Slightly trailing behind the freshmen surge, there's another notable peak denoting the sophomore year. Predominantly populated by individuals aged 25, this cohort represents the seasoned freshmen who have embraced the rhythm of collegiate life and are now well-versed in the nuances of academia. As the plot progresses, a prominent peak emerges around the age of 23, signifying the junior year. This stage marks a pivotal moment in the academic journey, where students delve deeper into their chosen fields of study, engage in specialized coursework, and perhaps embark on internships or research endeavors.
            </font>
            """, unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'>Explanation</h3>", unsafe_allow_html=True)

    # Display the "Conclusion" title
    st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)

    # Create an expander for the conclusion content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            Throughout the ridgeline plot, the peaks and troughs illustrate the cyclical nature of academic progression, with each stage offering its own set of challenges, triumphs, and milestones. It's a visual testament to the diverse experiences and journeys undertaken by students as they navigate the corridors of education, each peak representing a summit reached and conquered in pursuit of knowledge and personal growth.
            </font>
            """, unsafe_allow_html=True)
### TAB 6
with tab6:
    # Create a selectbox for the major
    df = data_6
    all_majors = df['major'].unique()
    selected_majors = st.multiselect('Select major(s)', options=all_majors, default=all_majors)

    # Filter the DataFrame based on the selected majors
    filtered_data = df[df['major'].isin(selected_majors)]

    # Create the plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=filtered_data, x='health_wellness', y='major', palette=['#41E5F2'], linewidth=1, flierprops=dict(marker='o', markersize=5, markerfacecolor='red'))
    plt.title('Expenses that Students Spend for the Purpose of Staying Healthy')
    plt.xlabel('Health Wellness')
    plt.ylabel('Major')
    plt.grid(True)

    # Display the plot in Streamlit
    st.pyplot(plt.gcf())
    # Create an expander for the explanation content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            This boxplot provides a concise overview of the expenses incurred by students from various majors - biology, computer science, economics, engineering, and psychology - concerning their health maintenance. By visualizing the range of expenditures across disciplines, it offers valuable insights into students' health-related spending patterns.
Engineering students demonstrate the highest expenditure range, with costs ranging from $60 to $155. This suggests a significant investment in maintaining health, potentially attributed to the demanding nature of engineering studies and the importance of physical and mental well-being in this field.
Conversely, psychology students exhibit the lowest expenditure range, with expenses ranging from $78 to $157. Despite the relatively lower spending compared to other majors, this still signifies a considerable financial commitment toward health-related necessities, reflecting the importance of holistic well-being in psychological studies.
            </font>
            """, unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'>Explanation</h3>", unsafe_allow_html=True)

    # Display the "Conclusion" title
    st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)

    # Create an expander for the conclusion content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The boxplot showcases spending variations across majors, revealing diverse health expenditure priorities among students. This insight informs tailored support and resource allocation to address students' diverse health needs.
            </font>
            """, unsafe_allow_html=True)
### TAB 7
with tab7:
    # Create a selectbox for the major
    df = data_7
    plt.figure(figsize=(12, 8))
    sns.kdeplot(data=df['personal_care'], color='skyblue', fill=True, label='KDE')
    plt.title('Kernel Density Estimation Plot')
    plt.xlabel('Personal Care Spending')
    plt.ylabel('Density')

    st.pyplot(plt.gcf())
    # Create an expander for the explanation content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The kernel density estimation plot visualizes the distribution of personal care spending, showing how the density of spending changes across different levels. Initially, at a spending level of 0, the density of personal care spending is also 0. As spending increases to 30, the density begins to grow, indicating an increasing number of individuals spending in this range. The plot then reaches a balance, where the density stabilizes momentarily before continuing to rise. This balance suggests a common range of personal care spending among a significant portion of the population. Finally, the plot peaks at a spending level of 76, with a density of 0.014, indicating the highest concentration of individuals spending at this level. 
            </font>
            """, unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'>Explanation</h3>", unsafe_allow_html=True)

    # Display the "Conclusion" title
    st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)

    # Create an expander for the conclusion content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            This visualization provides insights into the distribution and patterns of personal care spending among the sampled population, showing where spending is most concentrated and how it varies across different levels.
            </font>
            """, unsafe_allow_html=True)
### TAB 8
with tab8:
    df = data_8
    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 8))
    sns.histplot(df['entertainment'], bins=20, kde=False, color='#bdd7e7', edgecolor='black', stat='density')
    sns.kdeplot(df['entertainment'], color='#6baed6', linewidth=2)
    plt.title('Density Distribution of Student Spending on Entertainment', fontsize=16)
    plt.xlabel('Entertainment', fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)

    st.pyplot(plt.gcf())

    st.markdown("<h3 style='text-align: center;'>Explanation</h3>", unsafe_allow_html=True)

    # Create an expander for the explanation content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The column chart illustrates the density distribution of student spending on entertainment, ranging from a minimum of $10 to a peak of around $120. Each column represents a specific spending range, with the height of the column indicating the density of student spending within that range. At the lower end of the spectrum, spending of $10 has the lowest density, denoted by a column with a height corresponding to a density of 0.0025. This suggests that fewer students spend this amount on entertainment. In contrast, around the $120 mark, the density of student spending is notably higher, represented by a taller column with a density of 0.0075. This indicates that a larger proportion of students spend around $120 on entertainment, reflecting a peak in spending within this range.
            </font>
            """, unsafe_allow_html=True)

    # Display the "Conclusion" title
    st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)

    # Create an expander for the conclusion content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The chart visually depicts the distribution of student spending on entertainment, highlighting the varying densities across different spending levels and emphasizing the prevalence of spending around $120 compared to lower amounts like $10.
            </font>
            """, unsafe_allow_html=True)

### TAB 9
with tab9:
    df = data_9
    fig = go.Figure()
    fig.add_trace(go.Violin(x=df['major'][df['gender'].str.strip() == 'Male'],
                            y=df['food'][df['gender'].str.strip() == 'Male'],
                            legendgroup='M', scalegroup='M', name='M',
                            line_color='magenta')
                  )

    fig.add_trace(go.Violin(x=df['major'][df['gender'].str.strip() == 'Female'],
                            y=df['food'][df['gender'].str.strip() == 'Female'],
                            legendgroup='F', scalegroup='F', name='F',
                            line_color='skyblue')
                  )

    fig.update_layout(
        title="The Expenditure on Food of Male and Female on Each Major",
        xaxis_title="Major",
        yaxis_title="Allocating for Food",
        legend_title="Gender",
        font=dict(
            size=18,
            color="RebeccaPurple")
    )

    st.plotly_chart(fig)

    st.markdown("<h3 style='text-align: center;'>Explanation</h3>", unsafe_allow_html=True)

    # Create an expander for the explanation content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            This violin chart offers a concise examination of food expenditure among individuals of two genders: female amd male on each major, including: Biology, Engineering, Economics, Psychology, and Computer Science  major. Visualizing the range of expenditures across genders and majors provides insights into spending patterns related to nutritional needs.
 The proportions of male and female on Biology and Engineering major shared the similar from 100 to 300$. Howerver, women tent to spend more money on expensive food than men in both of these areas, in the range of 300$ and up. In Economics and Psychology major, more women than men spent between $50 and $180 and around $280 and $310, but they spent less between about $180 and  $280. According to the remaining major, the number of both sexes from 50 to 110 and 250 to 450 was relatively comparable , but in the range from 110 to 250, the number of females was nearly twofold that of males.
            </font>
            """, unsafe_allow_html=True)

    # Display the "Conclusion" title
    st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)

    # Create an expander for the conclusion content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The violin chart effectively captures the diversity in spending patterns among different genders on each major, offering valuable insights for understanding nutritional priorities and consumption behaviors. These insights can inform targeted support initiatives and resource allocation strategies aimed at promoting equitable access to healthy food options and addressing the diverse dietary needs of individuals across gender identities.
            </font>
            """, unsafe_allow_html=True)
### TAB 10
with tab10:
    df = data_10
    payment_method_counts = data_10['preferred_payment_method'].value_counts()
    colors = ['#B9E3F8', '#FFD699', '#D9F0D3']  # Blue, Orange, Green
    explode = (0.1, 0, 0)  # explode 1st slice
    plt.figure(figsize=(10, 6))
    plt.pie(payment_method_counts, labels=payment_method_counts.index, autopct='%1.1f%%', startangle=140, colors=colors,
            explode=explode, shadow=True)
    plt.axis('equal')
    plt.title('Distribution of Preferred Payment Methods', y=1.05)
    plt.legend(title='Payment Method', loc='best')

    st.pyplot(plt.gcf())

    st.markdown("<h3 style='text-align: center;'>Explanation</h3>", unsafe_allow_html=True)

    # Create an expander for the explanation content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            The pie chart displays the distribution of preferred payment methods among individuals, categorized into three options: mobile payment app, credit/debit card, and cash. Mobile payment apps are the most preferred method, accounting for 35% of the total. Close behind, credit/debit cards are chosen by 34% of individuals, reflecting their nearly equal popularity. Cash is the least preferred method, used by 31% of people. This distribution indicates a balanced preference among the three payment methods, with a slight inclination towards the convenience and technological advantages offered by mobile payment apps and credit/debit cards over traditional cash.
            </font>
            """, unsafe_allow_html=True)

    # Display the "Conclusion" title
    st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)

    # Create an expander for the conclusion content
    with st.expander(""):
        st.markdown("""
            <font size="4">
            This distribution indicates a balanced preference among the three payment methods, with a slight inclination towards the convenience and technological advantages offered by mobile payment apps and credit/debit cards over traditional cash.
            </font>
            """, unsafe_allow_html=True)