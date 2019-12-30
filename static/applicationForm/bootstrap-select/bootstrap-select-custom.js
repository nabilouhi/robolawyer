$('.countrySelect').selectpicker({
  liveSearch: true,
  noneSelectedText: 'Select Involved State(s)',
  maxOptions: 8,
  maxOptionsText: 'Reached Maximum Limit',
  selectedTextFormat: 'values',
  actionsBox: true,
  selectOnTab: true,
  multipleSeparator: ' , ',
  style: 'btn-muted',
  styleBase: 'form-control',
  virtualScroll: true
});

$(document).ready(function() {
  $('.bs-select-all').remove();
  $('.bs-deselect-all')
    .addClass('btn-info')
    .removeClass('btn-light');
});
