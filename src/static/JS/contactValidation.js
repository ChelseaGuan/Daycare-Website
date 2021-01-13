function contactValidate() {

    var full_name = document.getElementById('full_name').value;
    var full_name_RGEX = /^[a-zA-Z -]+$/;
    var full_name_Result = full_name_RGEX.test(full_name);


    if(full_name_Result == false)
    {
        alert('Please enter a valid full name (must only contain letters, spaces and hyphens).');
        return false;
    }


    return true;
}