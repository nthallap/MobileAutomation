import time
from appium import webdriver
from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()

options.set_capability("platformName", "Android")
options.set_capability("platformVersion", "13")
options.set_capability("deviceName", "Redmi Note 10 Pro")
options.set_capability("udid", "d12abdf7")
options.set_capability("automationName", "UiAutomator2")
options.set_capability("appPackage", "com.miui.calculator")
options.set_capability("appActivity", "com.miui.calculator.cal.CalculatorActivity")
options.set_capability("noReset", True)

# 🔥🔥 CRITICAL LINE (THIS FIXES YOUR ERROR)
options.set_capability("appium:disableHiddenApiPolicy", True)

driver = webdriver.Remote(
    command_executor="http://127.0.0.1:4723",
    options=options
)

time.sleep(10)
driver.quit()
