echrUrl = 'https://localhost:8000/api/ehcr/';
$('#involvedStates').on('change', function() {
  axios({
    method: 'get',
    url: echrUrl,
    responseType: 'stream'
  }).then(function(response) {
    console.log(response);
  });
});
