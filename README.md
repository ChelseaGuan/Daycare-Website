# Daycare-Website  


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ul>
    <li>
      <a href="#about-the-project">About the Project</a>
      <ol>
        <li><a href="#development">Development</a></li>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#features">Features</a></li>
      </ol>
    </li>
    <li>
      <a href="#demonstration">Demonstration</a>
       <ol type="1">
        <li><a href="#demo-part-1-home-and-about-us">Home and About Us</a></li>
         <li><a href="#demo-part-2-programs">Programs</a></li>
         <li><a href="#demo-part-3-gallery">Gallery</a></li>
         <li><a href="#demo-part-4-user-login-required">User Login Required</a></li>
         <li><a href="#demo-part-5-registration">Registration</a></li>
         <li><a href="#demo-part-6-successful-user-login">Successful User Login</a></li>
         <li><a href="#demo-part-7-contact">Contact</a></li>
      </ol>
    </li>
  </ul>
</details>  
  
## About the Project  
Responsive website with template inheritance, error handling and form validation. 
  
### Development
This project was developed in the PyCharm IDE from JetBrains.
  
### Built With  
* Python (Flask)
* CSS (Bootstrap)
* JavaScript
* HTML  

### Features
* Template inheritance
* Flask Form validation with WTForms 
* JavaScript input and form validation using regular expressions
* Tables and lists created dynamically from data stored in a local CSV file
* CSV file to store customer data and allow for user registration, login and logout.
  
## Demonstration  
  
### Demo Part 1: Home and About Us
![Home + About Us](images/Home+AboutUs.gif)  
  
### Demo Part 2: Programs  
![Programs](images/Programs.gif)  
  
### Demo Part 3: Gallery  
![Gallery](images/Gallery.gif)  
  
### Demo Part 4: User Login Required
To contact the daycare owner, the user must first login to their account  
![NewUser](images/NewUser.gif)  
  
### Demo Part 5: Registration  
  
Since this user is new, they must fill in the registration page. However, they forgot to fill in the "Last name" textbox, which is mandatory. Validation is unsuccessful.  
![Registration Empty Textbox Warning](images/RegistrationEmptyTBWarning.gif)  
  
The user enters a last name, but their password is too short. Upon entering a longer password, the form is validated and an account is created for the user.  
![Registration Password Warning](images/RegistrationPwdWarning.gif)  
  
The user's information is stored in a CSV file called "accounts.csv", where a salt is added to the password and the result is hashed.  
![Account Information](images/AccountInfo.PNG)  
  
### Demo Part 6: Successful User Login  
![Login](images/Login.gif)  
  
### Demo Part 7: Contact  
  
The form can be cleared to its original state.  
![Application Clear Form](images/ApplicationClearForm.gif)  
  
Upon successfully contacting the daycare owner, a confirmation message is displayed.  
![Application Done](images/ApplicationDone.gif)  
