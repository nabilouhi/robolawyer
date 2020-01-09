function UrlExists(url) {
  var http = new XMLHttpRequest();
  http.open('HEAD', url, false);
  http.withCredentials = true;
  http.setRequestHeader('Content-Type', 'application/json');
  http.send();
  try {
    baseUrl = url;
    echrRat(baseUrl);
    courtCountry(baseUrl);
  } catch (error) {
    console.error(error);
  }
}

var echrRat = function(baseUrl) {
  var echrUrl = baseUrl + 'api/echr/';

  var echrDiv = document.getElementById('echrDetails');
  $('#decisionDate').on('change', function() {
    currentSelected = $(this).val();
    if(moment(currentSelected, 'DD/MM/YYYY')._isValid){
    console.log();
        while (echrDiv.hasChildNodes()) {
      echrDiv.removeChild(echrDiv.lastChild);
    }
    axios({
      method: 'get',
      url: echrUrl
    }).then(function(response) {
      data = response.data;
      currentSelected.forEach(countryName => {
        for (var i = 0; i < data.length; i++) {
          if (data[i].country == countryName) {
            ratDate = data[i].ratDate;
            formattedDate = moment(ratDate).format('DD MMMM YYYY');
            var countryname = countryName.split('-');
            formattedCountryName = countryname[1].trim();

            var pTag = document.createElement('p');
            var p2Tag = document.createElement('p');
            finalText =
              '<b>' +
              formattedCountryName +
              '</b>' +
              ' ratified the European Convention on Human Rights and its Protocols on <b>' +
              formattedDate +
              '</b>. If the act, decision or omission take place after ' +
              formattedDate +
              ', but the effects of the act, decision or omission still continue to the present day (eg: the act of a disappearance, where the person has not been found, even if the person can be presumed dead), please continue to the next field.<br>';
            p2Tag.innerHTML += finalText;
            textReady = pTag.appendChild(p2Tag);
            appendedP = echrDiv.appendChild(textReady);
          }
        }
      });
    });
  }
  });
};

var courtCountry = function(baseUrl) {
  var courtUrl = baseUrl + 'api/court/';
  $('#decisionDate').on('change', function() {
    currentSelected = $('#involvedStates').val();
    while (courtData.hasChildNodes()) {
      courtData.removeChild(courtData.lastChild);
    }
    axios({
      method: 'get',
      url: courtUrl,
      crossorigin: true
    }).then(function(response) {
      data = response.data;
      courtData = document.getElementById('courtData');
      currentSelected.forEach(country => {
        for (var i = 0; i < data.length; i++) {
          countryArray = country.split('-');
          countryName = countryArray[1].trim();

          if (data[i].country == countryName) {
            courtDetail1 = document.createElement('tr');

            countryRow = document.createElement('td');
            countryRow.innerHTML = '<strong>' + data[i].country + '</strong>';
            courtDetail1.appendChild(countryRow);

            proceedingRow1 = document.createElement('td');
            proceedingRow1.innerHTML =
               data[i].proceedingType1 ;
            courtDetail1.appendChild(proceedingRow1);

            courtRow1 = document.createElement('td');
            courtRow1.innerHTML = data[i].court1;
            courtDetail1.appendChild(courtRow1);
            courtData.appendChild(courtDetail1);

            if (data[i].proceedingType2) {
              countryRow.setAttribute('rowspan', 2);
              countryRow.setAttribute('style', 'vertical-align:middle');
              courtDetail2 = document.createElement('tr');
              proceedingRow2 = document.createElement('td');
              proceedingRow2.innerHTML =
                data[i].proceedingType2;
              courtDetail2.appendChild(proceedingRow2);
              courtRow2 = document.createElement('td');
              courtRow2.innerHTML = data[i].court2;
              courtDetail2.appendChild(courtRow2);
              courtData.appendChild(courtDetail2);
            }

            if (data[i].proceedingType3) {
              countryRow.setAttribute('rowspan', 3);
              countryRow.setAttribute('style', 'vertical-align:middle');
              courtDetail3 = document.createElement('tr');
              proceedingRow3 = document.createElement('td');
              proceedingRow3.innerHTML = data[i].proceedingType3;
              courtDetail3.appendChild(proceedingRow3);
              courtRow3 = document.createElement('td');
              courtRow3.innerHTML = data[i].court3;
              courtDetail3.appendChild(courtRow3);
              courtData.appendChild(courtDetail3);
            }
          }
        }
      });
    });
  });
};

rootUrl = window.location.href.split('form/')[0];
UrlExists(rootUrl);
