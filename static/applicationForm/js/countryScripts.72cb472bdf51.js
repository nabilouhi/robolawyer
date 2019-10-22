options = {
  defaultCountry: '',
  responsiveDropdown: true,
  preferredCountries: []
};

$('#indPob').countrySelect(options);
$('#indNationality').countrySelect(options);
$('#lNationality').countrySelect(options);
$('#nlNationality').countrySelect(options);
$('#orgnlNationality').countrySelect(options);
$('#orglNationality').countrySelect(options);

// var countrySelect = function(countryID, telID) {
//   var countryData = window.intlTelInputGlobals.getCountryData(),
//     countryInput = document.querySelector(telID),
//     addressDropdown = document.querySelector(countryID);
//   var iti = window.intlTelInput(countryInput, {
//     utilsScript: 'static/appForm/intlTelInput/utils.js' // just for formatting/placeholders etc
//   });

//   for (var i = 0; i < countryData.length; i++) {
//     var country = countryData[i];
//     var optionNode = document.createElement('option');
//     optionNode.value = country.iso2;
//     var textNode = document.createTextNode(country.name);
//     optionNode.appendChild(textNode);
//     addressDropdown.appendChild(optionNode);
//   }
//   // set it's initial value
//   // addressDropdown.value = "iti.getSelectedCountryData().iso2;"

//   // listen to the address dropdown for changes
//   addressDropdown.addEventListener('change', function() {
//     console.log(iti);
//     iti.setCountry(this.value);
//   });

//   $(countryID)
//     .nextAll()
//     .remove();
// };

// countrySelect('#indPob', '#phonePob');
// countrySelect('#indNationality', '#phoneNationality');
// countrySelect('#nlNationality', '#phonenlNationality');
// countrySelect('#lNationality', '#phonelNationality');
// countrySelect('#orgnlNationality', '#orgPhonenlNationality');
// countrySelect('#orglNationality', '#orgPhonelNationality');
