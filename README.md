# Automation Bot Data Entry
This project involves data entry automation using Python and Selenium and can be used as a good starter automation template.

# Features
Python automation with Selenium webdriver that:
1. Opens Google Chrome
2. Navigates to a specific website
3. Finds input box specified
4. Types in text
5. Finds button specified
6. Clicks the button

More data entry can be done by extending out the operations needed to additional selectors.

The website is one that is used for automation testing. After the button is clicked,
it displays the typed in text message. This allows you to see that it is functioning in 
the correct order.


![DEMO](../main/preview/preview-1.png)





# How it Work
* Python script has Selenium module installed: pip3 install selenium  
* Selenium uses chromedriver to control Google Chrome based on commands in the automation.py script.
* Selenium can use html tags or css classes/ids/selectors to identify website fields and execute a series of actions.


# Setting Up Chromedriver
1. How to Get Chrome Driver & Update Google Chrome Browser

Official Website: https://sites.google.com/chromium.org/driver/

Choose latest stable release and download it.

I placed it as follows: 
C:/path/to/chromedriver.exe

Update your Google Chrome Browser to the latest by visiting your settings/help page:
chrome://settings/help

2. Add ChromeDriver to Environmental Variables

Windows 10
Search for "this pc"
right click, click properties
click Advanced system settings
On Advanced Tab | click Environmental Variables button

Bottom Section = System Variables
Click the Path line in the System Variables section
once highlighed, click Edit button
click New button
paste in path so saves at end: C:\path\to\chromedriver.exe
click ok to save all changes

# Download & Setup Instructions

1. Download or Clone project: git clone https://github.com/anthonyakiniz/automation-bot-data-entry
2. In code editor (e.g. VSCode) change path to project root: cd automation-form-data-entry
3. Create virtual environment: virtualenv venv
4. Activate virtual enviornment: venv\scripts\activate
5. Batch install all requirements: pip install -r requirements.txt
6. Verify correct path to your chromedriver in automation.py code. Can change or use same path I use:
    executable_path='C:/path/to/chromedriver.exe'
7. Launch by clicking run button (e.g. top right in VSCode) or type in terminal: py -3 automation.py
