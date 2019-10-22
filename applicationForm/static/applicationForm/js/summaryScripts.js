console.log('hello summary');
console.log($('#indSurname'));
console.log($("input[name='applicantType']").val());

$('#sumApplicantType').innerHTML = $("input[name='applicantType']").val();
$('#sumIndSurname').innerHTML = $('#indSurname').val();
$('#sumIndFirstName').innerHTML = $('#indFirstName').val();
