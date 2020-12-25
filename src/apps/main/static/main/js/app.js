window.app = new APP();
window.APP = APP;

$.ajaxSetup({
    headers: {
        "X-CSRF-TOKEN": $('meta[name="csrf-token"]').attr('content')
    },
    error: function (x, status, error) {
        if (x.status == 500) {
            app.displayErrorMessage(
                "Something went wrong, Please report this to the administrator."
            );
        }
    }

});

APP.prototype.getURLParamValue = function (key) {
    var results = new RegExp("[?&]" + name + "=([^]*)").exec(
        window.location.href
    );
    if (results == null) {
        return null;
    } else {
        return results[1] || 0;
    }
};

APP.prototype.isSet = function (key) {
    if (
        key &&
        key != "null" &&
        key != "undefined" &&
        key != undefined &&
        key != null &&
        key != ""
    ) {
        return true;
    }
    return false;
};

APP.prototype.resetForm = function ($form) {
    $("input", $form).val("");
    $("option", $form).attr("selected", false);
    $("textarea", $form).val("");
};

APP.prototype.setValidationRules = function () {
    var forms = $("form");
    forms.each(function (i) {
        if (i === forms.length - 1) {
            $("this").validate({
                highlight: function (input) {
                    $(input)
                        .parents(".form-line")
                        .addClass("error");
                },
                unhighlight: function (input) {
                    $(input)
                        .parents(".form-line")
                        .removeClass("error");
                },
                errorPlacement: function (error, element) {
                    $(element)
                        .parents(".form-group")
                        .append(error);
                }
            });
        }
    });
};

APP.prototype.initTextareaAutogrow = function () {
    $.each($('textarea'), function () {
        $(this).autogrow();
    });
};

APP.prototype.generateSlug = function (text) {
    return text.toString().toLowerCase()
        .replace(/\s+/g, '-')           // Replace spaces with -
        .replace(/[^\w\-]+/g, '')       // Remove all non-word chars
        .replace(/\-\-+/g, '-')         // Replace multiple - with single -
        .replace(/^-+/, '')             // Trim - from start of text
        .replace(/-+$/, '');            // Trim - from end of text
};

APP.prototype.initDatePicker = function (elementSelector, type) {
    flatpickr(elementSelector, {
        mode: type,
        dateFormat: "Y-m-d",
        disable: [
            function (date) {
                // disable every multiple of 8
                return !(date.getDate());
            }
        ]
    });
};

APP.prototype.attachMultipleSelect = function (option) {
    $('.dynamicSelectMultiple').select2(option);
};

APP.prototype.initDatatable = function (tabelId) {
    $(tabelId).DataTable({
        "sort": false,
    });

};

APP.prototype.handleFileSelect = function () {
    $(".fileInput").on('change', function () {
        var filePath = this.value;
        $(this).parent().find(".selectedFile").html(filePath.split(/(\\|\/)/g).pop());
    })
};

APP.prototype.handleFormSubmit = function () {
    $("form").on('submit', function () {
        var $submitBtn = $('button[type="submit"]', $(this));
        $submitBtn.attr('disabled', true);
    });
};

APP.prototype.autoCloseAlert = function () {
    $('.alert').delay(2500).slideUp(300);
};

APP.prototype.getDefaultDatatableOptions = function (excelTitle, excelMessage) {
    return {
        responsive: true,
        ordering: false,
        pagingType: 'full_numbers',
        destroy: true,
        language: {
            processing: "<div class='text-center'>Loading...</div>"
        },
        processing: true,
        dom: "Blftrip",
        buttons: [
            {
                extend: 'excel',
                exportOptions: {
                    columns: 'th:not(:last-child)'
                },
                title: excelTitle,
                message: excelMessage
            }
        ],
    };

};

APP.prototype.defaultValidationOptions = function () {
    return {
        errorClass: 'is-invalid text-danger',
        errorsWrapper: '<div class="form-text text-danger"></div>',
        errorTemplate: '<div></div>',
        trigger: 'change'
    }
};

APP.prototype.initSelect2 = function () {
    $('.select2').select2({
        allowClear: true,
        closeOnSelect: true,
    });
};

APP.prototype.initTooltip = function () {
    $('[data-toggle="tooltip"]').tooltip();
}

APP.prototype.getMonthNameFromNumber = function (monthNumber) {
    var months = [
        'January', 'February', 'March', 'April', 'May',
        'June', 'July', 'August', 'September',
        'October', 'November', 'December'
    ];

    return months[monthNumber - 1] || '';
};

function initializeFieldInputs() {
    $.fn.inputFilter = function (inputFilter) {
        return this.on("input keydown keyup mousedown mouseup select contextmenu drop", function () {
            if (inputFilter(this.value)) {
                this.oldValue = this.value;
                this.oldSelectionStart = this.selectionStart;
                this.oldSelectionEnd = this.selectionEnd;
            } else if (this.hasOwnProperty("oldValue")) {
                this.value = this.oldValue;
                this.setSelectionRange(this.oldSelectionStart, this.oldSelectionEnd);
            } else {
                this.value = "";
            }
        });
    };
}

// Example
// $('.class-name').inputFilter(function (value) {
//     return /^[0-9]*$/i.test(value);
// })
initializeFieldInputs(); // For using  input filter 


jQuery(function () {
    // app.initSelect2(); // uncomment if using select2
    app.initTooltip();
    app.autoCloseAlert();
});
