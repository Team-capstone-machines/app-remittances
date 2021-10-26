function validateForm() {
    let name = document.forms["fields"]["nm"].value;
    let phone = document.forms["fields"]["pho"].value;
    let cash = document.forms["fields"]["csh"].value;
    if (phone && phone.length < 10 && !name && !cash) {
        $('#name').addClass('invalid');
        $('#phone').addClass('invalid');
        $('#cash').addClass('invalid');
        if ($('#no-length').length === 0) {
            $('#name-box').append('<p id="no-name">Campo obligatorio</p>');
            $('#phone-box').append('<p id="no-length">Debe ser al menos de 10 dígitos</p>');
            $('#cash-box').append('<p id="no-cash">Campo obligatorio</p>');
        }
        return false;
    }
    if (phone && phone.length < 10 && !name) {
        $('#name').addClass('invalid');
        $('#phone').addClass('invalid');
        if ($('#no-length').length === 0) {
            $('#name-box').append('<p id="no-name">Campo obligatorio</p>');
            $('#phone-box').append('<p id="no-length">Debe ser al menos de 10 dígitos</p>');
        }
        return false;
    }
    if (phone && phone.length < 10 && !cash) {
        $('#phone').addClass('invalid');
        $('#cash').addClass('invalid');
        if ($('#no-length').length === 0) {
            $('#phone-box').append('<p id="no-length">Debe ser al menos de 10 dígitos</p>');
            $('#cash-box').append('<p id="no-cash">Campo obligatorio</p>');
        }
        return false;
    }
    if (!name && !phone && !cash) {
        $('#name').addClass('invalid');
        $('#phone').addClass('invalid');
        $('#cash').addClass('invalid');
        if ($('#no-name').length === 0) {
            $('#name-box').append('<p id="no-name">Campo obligatorio</p>');
            $('#phone-box').append('<p id="no-phone">Campo obligatorio</p>');
            $('#cash-box').append('<p id="no-cash">Campo obligatorio</p>');
        }
        return false;
    }
    if (!name && !phone) {
        $('#name').addClass('invalid');
        $('#phone').addClass('invalid');
        if ($('#no-name').length === 0) {
            $('#name-box').append('<p id="no-name">Campo obligatorio</p>');
            $('#phone-box').append('<p id="no-phone">Campo obligatorio</p>');
        }
        return false;
    }
    if (!name && !cash) {
        $('#name').addClass('invalid');
        $('#cash').addClass('invalid');
        if ($('#no-name').length === 0) {
            $('#name-box').append('<p id="no-name">Campo obligatorio</p>');
            $('#cash-box').append('<p id="no-cash">Campo obligatorio</p>');
        }
        return false;
    }
    if (!phone && !cash) {
        $('#phone').addClass('invalid');
        $('#cash').addClass('invalid');
        if ($('#no-phone').length === 0) {
            $('#phone-box').append('<p id="no-phone">Campo obligatorio</p>');
            $('#cash-box').append('<p id="no-cash">Campo obligatorio</p>');
        }
        return false;
    }
    if (!name) {
        $('#name').addClass('invalid');
        if ($('#no-name').length === 0) {
            $('#name-box').append('<p id="no-name">Campo obligatorio</p>');
        }
        return false;
    }
    if (!phone) {
        $('#phone').addClass('invalid');
        if ($('#no-phone').length === 0) {
            $('#phone-box').append('<p id="no-phone">Campo obligatorio</p>');
        }
        return false;
    }
    if (!cash) {
        $('#cash').addClass('invalid');
        if ($('#no-cash').length === 0) {
            $('#cash-box').append('<p id="no-cash">Campo obligatorio</p>');
        }
        return false;
    }
    if (phone && phone.length < 10) {
        $('#phone').addClass('invalid');
        if ($('#no-length').length === 0) {
            $('#phone-box').append('<p id="no-length">Debe ser al menos de 10 dígitos</p>');
        }
        return false;
    }
}

function nameSuccess() {
    $('#name').removeClass('invalid');
    $('#no-name').remove();
}

function phoneSuccess() {
    let phone = document.forms["fields"]["pho"].value;
    if (phone.length > 9) {
        $('#no-length').remove();
    }
    $('#phone').removeClass('invalid');
    $('#no-phone').remove();
}

function cashSuccess() {
    let cash = document.forms["fields"]["csh"].value;
    if (!(/^[0-9]/g.test(cash))) {
        $('#cash').addClass('invalid');
    }
    $('#cash').removeClass('invalid');
    $('#no-cash').remove();
}
