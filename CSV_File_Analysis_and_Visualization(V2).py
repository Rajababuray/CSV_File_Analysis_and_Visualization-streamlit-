import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np

def main():
    st.title('CSV File Analysis and Visualization')
    st.write("Objective: This application analyzes CSV files containing student data and provides insights through visualizations and summaries.")

    st.sidebar.title('Upload CSV File')
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=['csv'])

    if uploaded_file is not None:
        # Read data into DataFrame
        df = pd.read_csv(uploaded_file)

        # Data Preprocessing
        st.subheader('Data Preprocessing')
        st.write("Data Preview:")
        st.write(df.head())

        # Perform Exploratory Data Analysis (EDA)
        st.subheader('Exploratory Data Analysis (EDA)')

        # Choose Analytical Tools and Techniques
        # Summary statistics
        st.write("Summary Statistics:")
        st.write(df.describe())

        # Display correlation heatmap for numerical columns
        numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
        if len(numerical_cols) > 1:  # Check if there are numerical columns for correlation
            corr_df = df[numerical_cols].corr()

            # Create a Matplotlib figure for the heatmap
            fig, ax = plt.subplots()
            sns.heatmap(corr_df, annot=True, cmap='viridis', ax=ax)
            st.write("Correlation Heatmap:")
            st.pyplot(fig)

            # Develop Automated Analysis Scripts or Algorithms
            # Visualization options after EDA
            st.sidebar.subheader('Choose Visualization:')
            visualization_option = st.sidebar.radio('Select Visualization', ['Histogram', 'Scatter Plot', 'Pie Chart', 'Bar Chart', 'Donut Chart', 'Violin Plot', 'Pair Plot', 'Line Plot', 'Density Plot'])

            if visualization_option == 'Histogram':
                selected_column = st.selectbox('Select Column for Histogram', df.columns)
                if selected_column:
                    st.write(f"Histogram for {selected_column}")
                    fig = px.histogram(df, x=selected_column)
                    st.plotly_chart(fig)

            elif visualization_option == 'Scatter Plot':
                x_column = st.sidebar.selectbox('Select X-axis column', df.columns)
                y_column = st.sidebar.selectbox('Select Y-axis column', df.columns)
                if x_column and y_column:
                    st.write(f"Scatter Plot for {x_column} vs {y_column}")
                    fig = px.scatter(df, x=x_column, y=y_column)
                    st.plotly_chart(fig)

            elif visualization_option == 'Pie Chart':
                st.write("Pie Chart")
                selected_column = st.sidebar.selectbox('Select Column for Pie Chart', df.columns)
                if selected_column:
                    fig = px.pie(df, names=df[selected_column].value_counts().index, values=df[selected_column].value_counts().values)
                    st.plotly_chart(fig)

            elif visualization_option == 'Bar Chart':
                st.write("Bar Chart")
                selected_column = st.sidebar.selectbox('Select Column for Bar Chart', df.columns)
                if selected_column:
                    data_counts = df[selected_column].value_counts().reset_index()
                    data_counts.columns = ['Values', 'Counts']
                    bar_fig = px.bar(data_counts, x='Values', y='Counts')
                    st.plotly_chart(bar_fig)

            elif visualization_option == 'Donut Chart':
                st.write("Donut Chart")
                selected_column = st.sidebar.selectbox('Select Column for Donut Chart', df.columns)
                if selected_column:
                    fig = px.pie(df[selected_column].value_counts(), names=df[selected_column].value_counts().index, values=df[selected_column].value_counts().values, hole=0.3)
                    st.plotly_chart(fig)

            elif visualization_option == 'Violin Plot':
                st.write("Violin Plot")
                selected_column = st.sidebar.selectbox('Select Column for Violin Plot', df.columns)
                if selected_column:
                    fig = px.violin(df, y=selected_column)
                    st.plotly_chart(fig)

            elif visualization_option == 'Pair Plot':
                st.write("Pair Plot")
                fig = px.scatter_matrix(df)
                st.plotly_chart(fig)

            elif visualization_option == 'Line Plot':
                st.write("Line Plot")
                selected_column = st.sidebar.selectbox('Select Column for Line Plot', df.columns)
                if selected_column:
                    fig = px.line(df, x=df.index, y=selected_column)
                    st.plotly_chart(fig)

            elif visualization_option == 'Density Plot':
                st.write("Density Plot")
                selected_column = st.sidebar.selectbox('Select Column for Density Plot', df.columns)
                if selected_column:
                    fig = px.density_contour(df, x=selected_column)
                    st.plotly_chart(fig)
            else:
                st.warning("No numerical columns found for correlation calculation.")

            st.sidebar.title('Dashboard')
            show_dashboard = st.sidebar.checkbox('Show Dashboard')

            if show_dashboard:
                st.subheader('Custom Dashboard')

                # Summary statistics in the dashboard
                st.write("### Summary Statistics")
                st.write(df.describe())

                # Count plot for a categorical column
                st.write("### Count Plot for a Categorical Column")
                categorical_col = st.selectbox('Select Categorical Column for Count Plot',
                                               df.select_dtypes(include='object').columns)
                if categorical_col:
                    fig = px.histogram(df, x=categorical_col, title=f'Count Plot for {categorical_col}')
                    st.plotly_chart(fig)

                # Pair plot for numerical columns
                st.write("### Pair Plot for Numerical Columns")
                pair_plot_cols = st.multiselect('Select Numerical Columns for Pair Plot', numerical_cols)
                if pair_plot_cols:
                    pair_plot_df = df[pair_plot_cols]
                    fig = px.scatter_matrix(pair_plot_df)
                    st.plotly_chart(fig)


if __name__ == "__main__":
    main()
