document.addEventListener('DOMContentLoaded', function () {
    function CurrencyFormat(number) {
        let decimalplaces = 2;
        let decimalcharacter = ".";
        let thousandseparater = ",";
        number = parseFloat(number);
        let sign = number < 0 ? "-" : "";
        let formatted = new String(number.toFixed(decimalplaces));
        if( decimalcharacter.length && decimalcharacter != "." ) { formatted = formatted.replace(/\./,decimalcharacter); }
        let integer = "";
        let fraction = "";
        let strnumber = new String(formatted);
        let dotpos = decimalcharacter.length ? strnumber.indexOf(decimalcharacter) : -1;
        if( dotpos > -1 )
        {
            if( dotpos ) { integer = strnumber.substr(0,dotpos); }
            fraction = strnumber.substr(dotpos+1);
        }
        else { integer = strnumber; }
        if( integer ) { integer = String(Math.abs(integer)); }
        while( fraction.length < decimalplaces ) { fraction += "0"; }
        temparray = new Array();
        while( integer.length > 3 )
        {
            temparray.unshift(integer.substr(-3));
            integer = integer.substr(0,integer.length-3);
        }
        temparray.unshift(integer);
        integer = temparray.join(thousandseparater);
        return sign + integer + decimalcharacter + fraction;
    }
    let available = document.getElementById("available").innerText;
    formated = CurrencyFormat(available);
    document.getElementById("available").innerHTML = '$ ' + formated;
    let quantity = document.getElementsByClassName("amount");
    for (let index = 0; index < quantity.length; index++) {
        if (quantity[index].innerText[0] === '-') {
            amount = CurrencyFormat(quantity[index].innerText.split(' ')[1])
            document.getElementsByClassName("amount")[index].innerHTML = '$ - ' + amount;
        }
        else {
            amount = CurrencyFormat(quantity[index].innerText.split(' ')[1])
            document.getElementsByClassName("amount")[index].innerHTML = '$ ' + amount;
        }
    }
});
