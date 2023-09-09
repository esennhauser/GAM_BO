from appium import webdriver

desired_cap = {
  "platformName": "Android",
  "appium:platformVersion": "12",
  "appium:deviceName": "a12",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.sec.android.app.popupcalculator",
  "appium:appActivity": "com.sec.android.app.popupcalculator.Calculator"
}

appium_server_url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(command_executor=appium_server_url, desired_capabilities=desired_cap)
