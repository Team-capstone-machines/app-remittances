document.addEventListener('DOMContentLoaded', function () {
  let currencyInput = document.querySelector('input[type="currency"]')
  let currency = 'USD' // https://www.currency-iso.org/dam/downloads/lists/list_one.xml

  // format inital value
  onBlur({target:currencyInput})

  // bind event listeners
  currencyInput.addEventListener('focus', onFocus)
  currencyInput.addEventListener('blur', onBlur)


  function localStringToNumber( s ){
    return Number(String(s).replace(/[^0-9.-]+/g,""))
  }

  function onFocus(e){
    let value = e.target.value;
    e.target.value = value ? localStringToNumber(value) : ''
  }

  function onBlur(e){
    let value = e.target.value

    let options = {
        maximumFractionDigits : 2,
        currency              : currency,
        style                 : "currency",
        currencyDisplay       : "symbol"
    }
    
    e.target.value = (value || value === 0) 
      ? localStringToNumber(value).toLocaleString(undefined, options)
      : ''
  }
})
