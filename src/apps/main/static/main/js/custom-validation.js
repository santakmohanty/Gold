
window.Parsley
    .addValidator('checkmail', {
        requirementType: 'string',
        validateString : function (value, requirement) {

              var regex = /^([A-Za-z0-9_\-\.])+\@([A-Za-z0-9_\-\.])+\.([A-Za-z]{2,4})$/i;
              var emails = value.split(',');
              for ( var i = 0 ; i < emails.length ; i++){
                    if(!regex.test(emails[i])){
                        return false;
                    }
              }
              return true;
        },
        messages       : {
            en: "Please insert valid email",
        }
    });


window.Parsley
    .addValidator('plainText', {
        requirementType: 'string',
        validateString : function (value, requirement) {
              return /^[a-zA-Z][A-Za-z0-9 -#+]*$/i.test(value);
        },
        messages       : {
            en: "Name must contain only letters, numbers or dashes",
        }
    });


window.Parsley
    .addValidator('name', {
        requirementType: 'string',
        validateString : function (value, requirement) {
              return /^([^0-9]*)$/i.test(value);
        },
        messages       : {
            en: "Name must contain only letters",
        }
    });

window.Parsley
    .addValidator('city', {
        requirementType: 'string',
        validateString : function (value, requirement) {
              return /^[a-zA-Z][A-Za-z0-9-]*$/i.test(value);
        },
        messages       : {
            en: "Value must be valid",
        }
    });

window.Parsley
    .addValidator('contact', {
        requirementType: 'string',
        validateString : function (value, requirement) {
              return /^[0-9]{10}*$/i.test(value);
        },
        messages       : {
            en: "Value must be valid",
        }
    });

window.Parsley
    .addValidator('normalText', {
        requirementType: 'string',
        validateString : function (value, requirement) {
            return /^[a-zA-Z0-9-)(,&'. ]{0,150}$/i.test(value);
        },
        messages       : {
            en: "The field can only have letters, numbers, - , & , (, ) and '.",
        }
    });


window.Parsley
    .addValidator('noSpace', {
        requirementType: 'string',
        validateString : function (value, requirement) {
            return value.indexOf(" ") < 0 && value !== "";
        },
        messages       : {
            en: "Space in between not allowed.",
        }
    });

window.Parsley
    .addValidator('noLTSpace', {
        requirementType: 'string',
        validateString : function (value, requirement) {
            return !(/^[ \s]+|[ \s]+$/i.test(value));
        },
        messages       : {
            en: "Leading and Trailing space is not allowed.",
        }
    });

window.Parsley
    .addValidator('password', {
        requirementType: 'string',
        validateString : function (value, requirement) {
            return value.indexOf(" ") === -1;
        },
        messages       : {
            en: "Space is not allowed.",
        }
    });

window.Parsley
    .addValidator('textDate', {
        requirementType: 'string',
        validateString : function (value, requirement) {
            return (/^([0-2][0-9]|(3)[0-1])(\-)(((0)[0-9])|((1)[0-2]))(\-)\d{4}$/i.test(value));
        },
        messages       : {
            en: "Invalid Date or Date Format",
        }
    });

window.Parsley
    .addValidator('smallerThan', {
        requirementType: 'integer',
        validateNumber : function (value, requirement) {
            return value < requirement
        },
        messages       : {
            en: "Enter a number less than %s",
        }
    });

window.Parsley.addValidator('filemimetypes', {
    requirementType: 'string',
    validateString : function (value, requirement, parsleyInstance) {

        var fileList = parsleyInstance.$element[0].files;
        if (fileList.length === 0) {
            return true;
        }
        var allowedMimeTypes = ['pdf', 'jpeg', 'png', 'jpg', 'docx', 'doc'];
        var isValid = true;
        Object.keys(fileList).forEach(function (file, index) {
            console.log(fileList[index].type, "DEBUG");
            var fileName = fileList[index].name.split(".");
            var fileExtension = fileName[fileName.length - 1];
            if (!allowedMimeTypes.includes(fileExtension)) {
                isValid = false;
                return;
            }
        });
        return isValid;
    },
    messages       : {
        en: 'Only .pdf, .jpeg, .png, .jpg, .docx, .doc  files are allowed.'
    }
});

window.Parsley.addValidator('filesize', {
    requirementType: 'string',
    validateString : function (value, requirement, parsleyInstance) {

        var fileList = parsleyInstance.$element[0].files;
        if (fileList.length === 0) {
            return true;
        }
        var isValid = true;
        var totalSize = 0;
        Object.keys(fileList).forEach(function (file, index) {
            totalSize += fileList[index].size;
        });
        if (totalSize > 1048576) {
            isValid = false;
        }

        return isValid;
    },
    messages       : {
        en: 'Upload files size exceeds max upload size 1MB.'
    }
});