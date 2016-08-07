# Author: minh.nguyen
# Created Date: August 5, 2016
# Description: store all Home Page elements




# Navigation bar - on top
HomePage_Navigation_LogInBtn = '//span[text()="Login"]'
HomePage_Navigation_SignUpBtn = '//span[text()="Signup"]'
HomePage_Navigation_AccountInfomation = '//ul[@class="top-nav__list"]/li[@class="top-nav__item js-header-logged-in-account"]'


HomePage_LogInSignUpPopup_Navigation_LogInTab = '//a[text()="Login"]'
HomePage_LogInSignUpPopup_Navigation_LogInTab_Selected = HomePage_LogInSignUpPopup_Navigation_LogInTab + '/parent::*[contains(@class,"active")]'
HomePage_LogInSignUpPopup_Navigation_SignUpTab = '//a[text()="Signup"]'
HomePage_LogInSignUpPopup_Navigation_SignUpTab_Selected = HomePage_LogInSignUpPopup_Navigation_SignUpTab + '/parent::*[contains(@class,"active")]'








