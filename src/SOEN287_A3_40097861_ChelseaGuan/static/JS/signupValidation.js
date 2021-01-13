function signupValidate() {

    var first_name = document.getElementById('first_name').value;
    var first_name_RGEX = /^[a-zA-Z -]+$/;
    var first_name_Result = first_name_RGEX.test(first_name);

    var last_name = document.getElementById('last_name').value;
    var last_name_RGEX = /^[a-zA-Z -]+$/;
    var last_name_Result = last_name_RGEX.test(last_name);

    var phone = document.getElementById('phone').value;
    var phoneRGEX = /^[(]{0,1}[0-9]{3}[)]{0,1}[-\s\.]{0,1}[0-9]{3}[-\s\.]{0,1}[0-9]{4}$/;
    var phoneResult = phoneRGEX.test(phone);

    var email = document.getElementById('email').value;
    var emailRGEX = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    var emailResult = emailRGEX.test(email);

    var password = document.getElementById('password').value;
    var passwordRGEX = /^(?=.*\d)(?=.*[a-zA-Z])[0-9a-zA-Z!@#$%^&*()_+=]{6,}$/;
    var passwordResult = passwordRGEX.test(password);


    if(first_name_Result == false)
    {
        return false;
        alert('Please enter a valid first name (must only contain letters, spaces and hyphens).');
    }

    if(last_name_Result == false)
    {
        alert('Please enter a valid last name (must only contain letters, spaces and hyphens).');
        return false;
    }

    if(phoneResult == false)
    {
        alert('Please enter a valid phone number (must be 10 digits long).');
        return false;
    }

    if(emailResult == false)
    {
        alert('Please enter a valid email.');
        return false;
    }

    if(passwordResult == false)
    {
        alert('Please enter a valid password (must contain at least one letter and one number and be at least 6 characters long).');
        return false;
    }

    return true;
}