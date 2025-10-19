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

```
|
├── data/                     ← Folder for processed data
│   ├── mca_data/             ← Subfolder: raw mock MCA snapshots (Day 1–3)
│   ├── master_day1.csv       ← File: integrated master dataset for Day 1
│   ├── master_day2.csv       ← File: integrated master dataset for Day 2
│   └── master_day3.csv       ← File: integrated master dataset for Day 3
|
├── output/                   ← Folder for generated outputs
│   ├── changes_day1_to_day2.csv  ← File: change log from Day 1 → Day 2
│   ├── changes_day2_to_day3.csv  ← File: change log from Day 2 → Day 3
│   ├── all_changes.csv       ← File: combined changes across all days
│   ├── enriched_data.csv     ← File: enriched sample (50–100 CINs)
│   └── daily_summary.json    ← File: AI-generated daily reports
|
├── app.py                    ← File: Streamlit dashboard (search, filters, chatbot)
|
├── generate_mock_mca_data.py ← File: Step 1 - Simulate MCA data
├── integrate_data.py         ← File: Step 2 - Merge & clean
├── detect_changes.py         ← File: Step 3 - Change detection engine
├── enrich_data.py            ← File: Step 4 - Mock enrichment
├── generate_summary.py       ← File: Step 5 - AI summary generator
├── chatbot.py                ← File: Step 6 - Rule-based NLP logic
|
└── README.md                 ← File: Project documentation

```




---



## 🚀 How to Run (Local Setup)

### Prerequisites
- Python 3.8+
- `pip install pandas streamlit`

### Steps
1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/mca-insights-engine.git
   cd mca-insights-engine

2. **Regenerate mock data**

```bash
python generate_mock_mca_data.py
python integrate_data.py
python detect_changes.py
python enrich_data.py
python generate_summary.py
   

   


