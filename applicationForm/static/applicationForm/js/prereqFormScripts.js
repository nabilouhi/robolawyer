feedbackSubmit = function(page) {
  $(document).ready(function() {
    console.log('started');
    $('.feedback_submit-' + page).click(function(e) {
      e.preventDefault();
      var csrftoken = getCookie('csrftoken');
      $.ajax({
        type: 'POST',
        url: '/form/feedback',
        data: {
          pageNo: $('input[name="sugPageNo"]').val(),
          legalExp: $('input:radio[name="legalTrained"]:checked').val(),
          suggestion: $('input[name="suggestionArea"]').val(),
          csrfmiddlewaretoken: csrftoken
        },
        success: function() {
          $('.suggestion-form-' + page).addClass('is-hidden');
          alert('feedback done');
        }
      });
    });
  });
};

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
