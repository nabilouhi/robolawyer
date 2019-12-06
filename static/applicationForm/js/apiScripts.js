function UrlExists(url) {
  var http = new XMLHttpRequest();
  http.open('HEAD', url, false);
  http.withCredentials = true;
  http.setRequestHeader('Content-Type', 'application/json');
  http.send();
  console.log('it reached here');
  if (http.status == 200) {
    baseUrl = url;
    console.log(baseUrl);
    echrRat(baseUrl);
    courtCountry(baseUrl);
  } else {
    baseUrl = 'http://localhost:8000/';
    console.log(url);
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
      courtElement = document.getElementById('courtData');
      currentSelected.forEach(country => {
        for (var i = 0; i < data.length; i++) {
          countryArray = country.split('-');
          countryName = countryArray[1].trim();

          if (data[i].country == countryName) {
            courtDetail = document.createElement('tr');

            countryRow = document.createElement('td');
            countryRow.innerHTML = data[i].country;
            courtDetail.appendChild(countryRow);

            proceedingRow = document.createElement('td');
            proceedingRow.innerHTML = data[i].proceedingType;
            courtDetail.appendChild(proceedingRow);

            courtRow = document.createElement('td');
            courtRow.innerHTML = data[i].court;
            courtDetail.appendChild(courtRow);

            courtElement.appendChild(courtDetail);
          }
        }
      });
    });
  });
};

url = 'https://robo2lawyer.herokuapp.com/';
// url = 'http://localhost:8000/';
UrlExists(url);
