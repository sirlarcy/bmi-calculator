# # import streamlit as st

# # def calculate_bmi(weight, height):
# #     """Calculates BMI based on weight (in kg) and height (in cm)."""
# #     try:
# #         # Convert height from cm to meters for BMI calculation
# #         height_meters = height / 100
# #         bmi = weight / (height_meters ** 2)
# #         return bmi
# #     except ZeroDivisionError:
# #         st.error("Error: Height cannot be zero.")
# #     except ValueError:
# #         st.error("Error: Please enter valid numeric values for weight and height.")

# # def main():
# #     st.title("BMI Calculator")
# #     name = st.text_input('Enter your name: ')
# #     weight = st.number_input("Enter your weight in kg", min_value=0.0, step=0.1)
# #     height = st.number_input("Enter your height in cm", min_value=0.0, step=0.01)

# #     if st.button("Calculate BMI"):
# #         bmi = calculate_bmi(weight, height)
# #         if bmi is not None:
# #             st.write(f"Hi {name}. Your BMI is: {bmi:.2f}")
# #             if bmi < 18.5:
# #                 st.write("Category: Underweight")
# #             elif bmi < 25:
# #                 st.write("Category: Normal weight")
# #             elif bmi < 30:
# #                 st.write("Category: Overweight")
# #             else:
# #                 st.write("Category: Obesity")

# # if __name__ == "__main__":
# #     main()

# # import streamlit as st
# # import sqlite3

# # # Function to calculate BMI
# # def calculate_bmi(weight, height):
# #     """Calculates BMI based on weight (in kg) and height (in meters)."""
# #     bmi = weight / (height ** 2)
# #     return bmi

# # # Function to retrieve user names from the database
# # def get_user_names():
# #     try:
# #         conn = sqlite3.connect('bmi_data.db')
# #         c = conn.cursor()
# #         c.execute("SELECT DISTINCT user_name FROM bmi_records")
# #         user_names = [row[0] for row in c.fetchall()]
# #         conn.close()
# #         return user_names
# #     except sqlite3.Error as e:
# #         st.error(f"SQLite error: {e}")
# #         return []

# # # Function to retrieve historical data based on selected user
# # def get_historical_data(selected_user):
# #     try:
# #         conn = sqlite3.connect('bmi_data.db')
# #         c = conn.cursor()
# #         if selected_user and selected_user != "ALL USERS":
# #             c.execute("SELECT * FROM bmi_records WHERE user_name=? ORDER BY timestamp DESC LIMIT 10", (selected_user,))
# #         else:
# #             c.execute("SELECT * FROM bmi_records ORDER BY timestamp DESC LIMIT 10")
# #         rows = c.fetchall()
# #         conn.close()
# #         return rows
# #     except sqlite3.Error as e:
# #         st.error(f"SQLite error: {e}")
# #         return []

# # # Create the Streamlit app
# # st.title("BMI Calculator")

# # # Get user input for weight and height
# # weight = st.number_input("Enter your weight in kg", min_value=0.0, step=0.1)
# # height = st.number_input("Enter your height in meters", min_value=0.0, step=0.01)

# # # Calculate BMI
# # if st.button("Calculate BMI"):
# #     bmi = calculate_bmi(weight, height)
# #     st.write(f"Your BMI is: {bmi:.2f}")

# #     category = ""
# #     if bmi < 18.5:
# #         category = "Underweight"
# #     elif 18.5 <= bmi < 25:
# #         category = "Normal weight"
# #     elif 25 <= bmi < 30:
# #         category = "Overweight"
# #     else:
# #         category = "Obesity"

# #     st.write(f"Category: {category}")

# #     # Retrieve user names from the database and update dropdown
# #     user_names = get_user_names()
# #     selected_user = st.selectbox("Select User:", ["ALL USERS"] + user_names)
    
# #     # Display historical data based on selected user
# #     historical_data = get_historical_data(selected_user)
# #     if historical_data:
# #         st.write("Historical Data:")
# #         st.table(historical_data)
# #     else:
# #         st.info("No historical data found.")


# # import streamlit as st
# # import sqlite3
# # import pandas as pd
# # from datetime import datetime

# # # Function to create a connection to the SQLite database
# # def create_connection(db_file):
# #     try:
# #         conn = sqlite3.connect(db_file)
# #         return conn
# #     except sqlite3.Error as e:
# #         st.error(f"SQLite error: {e}")
# #         return None

