$(document).ready(function(){
    var select = $("#yearpicker");
    for(var i = 2003; i >=1900; i--){
        select.append(`<option value="${i}">${i}</option>`);
    }
});
