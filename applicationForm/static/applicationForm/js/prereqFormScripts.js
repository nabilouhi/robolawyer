function feedbackSubmit(e) {
  e.preventDefault();
  console.log('started');
  cardParentElement = e.target.parentElement.parentElement.children[2];
  firstInput = cardParentElement.children[0].children[1].value;
  radioInput = $('input:radio[name="legalTrained"]:checked').val();
  $('input[name="legalTrainedInput"]').val(radioInput);
  secondInput = cardParentElement.children[0].children[4].value;
  thirdInput = cardParentElement.children[1].children[1].value;

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
      alert('Feedback Submitted');
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
  $('.feedback_submit-1').click(feedbackSubmit);
  $('.feedback_submit-2').click(feedbackSubmit);
  $('.feedback_submit-3').click(feedbackSubmit);
  $('.feedback_submit-4').click(feedbackSubmit);
  $('.feedback_submit-5').click(feedbackSubmit);
  $('.feedback_submit-6').click(feedbackSubmit);
  $('.feedback_submit-7').click(feedbackSubmit);
  $('.feedback_submit-8').click(feedbackSubmit);
  $('.feedback_submit-9').click(feedbackSubmit);
  $('.feedback_submit-10').click(feedbackSubmit);
});

// data: {
//   pageNo: $('input[name="sugPageNo"]').val(),
//   suggestion: document.getElementsByName('suggestionArea')[0].value,
//   legalExp: $('input:radio[name="legalTrained"]:checked').val(),
//   csrfmiddlewaretoken: csrftoken
// },
