function setCookie(name, value, iday) {
    var oDate = new Date();

    oDate.setDate(oDate.getDate() + iday);
    document.cookie = name + '=' + value + ';expires=' + oDate;
}

function getCookie(name) {
    var arr1 = document.cookie.split('; ');

    for (var i = 0; i < arr1.length; i++) {
        var arr2 = arr1[i].split('=');

        if (arr2[0] == name) {
            return arr2[1];
        }
    }

    return 'false';
}

function removeCookie(name){
    setCookie(name,1,-1);
}