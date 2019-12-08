// https://github.com/xoxco/jQuery-Tags-Input

$('#tags').tagsInput({
  width: '100%',
  height: '5%',
  defaultText: '',
  removeWithBackspace: false,
  interactive: false
});

var finalTags = function(selectedCountries) {
  tagcsv = selectedCountries.toString();
  $('#tags').importTags(tagcsv);
};

$('#involvedStates').on('change', function() {
  currentSelected = $(this).val();
  finalTags(currentSelected);
});
