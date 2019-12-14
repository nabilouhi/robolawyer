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
      // if (onValidate('page1')) {
      console.log('page1 passed');
      // } else {
      //   alert('Please answer the mandatory fields first.');
      //   event.preventDefault();
      // }
    } else if (event.detail.from === 1) {
      if (onValidate('page2')) {
        appVal = document.querySelector("input[name='applicantType']:checked")
          .value;
        console.log(appVal);
        if (appVal === 'Individual') {
          if (onValidate('page2a')) {
            console.log('page2a passed');
          } else {
            alert('Please answer the mandatory fields first.');
            event.preventDefault();
            return;
          }
        } else if (appVal === 'Organisation') {
          if (onValidate('page2b')) {
            console.log('page2b passed');
          } else {
            alert('Please answer the mandatory fields first.');
            event.preventDefault();
            return;
          }
        } else {
          console.log('check for bug');
        }
      } else {
        alert('Please answer the mandatory fields first.');
        event.preventDefault();
      }
    } else if (event.detail.from === 1) {
    } else if (event.detail.from === 3) {
      if (onValidate('page4')) {
        console.log('page4 passed');
      } else {
        alert('Please answer the mandatory fields first.');
        event.preventDefault();
      }
    }
  });

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
      // generateSummary();
    }
  });

  submitBtn = document.getElementById('form-submit-btn');
  submitBtn.addEventListener('click', function() {
    form.submit();
  });
});

var applicantTypeOption = function() {
  $("input[name='page2[applicantType]']").change(function() {
    result = this.value;
    console.log(result);
    if (result === 'Individual') {
      $('#indBeginner').removeClass('is-hidden');
      $('#orgBeginner').addClass('is-hidden');
      $('#indRepresentative').removeClass('is-hidden');
      $('#orgRepresentative').addClass('is-hidden');
    } else if (result === 'Organisation') {
      $('#orgBeginner').removeClass('is-hidden');
      $('#indBeginner').addClass('is-hidden');
      $('#orgRepresentative').removeClass('is-hidden');
      $('#indRepresentative').addClass('is-hidden');
    } else {
      console.log('check for bug');
    }
  });
};

applicantTypeOption();

// anonymity Description
$("input[name='page2[applicantAnon]']").change(function() {
  result = this.value;

  if (result === 'Yes') {
    $('.applicantAnonReq').removeClass('is-hidden');
  } else {
    $('.applicantAnonReq').addClass('is-hidden');
  }
});
// anonymity Description End

// ___________________Page4

$("input[name='page3[indRepresentativeType]']").change(function() {
  result = this.value;
  console.log(result);
  if (result === 'lawyer') {
    $('#lawyerRep').removeClass('is-hidden');
    $('#nonLawyerRep').addClass('is-hidden');
    $('#selfRep').addClass('is-hidden');
    $('.indAuthority').removeClass('is-hidden');
  } else if (result === 'non-lawyer') {
    $('#nonLawyerRep').removeClass('is-hidden');
    $('#lawyerRep').addClass('is-hidden');
    $('#selfRep').addClass('is-hidden');
    $('.indAuthority').removeClass('is-hidden');
  } else if (result === 'selfRepresented') {
    $('#selfRep').removeClass('is-hidden');
    $('#nonLawyerRep').addClass('is-hidden');
    $('#lawyerRep').addClass('is-hidden');
    $('.indAuthority').addClass('is-hidden');
  } else {
    console.log('check for bugs');
  }
});

$("input[name='page3[orgRepresentativeType]']").change(function() {
  result = this.value;
  console.log(result);
  if (result === 'orgYesLawyer') {
    $('#orgLawyerRep').removeClass('is-hidden');
    $('.orgAuthority').removeClass('is-hidden');
  } else if (result === 'orgNoLawyer') {
    $('#orgLawyerRep').addClass('is-hidden');
    $('.orgAuthority').addClass('is-hidden');
  } else {
    console.log('check for bugs');
  }
});

//  stepper responsive

jQuery(document).ready(function($) {
  var alterClass = function() {
    var ww = document.body.clientWidth;
    if (ww < 700) {
      $('#stepperForm').addClass('vertical');
    } else if (ww >= 701) {
      $('#stepperForm').removeClass('vertical');
    }
  };
  $(window).resize(function() {
    alterClass();
  });
  //Fire it when the page first loads:
  alterClass();
});

