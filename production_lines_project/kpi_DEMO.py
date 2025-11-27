import pandas as pd # type: ignore
from tabulate import tabulate # type: ignore
import numpy as np # type: ignore
import pyodbc # type: ignore
import os # type: ignore
import sys

#**************************************************************************************************************************
#                                                Function: create_db_connection()   
#**************************************************************************************************************************


def create_db_connection():
    '''
    Function: create_db_connection
    ------------------------------
    Establishes a connection to a Microsoft SQL Server database.

    Connection Parameters:
        SERVER   : SQL Server instance ('DESKTOP-8QSTOS0')
        DATABASE : Database name ('production_lines_db')
        USERNAME : Username for authentication ('sa')
        PASSWORD : Password for authentication ('SQL_Pass')

    Returns:
        conn : pyodbc connection object to interact with the SQL Server.
    '''
    SERVER = 'DESKTOP-8QSTOS0'
    DATABASE = 'test'
    USERNAME = 'sa'
    PASSWORD = 'SQL_Pass'

    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'

    # Establish the connection
    conn = pyodbc.connect(connectionString)
    print("[DB] Connection successful")

    return conn



#**************************************************************************************************************************
#                                                KPI Functions   
#**************************************************************************************************************************

#  KPI 1
def get_kpi_1(df: pd.DataFrame) -> pd.DataFrame:

	'''
    Function: get_kpi_1
    ------------------------------
    Computes KPI 1 (production_line: gr-np-47: start_timestamp - stop_timestamp - duration)

    Parameters:
    	df   : pandas dataframe object
        
    Returns:
        result : pandas dataframe object
    '''
	
	# Apply filtering based on the production_line_id
	kpi_1_df = df[(df['production_line_id'] == 'gr-np-47') & (session_data['working_status'] == 1)]
	kpi_1_df = kpi_1_df[['production_line_id', 'start_timestamp', 'stop_timestamp', 'duration']]


	# Return the result
	return kpi_1_df



# ------------------------------------------------------------------------------------------------------------------------



#  KPI 2
def get_kpi_2(df: pd.DataFrame) -> pd.DataFrame:

	'''
    Function: get_kpi_2
    ------------------------------
    Computes KPI 2 (Total Uptime - Downtime of the whole production floor)

    Parameters:
    	df   : pandas dataframe object
        
    Returns:
        result : pandas dataframe object
    '''

	# Group by working_status and apply SUM() on duration column
	kpi_2_df = df.groupby('working_status')['duration'].sum().reset_index()

	# Replace working_status boolean values with the respective ones
	kpi_2_df['working_status'] = kpi_2_df['working_status'].replace({True: 'Uptime', False: 'Downtime'})


	# Return the result
	return kpi_2_df



# ------------------------------------------------------------------------------------------------------------------------



#  KPI 3
def get_kpi_3(df: pd.DataFrame) -> pd.DataFrame:

	'''
    Function: get_kpi_3
    ------------------------------
    Computes KPI 3 (production line with the maximum downtime value and dowtime value itself)

    Parameters:
    	df   : pandas dataframe object
        
    Returns:
        result : pandas dataframe object
    '''

    # Keep only downtime data
	kpi_3_df = df[df['working_status'] == 0]

	# Group py production_line_id and apply SUM() on duration column
	kpi_3_df = kpi_3_df.groupby('production_line_id')['duration'].sum().reset_index()


	# Sort in descending order by duration column and keep only the first row
	kpi_3_df = kpi_3_df.sort_values(by='duration', ascending=False).head(1)


	# Rename the duration column to MAX downtime
	kpi_3_df.columns = ['production_line_id', 'MAX dowtime']


	# Return the result
	return kpi_3_df



# ------------------------------------------------------------------------------------------------------------------------




#**************************************************************************************************************************
#                                                     Main SCRIPT  
#**************************************************************************************************************************
''' 
Call the create_db_connection() function to establish a connection to SQL Server and retrieve the new Complaints.

Query Returns:

'''
# Establish the connection
try:
    # Create connection
    conn = create_db_connection()

    # Create a cursor to execute queries
    cursor = conn.cursor()
    
    query = """
                            SELECT *
                            FROM [production_lines_db].[dbo].[session_table] 
                            """

    # Execute query
    cursor.execute(query)

    # Fetch session_table data
    session_table = cursor.fetchall()

except pyodbc.Error as e:
    print("Error:", e)
    sys.exit(1) # terminate program

finally:
    # Close the cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
        print("[DB] Connection closed\n")





#**************************************************************************************************************************
''' 
Check whether session_table has data:
    1. Terminate the process if session_table is empty.
    2. Create a dataframe containing all the session_table rows, otherwise.
'''
#**************************************************************************************************************************

if len(session_table) == 0:
    print("[LOG] session_table is empty\n\n")

else:
    session_data = pd.DataFrame(np.array(session_table), columns=['session_id', 'production_line_id', 'start_timestamp', 'stop_timestamp', 'duration', 'working_status'])
    print(tabulate(session_data.head(1000), headers='keys'))

    """
    Execution example:

  			  session_id  production_line_id    start_timestamp      stop_timestamp         duration  working_status
		--  ------------  -----------------  -------------------  -------------------  ----------  ----------------
		 0             4  gr-np-47           2020-10-07 01:33:20  2020-10-07 02:03:20        1800  True
		 1             5  gr-np-47           2020-10-07 02:03:20  2020-10-07 02:15:02         702  False
		 2             6  gr-np-47           2020-10-07 02:15:02  2020-10-07 04:15:02        7200  True
		 3             7  gr-np-47           2020-10-07 04:15:02  2020-10-07 05:00:00        2698  False
		 4             8  gr-np-47           2020-10-07 05:00:00  2020-10-07 05:55:17        3317  True
		 5            15  gr-np-22           2020-10-07 03:05:02  2020-10-07 06:01:00       10558  True
 		 6            16  gr-np-22           2020-10-07 06:01:00  2020-10-07 06:11:00         600  False
 		 7            17  gr-np-22           2020-10-07 06:11:00  2020-10-07 07:11:00        3600  True

    """

    print("\n\n")

    #  KPI 1

    #  Call the get_kpi_1() function
    print(tabulate(get_kpi_1(session_data), headers='keys'))
    """
    Execution Example:

		    start_timestamp      stop_timestamp         duration
		--  -------------------  -------------------  ----------
		 0  2020-10-07 01:33:20  2020-10-07 02:03:20        1800
		 2  2020-10-07 02:15:02  2020-10-07 04:15:02        7200
		 4  2020-10-07 05:00:00  2020-10-07 05:55:17        3317
    """



    print("\n\n")


    #  KPI 2

    #  Call the get_kpi_2() function
    print(tabulate(get_kpi_2(session_data), headers='keys'))
    """
    Execution Example:

		    working_status      duration
		--  ----------------  ----------
		 0  Downtime                4000
		 1  Uptime                 	2647
    """





    print("\n\n")



    #  KPI 3

    #  Call the get_kpi_3() function
    print(tabulate(get_kpi_3(session_data), headers='keys'))
    """
    Execution Example:

            production_line_id      MAX dowtime
        --  --------------------  -------------
        1  gr-np-47                       3400
		    
    """


