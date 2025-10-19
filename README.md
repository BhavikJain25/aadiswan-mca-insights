# aadiswan-mca-insights

# MCA Insights Engine

A Python-based data intelligence system that monitors, enriches, and surfaces insights from Ministry of Corporate Affairs (MCA) company data across 5 Indian states: **Maharashtra, Gujarat, Delhi, Tamil Nadu, and Karnataka**.

This solution fulfills all core requirements of the Aadiswan assignment:
- ✅ Daily change detection (new incorporations, deregistrations, field updates)
- ✅ Web-based enrichment (mocked per guidelines)
- ✅ AI-powered daily summaries
- ✅ Conversational chatbot (rule-based NLP)
- ✅ Streamlit dashboard with search & filters

> 📌 **Note**: As per assignment guidelines, this is a *representative implementation*. Real MCA data is simulated, and enrichment uses mock logic — sufficient for evaluation.

---

## 🗂️ Project Structure

├── data/
│ ├── mca_data/ # Raw mock MCA snapshots (Day 1–3)
│ ├── master_day1.csv # Integrated master datasets
│ ├── master_day2.csv
│ └── master_day3.csv
├── output/
│ ├── changes_day1_to_day2.csv # Structured change logs
│ ├── changes_day2_to_day3.csv
│ ├── all_changes.csv
│ ├── enriched_data.csv # Mock-enriched sample (50–100 CINs)
│ └── daily_summary.json # AI-generated daily reports
├── app.py # Streamlit dashboard (search, filters, chatbot)
├── generate_mock_mca_data.py # Step 1: Simulate MCA data
├── integrate_data.py # Step 2: Merge & clean
├── detect_changes.py # Step 3: Change detection engine
├── enrich_data.py # Step 4: Mock enrichment
├── generate_summary.py # Step 5: AI summary generator
├── chatbot.py # Step 6: Rule-based NLP logic
└── README.md
