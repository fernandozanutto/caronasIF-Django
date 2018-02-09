// Example starter JavaScript for disabling form submissions if there are invalid fields
$(function() {
    'use strict';

    var forms = $('.needs-validation');

    forms.submit(function(e){
        if(this.checkValidity() === false){
            e.preventDefault()
            e.stopPropagation()
        }
        $(this).addClass('was-validated')
    })
})
