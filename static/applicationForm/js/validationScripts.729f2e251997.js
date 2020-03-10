document.addEventListener('DOMContentLoaded', function() {
    var stepperFormEl = document.querySelector('#stepperForm');
    stepperForm = new Stepper(stepperFormEl, {
      animation: true,
      linear: false,
      excluded:
        'input[type=button], input[type=submit], input[type=reset], input[type=hidden], :disabled'
    });
    var form = stepperFormEl.querySelector('.bs-stepper-content form')
    stepperFormEl.addEventListener('show.bs-stepper', function(event) {
      if (event.detail.from === 0) {
        if (onValidate('page1')) {
          console.log('page1 passed');
        } else {
          // swal('Please answer the mandatory fields first.');
          // event.preventDefault();
        }
      } else if (event.detail.from === 1) {
          if(onValidate('page2')){
              console.log('page2 passed');
              appVal = document.querySelector("input[name='page2[applicantType]']:checked").value;
              console.log(appVal);
              if (appVal === 'Individual') {
                if (onValidate('page2a')) {
                  console.log('page2a passed');
                } else {
                  swal('Please answer the mandatory fields first.');
                  event.preventDefault();
                  return;
                }
              } else if (appVal === 'Organisation') {
                if (onValidate('page2b')) {
                  console.log('page2b passed');
                } else {
                  swal('Please answer the mandatory fields first.');
                  event.preventDefault();
                  return;
                }
              } else {
                console.log('check for bug');
              }
          }
          else {
              swal('Please answer mandatory fields first');
              event.preventDefault();
          }     
      } else if (event.detail.from === 2) {
        if (onValidate('page3')) {
          console.log('page3 passed');
        } else {
          swal('Please answer the mandatory fields first.');
          event.preventDefault();
        }
      } else if (event.detail.from === 3) {
        if (onValidate('page4')) {
          console.log('page4 passed');
        } else {
          swal('Please answer the mandatory fields first.');
          event.preventDefault();
        }
      }
    });
    stepperFormEl.addEventListener('shown.bs-stepper', function(event) {
      console.warn(event.detail);
    });
  
    var btnNextList = [].slice.call(document.querySelectorAll('.btn-next-form'));
    var stepperPanList = [].slice.call(
      stepperFormEl.querySelectorAll('.bs-stepper-pane')
    );
  
    btnNextList.forEach(function(btn) {
      btn.addEventListener('click', function() {
        stepperForm.next();
      });
    });

    submitBtn = document.getElementById('form-submit-btn');
    submitBtn.addEventListener('click', function() {
      form.submit();
    });
  });
  





  function onValidate(groupname) {
    if (
      $('#appForm')
        .parsley()
        .validate({
          group: groupname
        })
    ) {
      console.log('valid');
      return true;
    } else {
      console.log(this);
      console.log('invalid');
      return false;
    }
  }



