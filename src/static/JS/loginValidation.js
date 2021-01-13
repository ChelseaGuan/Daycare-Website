function loginValidate() {

    var email = document.getElementById('email').value;
    var emailRGEX = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var emailResult = emailRGEX.test(email);

    var password = document.getElementById('password').value;
    var passwordRGEX = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*()_+=]{6,}$/;
    var passwordResult = passwordRGEX.test(password);

    if (emailResult == false) {
        alert('Please enter a valid email.');
        return  false;
    }

    if(passwordResult == false)
    {
        alert('Please enter a valid password (must contain at least one letter and one number and be at least 6 characters long).');
        return false;
    }

    return true;
}