// for add/remove input functionality
var addRemElements = function(partners, partner, addmore) {
  $(document).ready(function() {
    var data_fo = $(partners).html();
    var sd = '<div class="btn btn-danger remove-add-more">Remove</div><hr>';
    var max_fields = 5; //maximum input boxes allowed
    var wrapper = $(partners); //Fields wrapper
    var add_button = $(addmore); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) {
      //on add input button click
      e.preventDefault();
      if (x < max_fields) {
        //max input box allowed
        x++; //text box increment
        var partnerClone = $(partner)
          .first()
          .clone();
        $(sd).appendTo(partnerClone);
        $(wrapper).append(partnerClone);
      }
    });

    $(wrapper).on('click', '.remove-add-more', function(e) {
      //user click on remove text
      e.preventDefault();
      $(this)
        .parent(partner)
        .remove();
      $(this).remove();
      x--;
    });
  });
};

addRemElements('.articles', '.article', '.add-more');
addRemElements('.complaints', '.complaint', '.add-more-complaints');
addRemElements('.docLists', '.docList', '.add-more-docs');

// Add remove functionality end

//  Custom file input name display
$('.custom-file-input').on('change', function() {
  var fileName = $(this)
    .val()
    .split('\\')
    .pop();
  $(this)
    .siblings('.custom-file-label')
    .addClass('selected')
    .html(fileName);
});
//  custom file input end

// Correspondent details

$("input[name='page9[signatureDeclaration]']").change(function() {
  result = this.value;
  if (result === 'Applicant') {
    $('#correspondentOptionApplicant').removeClass('is-hidden');
    $('#correspondentOptionRepresentative').addClass('is-hidden');
  } else if (result === 'Representative') {
    $('#correspondentOptionApplicant').addClass('is-hidden');
    $('#correspondentOptionRepresentative').removeClass('is-hidden');
  } else {
    console.log('check for bugs');
  }
});

// Correcpondant details end

// File upload script
$(document).ready(function() {
  if (window.File && window.FileList && window.FileReader) {
    $('.files').on('change', function(e) {
      var files = e.target.files,
        filesLength = files.length;
      for (var i = 0; i < filesLength; i++) {
        var f = files[i];
        var fileReader = new FileReader();
        fileReader.onload = function(e) {
          var file = e.target;
          $(
            '<span class="pip">' +
              '<img class="imageThumb" src="' +
              e.target.result +
              '" title="' +
              file.name +
              '"/>' +
              '<br/><span class="remove">Remove image</span>' +
              '</span>'
          ).insertAfter('#files');
          $('.remove').click(function() {
            $(this)
              .parent('.pip')
              .remove();
          });
        };
        fileReader.readAsDataURL(f);
      }
    });
  } else {
    alert("Your browser doesn't support to File API");
  }
});
// File upload script end

// Page 6 condition for text area
$("input[name='page6[appealAvailable]']").change(function() {
  result = this.value;
  if (result === 'Yes') $('.appealDescribe').removeClass('is-hidden');
  else {
    $('.appealDescribe').addClass('is-hidden');
  }
});

// Page 6 condition for text area end
// $("input[name='page7[intInvestigation']").change(function() {
//   result = this.value;
//   if (result === 'Yes') $('.intInvestigation').removeClass('is-hidden');
//   else {
//     $('.intInvestigation').addClass('is-hidden');
//   }
// });

// page 7 conditions for text area

// $("input[name='page3[orgRepresentativeType]']").change(function() {
//   result = this.value;
//   console.log(result);
//   if (result === 'orgYesLawyer') {
//     $('#orgLawyerRep').removeClass('is-hidden');
//     $('.orgAuthority').removeClass('is-hidden');
//   } else if (result === 'orgNoLawyer') {
//     $('#orgLawyerRep').addClass('is-hidden');
//     $('.orgAuthority').addClass('is-hidden');
//   } else {
//     console.log('check for bugs');
//   }
// });

$("input[name='page7[intInvestigation]']").change(function() {
  result = this.value;
  console.log(result);
  if (result === 'Yes') $('.intInvestigation').removeClass('is-hidden');
  else {
    $('.intInvestigation').addClass('is-hidden');
  }
});

$("input[name='page7[prevApplications]']").change(function() {
  result = this.value;
  console.log(result);
  if (result === 'Yes') $('.prevAppDesc').removeClass('is-hidden');
  else {
    $('.prevAppDesc').addClass('is-hidden');
  }
});

function textCounter(field, field2, maxlimit) {
  var countfield = document.getElementById(field2);
  if (field.value.length > maxlimit) {
    field.value = field.value.substring(0, maxlimit);
    return false;
  } else {
    countfield.value = maxlimit - field.value.length;
  }
}

$(document).ready(function() {
  var select = '';
  for (i = 1; i <= 100; i++) {
    select += '<option val=' + i + '>' + i + '</option>';
  }
  $('#noOfPage').html(select);
});
