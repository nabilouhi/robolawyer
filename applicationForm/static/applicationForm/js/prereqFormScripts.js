$('#finalDecisionDate').on('change', function(){
    finalDecisionDate = $('#finalDecisionDate').combodate('getValue',format='YYYY-MM-DD');
    currentDate = moment().format('YYYY-MM-DD');
    diffDate = moment(currentDate).diff(moment(finalDecisionDate), 'months', true);
    if (!isNaN(diffDate)){
      if(diffDate < 6) {
        sixFutureDate = moment(finalDecisionDate).add(6, 'months').format('YYYY-MM-DD');
        swal('Attention, according to the information entered in the date field, you must send your application in good time before '+ sixFutureDate);
      }
      else if (diffDate > 6) {
        swal('You have missed the 6 months limit deadline imposed by the court. It is possible, but not necessary that your application might be declared inadmissible.')  
      }
      else {
        console.warn('check for problem')
      }
    }
  });






// Feedback form
var curPageNum = function(pageNumValue) {
  console.log(pageNumValue.value)
    document.getElementById("sugPageNo").value = pageNumValue.value;
}



function feedbackSubmit(e) {
  e.preventDefault();

  console.log(e.target);
  cardParentElement = e.target.parentElement.parentElement.parentElement;
  console.log(cardParentElement);
  firstInput = document.getElementById("sugPageNo").value;
  radioInput = $('input:radio[name="legalTrained"]:checked').val();
  $('input[name="legalTrainedInput"]').val(radioInput);
  	thirdInput = cardParentElement.getElementsByTagName("textarea")[0].value
     secondInput = radioInput;


  var csrftoken = getCookie('csrftoken');
  $.ajax({
    type: 'POST',
    url: '/form/feedback',
    data: {
      pageNo: firstInput,
      legalExp: secondInput,
      suggestion: thirdInput,
      csrfmiddlewaretoken: csrftoken
    },
    success: function() {
      swal('Feedback Submitted');
      
    }
  });
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}


$(document).ready(function() {
  $('.feedback_submit').click(feedbackSubmit);
});




//////////////////////////////////////////////////////////////////
$("input[name='page1[complySix]']").change(function() {
  result = this.value;

  if (result === 'Yes') {
    swal('If you have not exhausted the available legal remedies your application can be declared inadmissible.')
  }
});