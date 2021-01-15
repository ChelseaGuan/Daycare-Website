# Daycare-Website  

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
        <li><a href="#features">Features</a></li>
      </ul>
    </li>
    <li>
      <a href="#demonstration">Demonstration</a>
       <ul>
        <li><a href="#demo-part-1-:-home-page-and-about-us-pagewith">Home and About Us</a></li>
      </ul>
    </li>
  </ol>
</details>  
  
## About the Project  
Responsive website with template inheritance, error handling and form validation.  
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
  
### Demo Part 1: Home page and About Us page  
![Home + About Us](images/Home+AboutUs.gif)  
  
### Demo Part 2: Programs page  
![Programs](images/Programs.gif)  
  
### Demo Part 3: Gallery page  
![Gallery](images/Gallery.gif)  
  
### Demo Part 4: To contact the daycare owner, the user must first login to their account  
![NewUser](images/NewUser.gif)  
  
### Demo Part 5: Registration  
  
Since this user is new, they must fill in the registration page. However, they forgot to fill in the "Last name" textbox, which is mandatory. Validation is unsuccessful.  
![Registration Empty Textbox Warning](images/RegistrationEmptyTBWarning.gif)  
  
The user enters a last name, but their password is too short. Upon entering a longer password, the form is validated and an account is created for the user.  
![Registration Password Warning](images/RegistrationPwdWarning.gif)  
  
The user's information is stored in a CSV file called "accounts.csv", where a salt is added to the password and the result is hashed.  
![Account Information](images/AccountInfo.PNG)  
  
### Demo Part 8: Successful user login  
![Login](images/Login.gif)  
  
### Demo Part 9: Contact  
  
The form can be cleared to its original state.  
![Application Clear Form](images/ApplicationClearForm.gif)  
  
Upon successfully contacting the daycare owner, a confirmation message is displayed.  
![Application Done](images/ApplicationDone.gif)  
