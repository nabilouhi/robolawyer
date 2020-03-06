currentStep = 0

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
      console.log(event.detail)
      stepDifference = event.detail.to - currentStep
      if (event.detail.to <= currentStep) {
        if (event.detail.from != currentStep) {
          if(!checkValidation(event.detail.from)){
            currentStep = event.detail.from
            // stepperForm.to(event.detail.from+1);
            swal('Please answer the mandatory fields first.');
          event.preventDefault();
        } 
        }
        // console.log("stepDifference - "+currentStep);
        // console.log("currentStep - "+ currentStep)
        // console.log("going to earlier page");
      }
      else if (stepDifference === 1){
        // next from current page, validation required
        if(!checkValidation(currentStep)){
          swal('Please answer the mandatory fields first.');
          event.preventDefault();
        }
        else{
          currentStep = Math.max(currentStep, event.detail.to);
          // console.log("current step - "+currentStep);
        }
      }
      else {
        // console.log(currentStep);
        stepperForm.to(currentStep+1);
        swal('Please answer the mandatory fields first.');
          event.preventDefault();
      }
    });
    
    stepperFormEl.addEventListener('shown.bs-stepper', function(event) {

      currentStep = Math.max(currentStep, event.detail.to);
      console.log("currentStep shown - ", currentStep);
      console.log("to shown - ", event.detail.to);
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



  function checkValidation(cur) {
    if (cur===0) { 
      if (onValidate('page1')) {
        console.log('page1 passed');
        return true;
      // }
    } else if (cur === 1) {
        if(onValidate('page2')){
            console.log('page2 passed');
            appVal = document.querySelector("input[name='page2[applicantType]']:checked").value;
            if (appVal === 'Individual') {
              if (onValidate('page2a')) {
                console.log('page2a passed');
                return true;
              } 
            } else if (appVal === 'Organisation') {
              if (onValidate('page2b')) {
                console.log('page2b passed');
                return true;
              } 
            } else {
              console.log('check for bug');
            }
        } 
    } else if (cur === 2) {
        appVal1 = document.querySelector("input[name='page2[applicantType]']:checked").value;
            console.log(appVal1);
            if (appVal1 === 'Individual'){
              if (onValidate('page3a')){
                appVal2 = document.querySelector("input[name='page3[indRepresentativeType]']:checked").value;
                  console.log('page3a passed');
                
                  if (appVal2 === 'non-lawyer'){
                  if(onValidate('page3b')) {
                    console.log('page3b passed');
                    return true;
                  }
                }
                else if (appVal2 === 'lawyer'){
                  if(onValidate('page3c')){
                    console.log('page3c passed');
                    return true;
                  } 
                } else if (appVal2 === 'selfRepresented') {
                  return true;
                }
                else{
                  console.log("problem in page 3 individual validation");
                }
              }
            }
            else{
              if (onValidate('page3d')){
                console.log('page 3d passed');
                if (onValidate('page3e')){
                  console.log('page 3e passed');
                  if (onValidate('page3f')){
                    console.log('page 3f passed');
                return true;
              }
            }
          }
            }
    } else if (cur === 3) {
      if (onValidate('page4')) {
        console.log('page4 passed');
        return true;
      } 
    } else if (cur === 4) {
      if (onValidate('page5')) {
        console.log('page5 passed');
        return true;
      } 
    } else if (cur === 5) {
      if (onValidate('page6')) {
        console.log('page6 passed');
        return true;
      } 
    } else if (cur === 6) {
      if (onValidate('page7')) {
        console.log('page7 passed');
        return true;
      } 
    } else if (cur === 7) {
        if (onValidate('page8')) {
          console.log('page8 passed');
          return true;
        } 
      } else if (cur === 8) {
          if (onValidate('page9a')) {
            appVal = document.querySelector("input[name='page9[signatureDeclaration]']:checked").value;
            if (appVal === 'Applicant') {
              if (onValidate('page9b')) {
                console.log('page9b passed');
                return true;
              }
            }
            else{
              if (onValidate('page9c')) {
                console.log('page9c passed');
                return true;
              }
            }
            console.log('page 9 passed');
            
            
            return true;
          } 
        }
        return false;
      }