import streamlit as st

# Initialize connection.

conn = st.connection(**st.secrets["snowflake"])

# Perform query.
df = conn.query("SELECT * from WATCHTOWER_STATIONS_TBL;", ttl=600)

# Print results.
for row in df.itertuples():
    st.write(f"{row.ID} has a :{row.ORGANIZATIONUNITID}:")
