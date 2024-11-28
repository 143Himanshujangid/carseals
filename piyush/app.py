import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the dataset
file_path = 'UserCarData.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Set plot style
sns.set(style="whitegrid")

# Function to generate visualizations
def generate_visualizations(question):
    if question == "Distribution of Car Sales by Fuel Type":
        fuel_counts = data['fuel'].value_counts()
        plt.figure(figsize=(8, 5))
        sns.barplot(x=fuel_counts.index, y=fuel_counts.values, palette="viridis")
        plt.title('Distribution of Car Sales by Fuel Type', fontsize=16)
        plt.xlabel('Fuel Type', fontsize=12)
        plt.ylabel('Number of Cars Sold', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)
    
    elif question == "Average Selling Price by Fuel Type":
        avg_selling_price = data.groupby('fuel')['selling_price'].mean().sort_values()
        plt.figure(figsize=(8, 5))
        sns.barplot(x=avg_selling_price.index, y=avg_selling_price.values, palette="coolwarm")
        plt.title('Average Selling Price by Fuel Type', fontsize=16)
        plt.xlabel('Fuel Type', fontsize=12)
        plt.ylabel('Average Selling Price', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)
    
    elif question == "Top 10 Most Sold Car Models":
        top_models = data['name'].value_counts().head(10)
        plt.figure(figsize=(8, 5))
        sns.barplot(x=top_models.values, y=top_models.index, palette="magma")
        plt.title('Top 10 Most Sold Car Models', fontsize=16)
        plt.xlabel('Number of Cars Sold', fontsize=12)
        plt.ylabel('Car Model', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)

    elif question == "Year-wise Distribution of Cars Sold":
        year_counts = data['year'].value_counts().sort_index()
        plt.figure(figsize=(8, 5))
        sns.lineplot(x=year_counts.index, y=year_counts.values, marker="o", color="green")
        plt.title('Year-wise Distribution of Cars Sold', fontsize=16)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Number of Cars Sold', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)
    
    elif question == "Average Mileage by Transmission Type":
        avg_mileage = data.groupby('transmission')['mileage'].mean()
        plt.figure(figsize=(8, 5))
        sns.barplot(x=avg_mileage.index, y=avg_mileage.values, palette="cool")
        plt.title('Average Mileage by Transmission Type', fontsize=16)
        plt.xlabel('Transmission Type', fontsize=12)
        plt.ylabel('Average Mileage', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)

    elif question == "Correlation Between Engine Size and Selling Price":
        plt.figure(figsize=(8, 5))
        sns.scatterplot(x=data['engine'], y=data['selling_price'], alpha=0.6, color="purple")
        plt.title('Correlation Between Engine Size and Selling Price', fontsize=16)
        plt.xlabel('Engine Size (CC)', fontsize=12)
        plt.ylabel('Selling Price', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)

    elif question == "Number of Cars Sold by Region":
        region_counts = data['Region'].value_counts()
        plt.figure(figsize=(8, 5))
        sns.barplot(x=region_counts.index, y=region_counts.values, palette="husl")
        plt.title('Number of Cars Sold by Region', fontsize=16)
        plt.xlabel('Region', fontsize=12)
        plt.ylabel('Number of Cars Sold', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)

    elif question == "State with the Most Car Sales":
        state_counts = data['State or Province'].value_counts().head(10)
        plt.figure(figsize=(8, 5))
        sns.barplot(y=state_counts.index, x=state_counts.values, palette="plasma")
        plt.title('State with the Most Car Sales', fontsize=16)
        plt.xlabel('Number of Cars Sold', fontsize=12)
        plt.ylabel('State', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)

    elif question == "Most Popular Transmission Type":
        trans_counts = data['transmission'].value_counts()
        plt.figure(figsize=(8, 5))
        sns.barplot(x=trans_counts.index, y=trans_counts.values, palette="muted")
        plt.title('Most Popular Transmission Type', fontsize=16)
        plt.xlabel('Transmission Type', fontsize=12)
        plt.ylabel('Number of Cars Sold', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)

    elif question == "Distribution of Cars by Owner Type":
        owner_counts = data['owner'].value_counts()
        plt.figure(figsize=(8, 5))
        sns.barplot(x=owner_counts.index, y=owner_counts.values, palette="cividis")
        plt.title('Distribution of Cars by Owner Type', fontsize=16)
        plt.xlabel('Owner Type', fontsize=12)
        plt.ylabel('Number of Cars Sold', fontsize=12)
        plt.tight_layout()
        st.pyplot(plt)

    # Add more questions and visualizations here...

# Streamlit App
st.title("Car Sales Data Analysis")
st.sidebar.title("Select a Question")

# Dropdown with questions
questions = [
    "Distribution of Car Sales by Fuel Type",
    "Average Selling Price by Fuel Type",
    "Top 10 Most Sold Car Models",
    "Year-wise Distribution of Cars Sold",
    "Average Mileage by Transmission Type",
    "Correlation Between Engine Size and Selling Price",
    "Number of Cars Sold by Region",
    "State with the Most Car Sales",
    "Most Popular Transmission Type",
    "Distribution of Cars by Owner Type",
    # Add remaining questions here...
]

selected_question = st.sidebar.selectbox("Choose a Question to Visualize", questions)

# Display visualization based on the selected question
st.subheader(selected_question)
generate_visualizations(selected_question)