# # # Function to create the BMI records table
# # def create_table(conn):
# #     try:
# #         c = conn.cursor()
# #         c.execute('''CREATE TABLE IF NOT EXISTS bmi_records
# #                      (id INTEGER PRIMARY KEY, name TEXT, weight REAL, height REAL, bmi REAL, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
# #     except sqlite3.Error as e:
# #         st.error(f"SQLite error: {e}")

# # # Function to insert BMI record into the database
# # def insert_bmi_record(conn, name, weight, height, bmi):
# #     try:
# #         c = conn.cursor()
# #         c.execute("INSERT INTO bmi_records (name, weight, height, bmi) VALUES (?, ?, ?, ?)", (name, weight, height, bmi))
# #         conn.commit()
# #     except sqlite3.Error as e:
# #         st.error(f"SQLite error: {e}")

# # # Function to calculate BMI
# # def calculate_bmi(weight, height):
# #     try:
# #         # Convert height from cm to meters for BMI calculation
# #         height_meters = height / 100
# #         bmi = weight / (height_meters ** 2)
# #         return bmi
# #     except ZeroDivisionError:
# #         st.error("Error: Height cannot be zero.")
# #         return None
# #     except ValueError:
# #         st.error("Error: Please enter valid numeric values for weight and height.")
# #         return None

# # # Function to fetch BMI records from the database
# # def fetch_bmi_records(conn):
# #     try:
# #         c = conn.cursor()
# #         c.execute("SELECT name, weight, height, bmi, timestamp FROM bmi_records ORDER BY id DESC LIMIT 10")
# #         rows = c.fetchall()
# #         return rows
# #     except sqlite3.Error as e:
# #         st.error(f"SQLite error: {e}")
# #         return []

# # # Function to initialize session state and widgets
# # def initialize_session():
# #     if 'name_input' not in st.session_state:
# #         st.session_state.name_input = ""
# #     if 'weight_input' not in st.session_state:
# #         st.session_state.weight_input = 0.0
# #     if 'height_input' not in st.session_state:
# #         st.session_state.height_input = 0.0

# # # Main function
# # def main():
# #     # Create or connect to the SQLite database
# #     conn = create_connection('bmi_data.db')
# #     if conn is not None:
# #         # Create BMI records table if not exists
# #         create_table(conn)

# #         # Initialize session state and widgets
# #         initialize_session()

# #         # Streamlit interface
# #         st.title("BMI Calculator")
# #         st.session_state.name_input = st.text_input('Enter your name:', st.session_state.name_input)
# #         st.session_state.weight_input = st.number_input("Enter your weight in kg", min_value=0.0, step=0.1, value=st.session_state.weight_input)
# #         st.session_state.height_input = st.number_input("Enter your height in cm", min_value=0.0, step=0.01, value=st.session_state.height_input)

# #         col1, col2 = st.columns(2)
# #         if col1.button("Calculate BMI"):
# #             bmi = calculate_bmi(st.session_state.weight_input, st.session_state.height_input)
# #             if bmi is not None:
# #                 st.write(f"Hi {st.session_state.name_input}. Your BMI is: {bmi:.2f}")
# #                 if bmi < 18.5:
# #                     st.write("Category: Underweight")
# #                 elif bmi < 25:
# #                     st.write("Category: Normal weight")
# #                 elif bmi < 30:
# #                     st.write("Category: Overweight")
# #                 else:
# #                     st.write("Category: Obesity")
                
# #                 # Insert BMI record into the database
# #                 insert_bmi_record(conn, st.session_state.name_input, st.session_state.weight_input, st.session_state.height_input, bmi)

# #                 # Fetch and display BMI records
# #                 st.header("Recent BMI Records")
# #                 records = fetch_bmi_records(conn)
# #                 if records:
# #                     # Extract column names from the first row of the records
# #                     headers = ["Name", "Weight (kg)", "Height (cm)", "BMI", "Timestamp"]
# #                     # Display the table with headers
# #                     st.write(pd.DataFrame(records, columns=headers))
# #                 else:
# #                     st.info("No records found.")

# #         if col2.button("Clear Fields"):
# #             st.session_state.name_input = ""
# #             st.session_state.weight_input = 0.0
# #             st.session_state.height_input = 0.0

# #         # Close the database connection
# #         conn.close()
# #     else:
# #         st.error("Error: Unable to connect to the database.")

# # if __name__ == "__main__":
# #     main()

# import streamlit as st
# import sqlite3
# import pandas as pd
# from datetime import datetime

# # Function to create a connection to the SQLite database
# def create_connection(db_file):
#     try:
#         conn = sqlite3.connect(db_file)
#         return conn
#     except sqlite3.Error as e:
#         st.error(f"SQLite error: {e}")
#         return None

