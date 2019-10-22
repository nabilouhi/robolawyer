var phoneInputScript = function(phoneDiv) {
  var inputPhone = document.querySelector(phoneDiv);
  var iti = window.intlTelInput(inputPhone, {
    utilsScript: 'static/intlTelInput/utils.js',
    allowDropdown: true,
    separateDialCode: true,
    initialCountry: 'auto',
    geoIpLookup: function(success, failure) {
      $.get('http://ipinfo.io', function() {}, 'jsonp').always(function(resp) {
        var countryCode = resp && resp.country ? resp.country : '';
        success(countryCode);
      });
    }
  });

  $(phoneDiv).change(function() {
    $(phoneDiv)
      .nextAll()
      .remove();
    if (iti.getNumber().trim()) {
      phoneError = iti.getValidationError();
      errorPar = document.createElement('p');
      inputPhone.parentElement.insertBefore(errorPar, inputPhone.nextSibling);

      if (iti.isValidNumber()) {
        console.log(iti.getNumber());
        errorPar.innerHTML = 'The number is valid';
        errorPar.className += 'help is-success is-size-6';
      } else {
        errorPar.className += 'help is-danger is-size-6';
        if (phoneError == 2) {
          errorPar.innerHTML = 'The number you entered is too short';
        } else if (phoneError == 3) {
          errorPar.innerHTML = 'The number you entered is too long';
        } else if (phoneError == 4) {
          errorPar.innerHTML = 'Input is not a number';
        } else {
          errorPar.innerHTML = 'Error in the number entered. Please verify';
        }
      }
    }
  });
};

phoneInputScript('#indPhone');
phoneInputScript('#orgPhone');
phoneInputScript('#nlTel');
phoneInputScript('#lTel');
phoneInputScript('#orgnlTel');
phoneInputScript('#orglTel');
