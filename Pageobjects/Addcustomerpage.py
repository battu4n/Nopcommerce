import time

from selenium.webdriver.common.by import By


class Addcustomer:
    # Add customerpage
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomermenu_item_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btnAddnew_xpath = "//a[normalize-space()='Add new']"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstname_id = "FirstName"
    txtLastname_id = "LastName"
    genderMale_xpath = "//input[@id='Gender_Male']"
    genderFemale_xpath = "//input[@id='Gender_Female']"
    textboxDOB_xpath = "//input[@id='DateOfBirth']"
    txtboxcompanyname_id = "Company"
    checkboxtaxexcempt_xpath = "//input[@id='IsTaxExempt']"
    txtboxnewsletter_xpath = "//span[@aria-expanded='true']//input[@role='searchbox']"
    txtcustomerrole_xpath = "//span[@class='select2 select2-container select2-container--default select2-container--focus']//ul[@class='select2-selection__rendered']"
    dropdownmanagevendor_xpath = "//select[@id='VendorId']"
    checboxActive_xpath = "//input[@id='Active']"
    txtboxAdmincomment_id = "AdminComment"
    btnsave_xpath = "//button[@name='save']"
    btnsave_continue_xpath = "//button[normalize-space()='Save and Continue Edit']"

    def __init__(self, driver):  # constructor will get the driver from actual test case and itiate the driver here
        self.driver = driver

    def clickoncsutomermenu(self):
        self.driver.find_element(By.XPATH, self.lnkCustomers_menu_xpath).click()

    def clickoncustomermenuitem(self):
        self.driver.find_element(By.XPATH, self.lnkCustomermenu_item_xpath).click()

    def clickonAddnew(self):
        self.driver.find_element(By.XPATH, self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element(By.ID, self.txtEmail_id).send_Keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.txtPassword_id).send_Keys(password)

    def setCustomerrole(self,role):
        self.driver.find_element(By.XPATH,self.txtcustomerrole_xpath).click()
        time.sleep(3)

