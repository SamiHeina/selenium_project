import os
import time
import pytest
from pages.login_page import LoginPage
from pages.jobs_page import JobsPage
from pages.apply_page import ApplyPage

def test_full_demo(driver):
    file_path = os.path.abspath("demo_site/index.html")
    driver.get(f"file:///{file_path}")

    login = LoginPage(driver)
    login.login("demo", "demo")

    jobs = JobsPage(driver)
    jobs.open_job(0)

    apply = ApplyPage(driver)
    apply.click_apply()

    time.sleep(2)

    confirmation = driver.find_element(*apply.confirmation_msg)
    assert confirmation.is_displayed(), "Application confirmation is not displayed"

    print("✅ Full demo complete! Browser will close in 5 seconds...")
    time.sleep(5)

