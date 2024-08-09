import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime

# Function to create a connection to the SQLite database
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error as e:
        st.error(f"Error connecting to the database: {e}")
        return None

# Function to create the BMI records table
def create_table(conn):
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS bmi_records
                     (id INTEGER PRIMARY KEY, name TEXT, weight REAL, height REAL, bmi REAL, category TEXT, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    except sqlite3.Error as e:
        st.error(f"Error creating BMI records table: {e}")

# Function to insert BMI record into the database
def insert_bmi_record(conn, name, weight, height, bmi, category):
    try:
        c = conn.cursor()
        c.execute("INSERT INTO bmi_records (name, weight, height, bmi, category) VALUES (?, ?, ?, ?, ?)", (name, weight, height, bmi, category))
        conn.commit()
    except sqlite3.Error as e:
        st.error(f"Error inserting BMI record: {e}")

# Function to calculate BMI and category
def calculate_bmi(weight, height):
    try:
        # Convert height from cm to meters for BMI calculation
        height_meters = height / 100
        bmi = weight / (height_meters ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal weight"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        return bmi, category
    except ZeroDivisionError:
        st.error("Error: Height cannot be zero.")
        return None, None
    except ValueError:
        st.error("Error: Please enter valid numeric values for weight and height.")
        return None, None

# Function to fetch BMI records from the database
def fetch_bmi_records(conn, start_date=None, end_date=None, categories=None):
    query = "SELECT name, weight, height, bmi, category, timestamp FROM bmi_records WHERE 1=1"
    params = []

    if start_date:
        query += " AND timestamp >= ?"
        params.append(start_date)
    if end_date:
        query += " AND timestamp <= ?"
        params.append(end_date)
    if categories:
        query += " AND category IN ({seq})".format(seq=','.join(['?']*len(categories)))
        params.extend(categories)

    query += " ORDER BY id DESC LIMIT 10"
    try:
        c = conn.cursor()
        c.execute(query, params)
        rows = c.fetchall()
        return rows
    except sqlite3.Error as e:
        st.error(f"Error fetching BMI records: {e}")
        return []

# Function to initialize session state and widgets
def initialize_session():
    if 'name_input' not in st.session_state:
        st.session_state.name_input = ""
    if 'weight_input' not in st.session_state:
        st.session_state.weight_input = 0.0
    if 'height_input' not in st.session_state:
        st.session_state.height_input = 0.0

# Main function
def main():
    # Create or connect to the SQLite database
    conn = create_connection('bmi_data.db')
    if conn is not None:
        # Create BMI records table if not exists
        create_table(conn)

        # Initialize session state and widgets
        initialize_session()

        # Streamlit interface
        st.title("BMI Calculator")
        st.session_state.name_input = st.text_input('Enter your name:', st.session_state.name_input)
        st.session_state.weight_input = st.number_input("Enter your weight in kg", min_value=0.0, step=0.1, value=st.session_state.weight_input)
        st.session_state.height_input = st.number_input("Enter your height in cm", min_value=0.0, step=0.01, value=st.session_state.height_input)

        col1, col2 = st.columns(2)
        if col1.button("Calculate BMI"):
            bmi, category = calculate_bmi(st.session_state.weight_input, st.session_state.height_input)
            if bmi is not None and category is not None:
                st.write(f"Hi {st.session_state.name_input}. Your BMI is: {bmi:.2f}")
                st.write(f"Category: {category}")
                
                # Insert BMI record into the database
                insert_bmi_record(conn, st.session_state.name_input, st.session_state.weight_input, st.session_state.height_input, bmi, category)

        if col2.button("Clear Fields"):
            st.session_state.name_input = ""
            st.session_state.weight_input = 0.0
            st.session_state.height_input = 0.0

        # Date Range Picker
        st.header("Filter Records by Date Range")
        start_date = st.date_input("Start Date")
        end_date = st.date_input("End Date")

        # Category Filter
        st.header("Filter Records by Category")
        categories = st.multiselect("Select category:", ["Underweight", "Normal weight", "Overweight", "Obesity"])

        # Fetch and display BMI records
        st.header("Recent BMI Records")
        records = fetch_bmi_records(conn, start_date, end_date, categories)
        if records:
            # Extract column names from the first row of the records
            headers = ["Name", "Weight (kg)", "Height (cm)", "BMI", "Category", "Timestamp"]
            # Display the table with headers
            df = pd.DataFrame(records, columns=headers)
            df['Timestamp'] = pd.to_datetime(df['Timestamp'])
            st.table(df)
            # Display the scatter plot
            st.subheader("Plot of BMI Over Time")
            st.line_chart(df.set_index('Timestamp')['BMI'].rename('BMI Over Time'))
        else:
            st.info("No records found.")

        # Close the database connection
        conn.close()
    else:
        st.error("Unable to connect to the database.")

if __name__ == "__main__":
    main()

