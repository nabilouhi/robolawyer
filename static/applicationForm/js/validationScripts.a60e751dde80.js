var stepperFormEl = document.querySelector('#stepperForm');
// var indSurname = document.getElementById();
var inputPasswordForm = document.getElementById('inputPasswordForm');
var form = stepperFormEl.querySelector('.bs-stepper-content form');
var stepperPanList = [].slice.call(
  stepperFormEl.querySelectorAll('.bs-stepper-pane')
);

stepperFormEl.addEventListener('show.bs-stepper', function(event) {
  form.classList.remove('was-validated');
  var nextStep = event.detail.indexStep;
  var currentStep = nextStep;

  if (currentStep > 0) {
    currentStep--;
  }

  var stepperPan = stepperPanList[currentStep];

  // if (
  //   stepperPan.getAttribute('indSurname') === 'form-page-1' &&
  //   !inputMailForm.value.length
  //   // (stepperPan.getAttribute('id') === 'form-page-2' &&
  //   //   !inputPasswordForm.value.length)
  // ) {
  //   event.preventDefault();
  //   form.classList.add('was-validated');
  // }
});
