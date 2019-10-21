$('#appForm')
  .parsley()
  .on('field:validate', function() {
    var elem = this.$element;

    // If the field is not visible, do not apply Parsley validation!
    if (
      $(elem)
        .closest('.form-page')
        .hasClass('is-hidden')
    ) {
      this.constraints = [];
    }
  });

document.addEventListener('DOMContentLoaded', function() {
  var stepperFormEl = document.querySelector('#stepperForm');
  stepperForm = new Stepper(stepperFormEl, {
    animation: true,
    linear: false
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

  function onValidate() {
    if (!$('appForm').parsley('isValid')) {
      $('.parsley-error')
        .closest('.tab-pane')
        .show();
      return false;
    }

    return true;
  }

  submitBtn = document.getElementById('form-submit-btn');
  submitBtn.addEventListener('click', function() {
    message = onValidate();
    if (message === true) {
      form.submit();
    } else {
      alert('Some of the required fields are empty. Please check the form.');
      form.submit();
    }
  });
});

var applicantTypeOption = function() {
  $("input[name='applicantType']").change(function() {
    result = this.value;
    console.log(result);
    if (result === 'Individual') {
      $('#page1Button').removeAttr('disabled');
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
  if (result === 'lawyer') {
    $('#nonLawyerRep').removeClass('is-hidden');
    $('#lawyerRep').addClass('is-hidden');
  } else if (result === 'non-lawyer') {
    $('#lawyerRep').removeClass('is-hidden');
    $('#nonLawyerRep').addClass('is-hidden');
  } else {
    console.log('check for bugs');
  }
});

$("input[name='orgRepresentativeType']").change(function() {
  result = this.value;
  if (result === 'lawyer') {
    $('#orgNonLawyerRep').removeClass('is-hidden');
    $('#lawyerRep').addClass('is-hidden');
  } else if (result === 'non-lawyer') {
    $('#lawyerRep').removeClass('is-hidden');
    $('#orgNonLawyerRep').addClass('is-hidden');
  } else {
    console.log('check for bugs');
  }
});

$(function() {
  var $sections = $('.form-section');

  function navigateTo(index) {
    // Mark the current section with the class 'current'
    $sections
      .removeClass('current')
      .eq(index)
      .addClass('current');
    // Show only the navigation buttons that make sense for the current section:
    $('.form-navigation .previous').toggle(index > 0);
    var atTheEnd = index >= $sections.length - 1;
    $('.form-navigation .next').toggle(!atTheEnd);
    $('.form-navigation [type=submit]').toggle(atTheEnd);
  }

  function curIndex() {
    // Return the current index by looking at which section has the class 'current'
    return $sections.index($sections.filter('.current'));
  }

  // Previous button is easy, just go back
  $('.form-navigation .previous').click(function() {
    navigateTo(curIndex() - 1);
  });

  // Next button goes forward iff current block validates
  $('.form-navigation .next').click(function() {
    if (
      $('.demo-form')
        .parsley()
        .validate('block-' + curIndex())
    )
      navigateTo(curIndex() + 1);
  });

  // Prepare sections by setting the `data-parsley-group` attribute to 'block-0', 'block-1', etc.
  $sections.each(function(index, section) {
    $(section)
      .find(':input')
      .attr('data-parsley-group', 'block-' + index);
  });
  navigateTo(0); // Start at the beginning
});
