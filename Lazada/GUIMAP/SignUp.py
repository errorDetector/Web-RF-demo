# Author: minh.nguyen
# Created Date: August 5, 2016
# Description: store all Home Page - Log In/Sign Up popup - SignUp elements



SignUp_SignUpForm = '//form[@id="popup-form-account-create"]'

SignUp_NameLabel = SignUp_SignUpForm + '//label[contains(text(),"Name *")]'
SignUp_NameTextField = SignUp_SignUpForm + '//input[@id="signup-popup-name"]'
SignUp_EmailAddressLabel = SignUp_SignUpForm + SignUp_SignUpForm + '//label[contains(text(),"Email Address *")]'
SignUp_EmailAddressTextField = SignUp_SignUpForm + '//input[@id="signup-popup-email"]'
SignUp_PasswordLabel = SignUp_SignUpForm + SignUp_SignUpForm + '//label[contains(text(),"Password *")]'
SignUp_PasswordTextField = SignUp_SignUpForm + '//input[@id="signup-popup-password"]'
SignUp_RetypePasswordLabel = SignUp_SignUpForm + SignUp_SignUpForm + '//label[contains(text(),"Retype Password *")]'
SignUp_RetypePasswordTextField = SignUp_SignUpForm + '//input[@id="signup-popup-password2"]'
SignUp_BirthdayLabel = SignUp_SignUpForm + SignUp_SignUpForm + '//label[contains(text(),"Birthday *")]'
SignUp_Birthday_Day = SignUp_SignUpForm + '//select[@id="RegistrationForm_day"]'
SignUp_Birthday_Month = SignUp_SignUpForm + '//select[@id="RegistrationForm_month"]'
SignUp_Birthday_Year = SignUp_SignUpForm + '//select[@id="RegistrationForm_year"]'
SignUp_GenderLabel = SignUp_SignUpForm + '//label[contains(text(),"Gender")]'
SignUp_Gender_Male = SignUp_SignUpForm + '//input[@id="RegistrationForm_gender_0"]'
SignUp_Gender_Female = SignUp_SignUpForm + '//input[@id="RegistrationForm_gender_1"]'

SignUp_SubmitButton = '//button[contains(text(),"Submit")]'
