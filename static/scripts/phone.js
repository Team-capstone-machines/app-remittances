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
    const phoneInput = window.intlTelInput(phoneInputField, {
        initialCountry: "auto",
        preferredCountries: ["us", "co", "mx", "de", "au"],
        geoIpLookup: getIp,
        utilsScript:
        "https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js",
    });
});
