from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# === Automated Login Test ===
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Test cases for valid and invalid credentials
test_cases = [
    {"username": "student", "password": "Password123", "expected": "pass"},
    {"username": "wronguser", "password": "wrongpass", "expected": "fail"},
]

passed = 0
failed = 0

for case in test_cases:
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    driver.find_element(By.ID, "username").clear()
    driver.find_element(By.ID, "username").send_keys(case["username"])
    driver.find_element(By.ID, "password").clear()
    driver.find_element(By.ID, "password").send_keys(case["password"])
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)
    body_text = driver.find_element(By.TAG_NAME, "body").text

    if case["expected"] == "pass" and "Congratulations" in body_text:
        print(f"✅ Valid login PASSED for {case['username']}")
        passed += 1
    elif case["expected"] == "fail" and "Your username is invalid!" in body_text:
        print(f"✅ Invalid login correctly FAILED for {case['username']}")
        passed += 1
    else:
        print(f"❌ Test FAILED for {case['username']}")
        failed += 1

total = len(test_cases)
success_rate = (passed / total) * 100

print("\n=== TEST SUMMARY ===")
print(f"Total tests run: {total}")
print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Success rate: {success_rate:.1f}%")

# Capture screenshot of result
driver.save_screenshot("task2_results.png")
driver.quit()
