function UrlExists(url) {
  rootUrl = window.location.href.split('form/')[0];
  console.log(rootUrl);
  var http = new XMLHttpRequest();
  http.open('HEAD', url, false);
  http.withCredentials = true;
  http.setRequestHeader('Content-Type', 'application/json');
  http.send();
  console.log('it reached here');
  if (http.status == 200) {
    baseUrl = url;
    console.log('baseURL ' + baseUrl);
    echrRat(baseUrl);
    courtCountry(baseUrl);
  } else {
    baseUrl = 'http://localhost:8000/';
    console.log('url ' + url);
    echrRat(url);
    courtCountry(url);
  }
}

var echrRat = function(baseUrl) {
  var echrUrl = baseUrl + 'api/echr/';

  var echrDiv = document.getElementById('echrDetails');
  $('#involvedStates').on('change', function() {
    currentSelected = $(this).val();
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
            var smallTag = document.createElement('small');
            finalText =
              '<b>' +
              formattedCountryName +
              '</b>' +
              ' ratified the European Convention on Human Rights and its Protocols on <b>' +
              formattedDate +
              '</b>. If the act, decision or omission take place after ' +
              formattedDate +
              ', but the effects of the act, decision or omission still continue to the present day (eg: the act of a disappearance, where the person has not been found, even if the person can be presumed dead), please continue to the next field.<br>';
            smallTag.innerHTML += finalText;
            textReady = pTag.appendChild(smallTag);
            appendedP = echrDiv.appendChild(textReady);
          }
        }
      });
    });
  });
};

var courtCountry = function(baseUrl) {
  var courtUrl = baseUrl + 'api/court/';
  $('#involvedStates').on('change', function() {
    currentSelected = $(this).val();
    while (courtData.hasChildNodes()) {
      courtData.removeChild(courtData.lastChild);
    }
    axios({
      method: 'get',
      url: courtUrl,
      crossorigin: true
    }).then(function(response) {
      data = response.data;
      console.log(data);
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
              '<em>' + data[i].proceedingType1 + '</em>';
            courtDetail1.appendChild(proceedingRow1);

            courtRow1 = document.createElement('td');
            courtRow1.innerHTML = '<em>' + data[i].court1 + '</em>';
            courtDetail1.appendChild(courtRow1);
            courtData.appendChild(courtDetail1);

            if (data[i].proceedingType2) {
              countryRow.setAttribute('rowspan', 2);
              countryRow.setAttribute('style', 'vertical-align:middle');
              courtDetail2 = document.createElement('tr');
              proceedingRow2 = document.createElement('td');
              proceedingRow2.innerHTML =
                '<em>' + data[i].proceedingType2 + '</em>';
              courtDetail2.appendChild(proceedingRow2);
              courtRow2 = document.createElement('td');
              courtRow2.innerHTML = '<em>' + data[i].court2 + '</em>';
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

// url = 'https://robo2lawyer.herokuapp.com/';
url = 'http://localhost:8000/';

UrlExists(url);
