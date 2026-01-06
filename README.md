JOB PORTAL AUTOMATION PROJECT
Automated Selenium + Python project simulating user interactions on a demo job portal. Tests include login, job browsing, and applying, with live browser interaction and HTML reports.

Structure:
selenium_project/
├── demo_site/ # HTML demo website
├── pages/ # Page Object Model files
│ ├── login_page.py
│ ├── jobs_page.py
│ └── apply_page.py
├── tests/ # Test scripts
│ └── test_full_demo.py
├── reports/ # HTML test reports
├── conftest.py # pytest fixtures
├── requirements.txt # Dependencies
└── README.md

1. Clone repo: 
git clone https://github.com/SamiHeina/selenium_project.git
cd selenium_project

2. Create & activate virtual environment:
python -m venv selenium_env
# Windows
selenium_env\Scripts\activate
# macOS/Linux
source selenium_env/bin/activate

3. Install dependencies:
pip install -r requirements.txt

4. Run: 
pytest -s tests/ --html=reports/report.html
