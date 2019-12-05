$('#involvedStates').on('change', function() {
  currentSelected = $(this).val();
  $('.selectedTag').tagsinput({
    allowDuplicated: false,
    itemValue: currentSelected
  });
});
