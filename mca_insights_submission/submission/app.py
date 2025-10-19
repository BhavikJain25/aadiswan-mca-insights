
import streamlit as st
import pandas as pd
import json
import re
from datetime import datetime

# ----------------------------
# Load Data
# ----------------------------
@st.cache_data
def load_data():
    master = pd.read_csv("master_day3.csv")
    changes = pd.read_csv("all_changes.csv")
    enriched = pd.read_csv("enriched_data.csv")
    with open("daily_summary.json", "r") as f:
        summaries = json.load(f)
    return master, changes, enriched, summaries

master_df, all_changes, enriched_df, daily_summaries = load_data()

# Ensure CIN is string
master_df["CIN"] = master_df["CIN"].astype(str)
all_changes["CIN"] = all_changes["CIN"].astype(str)

# ----------------------------
# Chatbot Logic (from Step 6)
# ----------------------------
def chatbot_response(query):
    query = query.lower().strip()
    if "new incorporation" in query or ("new" in query and "incorporation" in query):
        state_map = {
            "maharashtra": "Maharashtra",
            "gujarat": "Gujarat",
            "delhi": "Delhi",
            "tamil": "Tamil Nadu",
            "nadu": "Tamil Nadu",
            "karnataka": "Karnataka"
        }
        state_filter = None
        for kw, state in state_map.items():
            if kw in query:
                state_filter = state
                break
        
        new_cins = all_changes[all_changes["Change_Type"] == "New Incorporation"]["CIN"].tolist()
        if state_filter:
            filtered = master_df[
                (master_df["CIN"].isin(new_cins)) & 
                (master_df["State"] == state_filter)
            ][["CIN", "Company Name"]]
            if not filtered.empty:
                result = f"✅ Found {len(filtered)} new incorporations in {state_filter}:\n\n"
                for _, row in filtered.head(5).iterrows():
                    result += f"- **{row['Company Name']}** (`{row['CIN']}`)\n"
                return result
            else:
                return f"❌ No new incorporations found in {state_filter}."
        else:
            count = len(new_cins)
            return f"📊 Total new incorporations: **{count}**"

    elif "struck off" in query or "deregister" in query or "strike off" in query:
        count = len(all_changes[all_changes["Change_Type"] == "Deregistered/Struck Off"])
        return f"🗑️ Companies struck off/deregistered: **{count}**"

    elif "capital" in query and ("above" in query or "greater" in query):
        lakh_match = re.search(r'(\d+)\s*lakh', query)
        if lakh_match:
            min_cap = int(lakh_match.group(1)) * 100000
        else:
            num_match = re.search(r'(\d{5,})', query)
            min_cap = int(num_match.group(1)) if num_match else 1000000
        
        high_cap = master_df[master_df["Authorized Capital"] > min_cap][["Company Name", "Authorized Capital"]]
        if not high_cap.empty:
            result = f"💰 Found {len(high_cap)} companies with capital > ₹{min_cap:,}:\n\n"
            for _, row in high_cap.head(5).iterrows():
                result += f"- **{row['Company Name']}** (₹{int(row['Authorized Capital']):,})\n"
            return result
        else:
            return f"❌ No companies found with capital > ₹{min_cap:,}."

    else:
        return (
            "🤖 Try these examples:\n\n"
            "- *Show new incorporations in Maharashtra*\n"
            "- *How many companies were struck off?*\n"
            "- *List companies with capital above 10 lakh*"
        )

# ----------------------------
# Streamlit App
# ----------------------------
st.set_page_config(page_title="MCA Insights Engine", layout="wide")
st.title("🔍 MCA Insights Engine")
st.markdown("Track company changes across Maharashtra, Gujarat, Delhi, Tamil Nadu & Karnataka")

# Sidebar Filters
st.sidebar.header("Filters")
states = ["All"] + sorted(master_df["State"].dropna().unique().tolist())
selected_state = st.sidebar.selectbox("State", states)
statuses = ["All"] + sorted(master_df["Company Status"].dropna().unique().tolist())
selected_status = st.sidebar.selectbox("Company Status", statuses)

# Search
search_query = st.text_input("🔍 Search by CIN or Company Name")

# Filter data
filtered_df = master_df.copy()
if selected_state != "All":
    filtered_df = filtered_df[filtered_df["State"] == selected_state]
if selected_status != "All":
    filtered_df = filtered_df[filtered_df["Company Status"] == selected_status]
if search_query:
    filtered_df = filtered_df[
        filtered_df["CIN"].str.contains(search_query, case=False, na=False) |
        filtered_df["Company Name"].str.contains(search_query, case=False, na=False)
    ]

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["📊 Dashboard", "📈 Change History", "🧩 Enriched Data", "💬 Chat with Data"])

# Tab 1: Dashboard
with tab1:
    st.subheader("Company Records")
    st.dataframe(filtered_df[[
        "CIN", "Company Name", "State", "Company Status", 
        "Authorized Capital", "Paid Up Capital", "Principal Business Activity"
    ]].head(20), use_container_width=True)

# Tab 2: Change History
with tab2:
    st.subheader("Daily Change Trends")
    change_counts = all_changes.groupby(["Date", "Change_Type"]).size().unstack(fill_value=0)
    st.bar_chart(change_counts)

# Tab 3: Enriched Data
with tab3:
    st.subheader("Enriched Company Info (Sample)")
    enriched_sample = enriched_df.head(15)
    st.dataframe(enriched_sample, use_container_width=True)

# Tab 4: Chatbot
with tab4:
    st.subheader("Ask Questions in Natural Language")
    user_input = st.text_input("💬 Type your query below:")
    if user_input:
        response = chatbot_response(user_input)
        st.markdown(response)

# Show latest AI Summary
latest_summary = daily_summaries["summaries"][-1]["summary"]
st.sidebar.markdown("### 📰 Latest AI Summary")
st.sidebar.text(latest_summary)
