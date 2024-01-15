import streamlit as st

# Initialize connection.
conn = st.connection("snowpark")

# Perform query.
df = conn.query("SELECT * from JAMF_DEVICE_INFO.PUBLIC.WATCHTOWER_STATIONS_TBL;", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.ORGANIZATIONUNITNAME} has a :{row.LAST_UPDATED}:")
