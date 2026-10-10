document.addEventListener('DOMContentLoaded', function() {
    // Fill the department dropdown on page load
    var deptDropdown = document.getElementById('ddlDeptNo');
    deptDropdown.innerHTML = '<option value="">Select Department</option>';
    // get-all-departments Api call using fetch
    fetch('/api/get-all-departments/')
        .then(response => response.json())
        .then(data => {
            // Handle the fetched data
            console.log(data);
            data.forEach(department => {
                deptDropdown.innerHTML += '<option value="' + department.DeptNo + '">' + department.DeptNo + ' - ' + department.Dname + ' - ' + department.Location + '</option>';
            });
        });

    // Cancel Button click event
    var cancelButton = document.getElementById('btnCancel');
    cancelButton.addEventListener('click', function() {
        // Redirect to the home page
        window.location.href = '/';
    });

    // Register form click event
    var btnRegister = document.getElementById('btnRegister');
    btnRegister.addEventListener('click', function() {
        // Get page control values and create a JSON object
        var empData = {
            Ename: document.getElementById('txtEname').value,
            Gender: document.querySelector('input[name="Gender"]:checked') ? document.querySelector('input[name="Gender"]:checked').value : '',
            Password: document.getElementById('txtPwd').value,
            Phone: document.getElementById('txtPhone').value,
            Email: document.getElementById('txtEmail').value,
            DOB: document.getElementById('txtDOB').value,
            Salary: parseInt(document.getElementById('txtSalary').value) || 0,
            Address: document.getElementById('txtAddress').value,
            DeptNo: parseInt(document.getElementById('ddlDeptNo').value) || 0
        };
        // Call the create-employee/ API using fetch
        fetch('/api/create-employee/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(empData)
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response from the API
            alert('Employee created successfully...!');
            // Redirect to the home page or display a success message
            window.location.href = '/';
        })
        .catch(error => {
            // Handle any errors
            console.error('Error:', error);
            alert('Error creating employee...');
        });
    });
});