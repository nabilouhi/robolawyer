function addDatepicker() {
  $('.datepicker').datepicker({
    weekStart: 1,
    assumeNearbyYear: true,
    autoclose: false,
    todayHighlight: true,
    clearBtn: true,
    format: "dd/mm/yyyy",
    todayHighlight: true,
    format: {
      toDisplay: 'dd-mm-yyyy',
      toValue: 'dd-mm-yyyy'
        },
  });
}

$('document').on('focus',".datepicker", function(){
  $(this).addDatepicker();
})