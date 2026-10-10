document.addEventListener('DOMContentLoaded', function() {
    // Home Page Load Event
    // alert('Home Page Loaded');
    var empTable = document.getElementById('empTable');
    empTable.innerHTML = '';
    empTable.innerHTML = '<thead>' +
        '<tr>' +
            '<th>EmpId</th>' +
            '<th>Name</th>' +
            '<th>Gender</th>' +
            '<th>Password</th>' +
            '<th>Phone</th>' +
            '<th>Email</th>' +
            '<th>DOB</th>' +
            '<th>Salary</th>' +
            '<th>Address</th>' +
            '<th>DeptNo</th>' +
        '</tr>' +
    '</thead>';
    // get-all-employees Api call using fetch
    fetch('/api/get-all-employees/')
        .then(response => response.json())
        .then(data => {
            // Handle the fetched data
            console.log(data);
            empTable.innerHTML += '<tbody>';
            data.forEach(employee => {
               empTable.innerHTML += '<tr>' +
                    '<td>' + employee.EmpId + '</td>' +
                    '<td>' + employee.Ename + '</td>' +
                    '<td>' + employee.Gender + '</td>' +
                    '<td>' + employee.Password + '</td>' +
                    '<td>' + employee.Phone + '</td>' +
                    '<td>' + employee.Email + '</td>' +
                    '<td>' + employee.DOB + '</td>' +
                    '<td>' + employee.Salary + '</td>' +
                    '<td>' + employee.Address + '</td>' +
                    '<td>' + employee.DeptNo + '</td>' +
                '</tr>' +
            '</tbody>';
            });
            empTable.innerHTML += '</tbody>';
        });
    });