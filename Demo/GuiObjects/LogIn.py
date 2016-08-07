# Author: minh.nguyen
# Created Date: August 5, 2016
# Description: store all Home Page - Log In/Sign Up popup - LogIn elements


LogIn_LogInForm = '//form[@id="popup-form-account-login"]'

LogIn_EmailAddressLabel = LogIn_LogInForm + '//label[contains(text(),"Email Address *")]'
LogIn_EmailAddressTextField = LogIn_LogInForm + '//input[@id="login-popup-email"]'
LogIn_PasswordLabel = LogIn_LogInForm + '//label[contains(text(),"Password *")]'
LogIn_PasswordTextField = LogIn_LogInForm + '//input[@id="login-popup-pass"]'
LogIn_LOGINButton = LogIn_LogInForm + '//button[contains(text(),"LOGIN")]'

LogIn_ForgotPasswordLink = LogIn_LogInForm + '//a[contains(text(),"Forgot password?")]'

LogIn_ErrorMessage1 = LogIn_EmailAddressTextField + '/../span'
LogIn_ErrorMessage2 = LogIn_PasswordTextField + '/../span'

