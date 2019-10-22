document.addEventListener('DOMContentLoaded', function() {
  var stepperFormEl = document.querySelector('#stepperForm');
  stepperForm = new Stepper(stepperFormEl, {
    animation: true,
    linear: false,
    excluded:
      'input[type=button], input[type=submit], input[type=reset], input[type=hidden], :disabled'
  });

  stepperFormEl.addEventListener('show.bs-stepper', function(event) {
    if (event.detail.from === 0) {
      if (onValidate('page1')) {
        console.log('page1');
      } else {
        console.warn(event.detail);
        event.preventDefault();
      }
    } else if (event.detail.from === 1) {
      appVal = $("input[name='applicantType']").val();
      if (appVal === 'Individual') {
        if (onValidate('page2a')) {
          console.log('page2a');
        } else {
          console.log(event);
          event.preventDefault();
        }
      } else {
        if (onValidate('page2b')) {
          console.log('page2b');
        } else {
          console.log(event);
          event.preventDefault();
        }
      }
    } else if (event.detail.from === 2) {
      if (onValidate('page3')) {
        console.log('page3');
      } else {
        console.warn(event.detail);
        event.preventDefault();
      }
    }
  });
  // stepperFormEl.addEventListener('shown.bs-stepper', function(event) {
  //   console.warn(event.detail);
  // });

  var btnNextList = [].slice.call(document.querySelectorAll('.btn-next-form'));
  var stepperPanList = [].slice.call(
    stepperFormEl.querySelectorAll('.bs-stepper-pane')
  );

  btnNextList.forEach(function(btn) {
    btn.addEventListener('click', function() {
      stepperForm.next();
    });
  });

  function onValidate(groupname) {
    if (
      $('#appForm')
        .parsley()
        .validate({
          group: groupname,
          force: true
        })
    ) {
      console.log('valid');
      return true;
    } else {
      console.log(this);
      console.log('invalid');
      return false;
    }
  }

  submitBtn = document.getElementById('form-submit-btn');
  submitBtn.addEventListener('click', function() {
    form.submit();
  });
});

var applicantTypeOption = function() {
  $("input[name='applicantType']").change(function() {
    result = this.value;
    if (result === 'Individual') {
      // $('#page1Button').removeAttr('disabled');
      $('#indBeginner').removeClass('is-hidden');
      $('#orgBeginner').addClass('is-hidden');
      //   $('#indRepresentative').removeClass('is-hidden');
      //   $('#orgRepresentative').addClass('is-hidden');
    } else if (result === 'Organisation') {
      $('#page1Button').removeAttr('disabled');
      $('#indBeginner').attr('style', 'display: none');
      $('#orgBeginner').attr('style', 'display: block');
    } else {
      console.log('check for bug');
    }
  });
};

applicantTypeOption();

// ___________________Page4

$("input[name='representativeType']").change(function() {
  result = this.value;
  console.log(result);
  if (result === 'lawyer') {
    $('#lawyerRep').removeClass('is-hidden');
    $('#nonLawyerRep').addClass('is-hidden');
  } else if (result === 'non-lawyer') {
    $('#lawyerRep').addClass('is-hidden');
    $('#nonLawyerRep').removeClass('is-hidden');
  } else {
    console.log('check for bugs');
  }
});

$("input[name='orgRepresentativeType']").change(function() {
  result = this.value;
  if (result === 'lawyer') {
    $('#orgNonLawyerRep').addClass('is-hidden');
    $('#lawyerRep').removeAttr('is-hidden');
  } else if (result === 'non-lawyer') {
    $('#lawyerRep').addClass('is-hidden');
    $('#orgNonLawyerRep').removeClass('is-hidden');
  } else {
    console.log('check for bugs');
  }
});
