


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

// $(document).ready(function(){

// })

// for add/remove input functionality
var addRemElements = function(partners, partner, addmore) {
  $(document).ready(function() {
    var data_fo = $(partners).html();
    var sd = '<div class="btn btn-danger remove-add-more">Remove</div><hr>';
    var max_fields = 10; //maximum input boxes allowed
    var wrapper = $(partners); //Fields wrapper
    var add_button = $(addmore); //Add button ID

    var x = 1; //initlal text box count
    $(add_button).click(function(e) {
      //on add input button click
      e.preventDefault();
      if (x < max_fields) {
        //max input box allowed
        x++; //text box increment
        var partnerClone = $(partner).first().clone();
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

// addRemElements('.articles', '.article', '.add-more');
// addRemElements('.complaints', '.complaint', '.add-more-complaints');
// addRemElements('.docLists', '.docList', '.add-more-docs');

// Add remove functionality end
// $(function () {
//   $('.page8Date').combodate({
//       minYear: 1900,
//       maxYear: 2020,
//       customClass: 'custom-control-inline form-control',
//       smartDays: true,
//       firstItem: 'name',
//       format: "DD/MM/YYYY"
//   });
// });

$('#page8Group').repeater({
              btnAddClass: 'r-btnAdd',
              btnRemoveClass: 'r-btnRemove',
              groupClass: 'r-group',
              minItems: 1,
              maxItems: 0,
              startingIndex: 0,
              showMinItemsOnLoad: true,
              reindexOnDelete: true,
              repeatMode: 'append',
              animation: 'fade',
              animationSpeed: 400,
              animationEasing: 'swing',
              clearValues: true
          });

$('#page6Group').repeater({
            btnAddClass: 's-btnAdd',
            btnRemoveClass: 's-btnRemove',
            groupClass: 's-group',
            minItems: 1,
            maxItems: 0,
            startingIndex: 0,
            showMinItemsOnLoad: true,
            reindexOnDelete: true,
            repeatMode: 'append',
            animation: 'fade',
            animationSpeed: 400,
            animationEasing: 'swing',
            clearValues: true
        });

$('#example1').repeater({
          btnAddClass: 'a-btnAdd',
          btnRemoveClass: 'a-btnRemove',
          groupClass: 'a-group',
          minItems: 1,
          maxItems: 0,
          startingIndex: 0,
          showMinItemsOnLoad: true,
          reindexOnDelete: true,
          repeatMode: 'append',
          animation: 'fade',
          animationSpeed: 400,
          animationEasing: 'swing',
          clearValues: true
      });
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


// Page 6 condition for text area
$("input[name='page6[appealAvailable]']").change(function() {
  result = this.value;
  if (result === 'Yes') $('.appealDescribe').removeClass('is-hidden');
  else {
    $('.appealDescribe').addClass('is-hidden');
  }
});

// Page 6 condition for text area end

// page 7 conditions for text area


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
    if(field.id==="stofFacts"){
    swal("You have used up the allocated length for Statement of Facts. For more explanation, please use the extra provided area by clicking the button 'Do you need more?'");
    }
    if(field.id==="stofFactsExtra"){
      swal("Unfortunately there is no more space available to add extra content in statement of facts according to the guidelines provided by ECtHR. Please try to modify the existing text.");
    }
    field.value = field.value.substring(0, maxlimit);
    
    return false;
  } else {
    countfield.value = maxlimit - field.value.length;
  }
}

// function maxLength(el) {    
//   if (!('maxLength' in el)) {
//       var max = el.attributes.maxLength.value;
//       el.onkeypress = function () {
//           if (this.value.length >= max) return false;
//       };
//   }
// }

// maxLength(document.getElementsByClassName("limitedArea"));