document.addEventListener('DOMContentLoaded', function() {
  var stepperFormEl = document.querySelector('#stepperForm');
  stepperForm = new Stepper(stepperFormEl, {
    animation: true,
    linear: false,
    excluded:
      'input[type=button], input[type=submit], input[type=reset], input[type=hidden], :disabled'
  });

  // stepperFormEl.addEventListener('show.bs-stepper', function(event) {
  //   if (event.detail.from === 0) {
  //     if (onValidate('page1')) {
  //       console.log('page1 passed');
  //     } else {
  //       alert('Please answer the mandatory fields first.');
  //       event.preventDefault();
  //     }
  //   } else if (event.detail.from === 1) {
  //     appVal = document.querySelector("input[name='applicantType']:checked")
  //       .value;
  //     console.log(appVal);
  //     if (appVal === 'Individual') {
  //       if (onValidate('page2a')) {
  //         console.log('page2a passed');
  //       } else {
  //         alert('Please answer the mandatory fields first.');
  //         event.preventDefault();
  //         return;
  //       }
  //     } else if (appVal === 'Organisation') {
  //       if (onValidate('page2b')) {
  //         console.log('page2b passed');
  //       } else {
  //         alert('Please answer the mandatory fields first.');
  //         event.preventDefault();
  //         return;
  //       }
  //     } else {
  //       console.log('check for bug');
  //     }
  //   } else if (event.detail.from === 2) {
  //     if (onValidate('page3')) {
  //       console.log('page3 passed');
  //     } else {
  //       alert('Please answer the mandatory fields first.');
  //       event.preventDefault();
  //     }
  //   }
  // });
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
      console.log('invalid');
      return false;
    }
  }

  stepperFormEl.addEventListener('shown.bs-stepper', function(event) {
    if (event.detail.indexStep === 7) {
      generateSummary();
    }
  });

  submitBtn = document.getElementById('form-submit-btn');
  submitBtn.addEventListener('click', function() {
    form.submit();
  });
});

var applicantTypeOption = function() {
  $("input[name='applicantType']").change(function() {
    result = this.value;
    if (result === 'Individual') {
      $('#indBeginner').removeClass('is-hidden');
      $('#orgBeginner').addClass('is-hidden');
    } else if (result === 'Organisation') {
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
    $('#selfRep').addClass('is-hidden');
  } else if (result === 'non-lawyer') {
    $('#nonLawyerRep').removeClass('is-hidden');
    $('#lawyerRep').addClass('is-hidden');
    $('#selfRep').addClass('is-hidden');
  } else if (result === 'selfRepresented') {
    $('#selfRep').removeClass('is-hidden');
    $('#nonLawyerRep').addClass('is-hidden');
    $('#lawyerRep').addClass('is-hidden');
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

//  stepper responsive

// jQuery(document).ready(function($) {
//   var alterClass = function() {
//     var ww = document.body.clientWidth;
//     if (ww < 1000) {
//       $('#stepperForm').addClass('vertical');
//     } else if (ww >= 1001) {
//       $('#stepperForm').removeClass('vertical');
//     }
//   };
//   $(window).resize(function() {
//     alterClass();
//   });
//   //Fire it when the page first loads:
//   alterClass();
// });
