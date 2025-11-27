import pandas as pd

# ------------------------------------------------------------------------------------------------------------------------

# KPI 1
def get_kpi_1(df: pd.DataFrame) -> pd.DataFrame:
	'''
    Function: get_kpi_1
    ------------------------------
    Computes KPI 1 (production_line: gr-np-47: start_timestamp - stop_timestamp - duration)

    Parameters:
    	df : pandas dataframe object
        
    Returns:
        result : pandas dataframe object
    '''
	
	# Apply filtering based on the production_line_id
	kpi_1_df = df[(df['production_line_id'] == 'gr-np-47') & (df['working_status'] == 1)]
	kpi_1_df = kpi_1_df[['production_line_id', 'start_timestamp', 'stop_timestamp', 'duration']]


	# Return the result
	return kpi_1_df

# ------------------------------------------------------------------------------------------------------------------------

# KPI 2
def get_kpi_2(df: pd.DataFrame) -> pd.DataFrame:
	'''
    Function: get_kpi_2
    ------------------------------
    Computes KPI 2 (Total Uptime - Downtime of the whole production floor)

    Parameters:
    	df : pandas dataframe object
        
    Returns:
        result : pandas dataframe object
    '''

	# Group by working_status and apply SUM() on duration column
	kpi_2_df = df.groupby('working_status')['duration'].sum().reset_index()

	# Replace working_status boolean values with the respective ones
	# Assuming working_status is 1 for Uptime and 0 for Downtime, or True/False.
	kpi_2_df['working_status'] = kpi_2_df['working_status'].replace({1: 'Uptime', 0: 'Downtime', True: 'Uptime', False: 'Downtime'})


	# Return the result
	return kpi_2_df

# ------------------------------------------------------------------------------------------------------------------------

# KPI 3
def get_kpi_3(df: pd.DataFrame) -> pd.DataFrame:
	'''
    Function: get_kpi_3
    ------------------------------
    Computes KPI 3 (production line with the maximum downtime value and dowtime value itself)

    Parameters:
    	df : pandas dataframe object
        
    Returns:
        result : pandas dataframe object
    '''

    # Keep only downtime data
	# Assuming working_status = 0 means Downtime
	kpi_3_df = df[df['working_status'] == 0]

	# Group py production_line_id and apply SUM() on duration column
	kpi_3_df = kpi_3_df.groupby('production_line_id')['duration'].sum().reset_index()


	# Sort in descending order by duration column and keep only the first row
	kpi_3_df = kpi_3_df.sort_values(by='duration', ascending=False).head(1)


	# Rename the duration column to MAX downtime
	kpi_3_df.columns = ['production_line_id', 'MAX downtime']


	# Return the result
	return kpi_3_df