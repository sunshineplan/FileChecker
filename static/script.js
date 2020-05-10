function copyResult() {
    result = document.getElementById('output');
    result.select();
    document.execCommand('Copy');
    result.setSelectionRange(0, 0);
    if (result.value !== '') {
        alert('Text has been copied to clipboard.');
    }
}

function clearAll() {
    $('#inputA').val('');
    $('#inputB').val('');
    $('#output').val('');
}

function swap() {
    data1 = $('#inputA').val();
    data2 = $('#inputB').val();
    $('#inputA').val(data2);
    $('#inputB').val(data1);
}

function processing() {
    $('#output').val('Processing');
    setTimeout(function () {
        $('#output').val('Processing.');
    }, 250);
    setTimeout(function () {
        $('#output').val('Processing..');
    }, 500);
    setTimeout(function () {
        $('#output').val('Processing...');
    }, 750);
}

$(document).ajaxSend(function() {
    processing();
    process = setInterval(function() {
        processing();
    }, 1000);
}).ajaxComplete(function() {
    clearInterval(process);
}).ajaxError(function() {
    setTimeout(function() {
        $('#output').val('Oops, we encountered a problem! Please contact your administrator for assistance.');
    }, 800);
});

window.onload = function () {
    data1 = localStorage.getItem('data1');
    if (data1 !== null) $('#inputA').val(data1);
    data2 = localStorage.getItem('data2');
    if (data2 !== null) $('#inputB').val(data2);
}

window.onbeforeunload = function () {
    localStorage.setItem('data1', $('#inputA').val());
    localStorage.setItem('data2', $('#inputB').val());
}