# # Function to create the BMI records table
# def create_table(conn):
#     try:
#         c = conn.cursor()
#         c.execute('''CREATE TABLE IF NOT EXISTS bmi_records
#                      (id INTEGER PRIMARY KEY, name TEXT, weight REAL, height REAL, bmi REAL, timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
#     except sqlite3.Error as e:
#         st.error(f"SQLite error: {e}")

# # Function to insert BMI record into the database
# def insert_bmi_record(conn, name, weight, height, bmi):
#     try:
#         c = conn.cursor()
#         c.execute("INSERT INTO bmi_records (name, weight, height, bmi) VALUES (?, ?, ?, ?)", (name, weight, height, bmi))
#         conn.commit()
#     except sqlite3.Error as e:
#         st.error(f"SQLite error: {e}")

# # Function to calculate BMI
# def calculate_bmi(weight, height):
#     try:
#         # Convert height from cm to meters for BMI calculation
#         height_meters = height / 100
#         bmi = weight / (height_meters ** 2)
#         return bmi
#     except ZeroDivisionError:
#         st.error("Error: Height cannot be zero.")
#         return None
#     except ValueError:
#         st.error("Error: Please enter valid numeric values for weight and height.")
#         return None

# # Function to fetch BMI records from the database
# def fetch_bmi_records(conn):
#     try:
#         c = conn.cursor()
#         c.execute("SELECT name, weight, height, bmi, timestamp FROM bmi_records ORDER BY id DESC LIMIT 10")
#         rows = c.fetchall()
#         return rows
#     except sqlite3.Error as e:
#         st.error(f"SQLite error: {e}")
#         return []

# # Function to initialize session state and widgets
# def initialize_session():
#     if 'name_input' not in st.session_state:
#         st.session_state.name_input = ""
#     if 'weight_input' not in st.session_state:
#         st.session_state.weight_input = 0.0
#     if 'height_input' not in st.session_state:
#         st.session_state.height_input = 0.0

# # Main function
# def main():
#     # Create or connect to the SQLite database
#     conn = create_connection('bmi_data.db')
#     if conn is not None:
#         # Create BMI records table if not exists
#         create_table(conn)

#         # Initialize session state and widgets
#         initialize_session()

#         # Streamlit interface
#         st.title("BMI Calculator")
#         st.session_state.name_input = st.text_input('Enter your name:', st.session_state.name_input)
#         st.session_state.weight_input = st.number_input("Enter your weight in kg", min_value=0.0, step=0.1, value=st.session_state.weight_input)
#         st.session_state.height_input = st.number_input("Enter your height in cm", min_value=0.0, step=0.01, value=st.session_state.height_input)

#         col1, col2 = st.columns(2)
#         if col1.button("Calculate BMI"):
#             bmi = calculate_bmi(st.session_state.weight_input, st.session_state.height_input)
#             if bmi is not None:
#                 st.write(f"Hi {st.session_state.name_input}. Your BMI is: {bmi:.2f}")
#                 if bmi < 18.5:
#                     st.write("Category: Underweight")
#                 elif bmi < 25:
#                     st.write("Category: Normal weight")
#                 elif bmi < 30:
#                     st.write("Category: Overweight")
#                 else:
#                     st.write("Category: Obesity")
                
#                 # Insert BMI record into the database
#                 insert_bmi_record(conn, st.session_state.name_input, st.session_state.weight_input, st.session_state.height_input, bmi)

#         if col2.button("Clear Fields"):
#             st.session_state.name_input = ""
#             st.session_state.weight_input = 0.0
#             st.session_state.height_input = 0.0

#         # Fetch and display BMI records
#         st.header("Recent BMI Records")
#         records = fetch_bmi_records(conn)
#         if records:
#             # Extract column names from the first row of the records
#             headers = ["Name", "Weight (kg)", "Height (cm)", "BMI", "Timestamp"]
#             # Display the table with headers
#             df = pd.DataFrame(records, columns=headers)
#             df['Timestamp'] = pd.to_datetime(df['Timestamp'])
#             st.table(df)
#             # Display the scatter plot
#             st.subheader("Plot of BMI Over Time")
#             st.scatter_chart(df.set_index('Timestamp')['BMI'].rename('BMI Over Time'))
#         else:
#             st.info("No records found.")

#         # Close the database connection
#         conn.close()
#     else:
#         st.error("Error: Unable to connect to the database.")

# if __name__ == "__main__":
#     main()





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

