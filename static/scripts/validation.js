function validateForm() {
    let name = document.forms["fields"]["nm"].value;
    let phone = document.forms["fields"]["pho"].value;
    if (!name && !phone) {
        $('#name').addClass('invalid');
        $('#phone').addClass('invalid');
        if ($('#p_name').length === 0) {
            $('#name_box').append('<p id="p_name">Campo obligatorio</p>');
            $('#phone_box').append('<p id="p_phone">Campo obligatorio</p>');
        }
        return false;
    }
    if (phone.length < 10 && !name) {
        $('#name').addClass('invalid');
        $('#phone').addClass('invalid');
        if ($('#v_pho').length === 0) {
            $('#phone_box').append('<p id="v_pho">Debe ser al menos de 10 dígitos</p>');
        }
        if ($('#p_name').length === 0) {
            $('#name_box').append('<p id="p_name">Campo obligatorio</p>');
        }
        return false;
    }
    if (!name) {
        $('#name').addClass('invalid');
        if ($('#p_name').length === 0) {
            $('#name_box').append('<p id="p_name">Campo obligatorio</p>');
        }
        return false;
    }
    if (!phone) {
      $('#phone').addClass('invalid');
      if ($('#p_phone').length === 0) {
        $('#phone_box').append('<p id="p_phone">Campo obligatorio</p>');
      }
      return false;
    }
    if (phone && phone.length < 10) {
        $('#v_pho').addClass('invalid');
        if ($('#v_pho').length === 0) {
            $('#phone_box').append('<p id="v_pho">Debe ser al menos de 10 dígitos</p>');
        }
        return false;
    }
}

function success_name() {
    $('#p_name').remove();
    $('#name').removeClass('invalid');
}

function success_phone() {
    let phone = document.forms["fields"]["pho"].value;
    if (phone.length > 8) {
        $('#v_pho').remove();
    }
    $('#p_phone').remove();
    $('#phone').removeClass('invalid');
}
