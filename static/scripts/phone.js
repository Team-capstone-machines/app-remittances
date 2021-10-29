document.addEventListener('DOMContentLoaded', function () {
  function getIp(callback) {
    fetch('https://ipinfo.io/json?token=ae0968f71ab1ef', { headers: { 'Accept': 'application/json' }})
    .then((resp) => resp.json())
    .catch(() => {
      return {
        country: 'us',
      };
    })
    .then((resp) => callback(resp.country));
  }
  const phoneInputField = document.querySelector("#phone");
  phoneInput = window.intlTelInput(phoneInputField, {
    initialCountry: "mx",
    preferredCountries: ["us", "co", "mx", "de", "au"],
    // geoIpLookup: getIp,
    utilsScript:
    "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
  });
});
function process(event) {
  /* event.preventDefault();
  const phoneNumber = phoneInput.getNumber();
  console.log(phoneInput.s.dialCode);
  console.log(phoneNumber.split('+')[1]); */
  phone = phoneInput.getNumber().split('+')[1];
  $.ajax({
    type: "POST",
    contentType: 'application/json',
    dataType: "json",
    url: "http://172.25.203.244:5000/get_phone?value="+phone,
    success: function (response) {
      let reply = response.reply;
      if (reply=="success") {
        return;
      } else {
        alert("BAD");
      }
    }
  });
}
