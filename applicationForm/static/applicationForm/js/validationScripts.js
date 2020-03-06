currentStep = 0

document.addEventListener('DOMContentLoaded', function() {
    var stepperFormEl = document.querySelector('#stepperForm');
    stepperForm = new Stepper(stepperFormEl, {
      animation: true,
      linear: false,
      excluded:
        'input[type=button], input[type=submit], input[type=reset], input[type=hidden], :disabled'
    });
    var form = stepperFormEl.querySelector('.bs-stepper-content form');
    stepperFormEl.addEventListener('show.bs-stepper', function(event) {
      stepDifference = event.detail.to - currentStep;
      if (event.detail.to <= currentStep) {
        if (event.detail.from != currentStep) {
          if(!checkValidation(event.detail.from)){
            currentStep = event.detail.from;
            // stepperForm.to(event.detail.from+1);
            swal('Please answer the mandatory fields first.');
          event.preventDefault();
        } 
        }
      }
      else if (stepDifference === 1){
        // next from current page, validation required
        if(!checkValidation(currentStep)){
          swal('Please answer the mandatory fields first.');
          event.preventDefault();
        }
        else{
          currentStep = Math.max(currentStep, event.detail.to);
        }
      }
      else {
        stepperForm.to(currentStep+1);
        swal('Please answer the mandatory fields first.');
          event.preventDefault();
      }
    });
    
    stepperFormEl.addEventListener('shown.bs-stepper', function(event) {

      currentStep = Math.max(currentStep, event.detail.to);
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
      return true;
    } else {
      return false;
    }
  }



  function checkValidation(cur) {
    if (cur===0) { 
      if (onValidate('page1')) {
        return true;
      }
    } else if (cur === 1) {
        if(onValidate('page2')){
            appVal = document.querySelector("input[name='page2[applicantType]']:checked").value;
            if (appVal === 'Individual') {
              if (onValidate('page2a')) {
                return true;
              } 
            } else if (appVal === 'Organisation') {
              if (onValidate('page2b')) {
                return true;
              } 
            } else {
            }
        } 
    } else if (cur === 2) {
        appVal1 = document.querySelector("input[name='page2[applicantType]']:checked").value;
            if (appVal1 === 'Individual'){
              if (onValidate('page3a')){
                appVal2 = document.querySelector("input[name='page3[indRepresentativeType]']:checked").value;                
                  if (appVal2 === 'non-lawyer'){
                  if(onValidate('page3b')) {
                    return true;
                  }
                }
                else if (appVal2 === 'lawyer'){
                  if(onValidate('page3c')){
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
                if (onValidate('page3e')){
                    appVal = document.querySelector("input[name='page3[orgRepresentativeType]']:checked").value;
                    if (appVal === 'orgYesLawyer'){
                      if (onValidate('page3f')){
                        return true;
                        }
                     }
                    return true;
                }
               }
            }
    } else if (cur === 3) {
      if (onValidate('page4')) {
        return true;
      } 
    } else if (cur === 4) {
      if (onValidate('page5')) {
        return true;
      } 
    } else if (cur === 5) {
      if (onValidate('page6')) {
        return true;
      } 
    } else if (cur === 6) {
      if (onValidate('page7a')) {
        appVal = document.querySelector("input[name='page7[intInvestigation]']:checked").value;
        if (appVal === 'Yes'){
          if (onValidate('page7b')) {
            return true;
          }
        }
        else {
          return true;
        }
      }
      if (onValidate('page7c')) {
        appVal = document.querySelector("input[name='page7[prevApplications]']:checked").value;
        if (appVal === 'Yes'){
          if (onValidate('page7d')) {
            return true;
          }
        } 
        else {
          return true;
        }
      }
    } else if (cur === 7) {
        if (onValidate('page8')) {
          return true;
        } 
      } else if (cur === 8) {
          if (onValidate('page9a')) {
            appVal = document.querySelector("input[name='page9[signatureDeclaration]']:checked").value;
            if (appVal === 'Applicant') {
              if (onValidate('page9b')) {
                return true;
              }
            }
            else{
              if (onValidate('page9c')) {
                return true;
              }
            }
          } 
        }
        return false;
      }
    
  