function validateForm() {
    let name = document.forms["fields"]["nm"].value;
    let phone = document.forms["fields"]["pho"].value;
    if (!name && !phone) {
      $('#name').addClass('invalid');
      $('#phone').css({"border": "1px solid #FA5C7C"});
      $('#name_box').append('<p id="p_name">Campo obligatorio</p>');
      $('#phone_box').append('<p id="p_phone">Campo obligatorio</p>');
      return false;
    }
    if (!name) {
      $('#name').css({"border": "1px solid #FA5C7C"});
      $('#name_box').append('<p id="p_name">Campo obligatorio</p>');
      return false;
    }
    if (!phone) {
      $('#phone').css({"border": "1px solid #FA5C7C"});
      $('#phone_box').append('<p id="p_phone">Campo obligatorio</p>');
      return false;
    }
}

function success_name() {
    $('#p_name').remove();
    $('#name').removeClass('invalid');
}

function success_phone() {
    $('#p_phone').remove();
    $('#phone').removeClass('invalid');
}
