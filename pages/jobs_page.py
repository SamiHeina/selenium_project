from selenium.webdriver.common.by import By

class JobsPage:
    def __init__(self, driver):
        self.driver = driver
        self.job_links = (By.CLASS_NAME, "job")
        self.jobs_section = (By.ID, "jobs-section")

    def open_job(self, index=0):
        jobs = self.driver.find_elements(*self.job_links)
        if not jobs:
            print("⚠️ No jobs found")
            return
        jobs[index].click()




