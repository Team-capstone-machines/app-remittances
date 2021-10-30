function toInt(str) {
    str = str.split('$')[1].split('.')[0];
    return str.split(',').join('');
}

document.addEventListener('DOMContentLoaded', function () {
    /* function toInt(str) {
        str = str.split(' ')[1].split('.')[0];
        return str.split(',').join('');
    } */
    const ava = toInt(document.getElementById("available").innerHTML);
});

console.log(ava);

function validateBalance() {
    let req = toInt(document.forms["cash-balance"]["cash"].value);
    if (parseInt(req) > parseInt(ava)) {
        $('#invalid').addClass('no-valid');
        if ($('#cash-box').length === 0) {
            $('#cash-box').append('<p id="invalid">Monto Inválido</p>');
        }
    }
}
