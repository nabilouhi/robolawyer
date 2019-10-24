var generateSummary = function() {
  document.getElementById('sumApplicantType').innerHTML = $(
    "input[name='applicantType']"
  ).val();

  document.getElementById('sumIndSurname').innerHTML = document.getElementById(
    'indSurname'
  ).value;
  document.getElementById(
    'sumIndFirstName'
  ).innerHTML = document.getElementById('indFirstName').value;
};
