import streamlit as st

from snowflake.snowpark import Session

from secrets import SNOWFLAKE_ACCOUNT, SNOWFLAKE_USER, SNOWFLAKE_PASSWORD

session = Session(url=st.secrets["SNOWFLAKE_ACCOUNT"], user=st.secrets["SNOWFLAKE_USER"], password=st.secrets["SNOWFLAKE_PASSWORD"])

df = session.sql("select * from JAMF_DEVICE_INFO.PUBLIC.WATCHTOWER_STATIONS_TBL").to_pandas()

st.write(df)

# Perform query.
#df = conn.query("SELECT * from WATCHTOWER_STATIONS_TBL;", ttl=600)

# Print results.
#for row in df.itertuples():
    #st.write(f"{row.ID} has a :{row.ORGANIZATIONUNITID}:")
