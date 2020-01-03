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
  $('#feedback_submit').click(function(e) {
    e.preventDefault();
    var csrftoken = getCookie('csrftoken');
    $.ajax({
      type: 'POST',
      url: '/form/feedback',
      data: {
        legalExp: $('input[name="legalTrained"]').val(),
        suggestion: $('#suggestionArea').val(),
        csrfmiddlewaretoken: csrftoken
      },
      success: function() {
        alert('feedback done');
      }
    });
  });
});