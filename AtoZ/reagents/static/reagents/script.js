var phusion = [
    ['Forward Primer', 1],
    ['Reverse Primer', 1],
    ['2X Phusion Flash PCR Master Mix', 10],
    ['Template DNA', 1],
    ['Water', 7]
]

var toughmix = [
    ['Forward Primer', 0.75],
    ['Reverse Primer', 0.75],
    ['ToughMix PCR Master Mix', 12.5],
    ['Template DNA', 1],
    ['Water', 10]
]

var tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
var tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

function btnClick(polName, polList) {
    $(`#${polName}`).on('click', function () {
        $("#table-body").empty();
        const rxNum = $('#tentacles').val();    
        for (let i = 0; i < polList.length; i++) {
            let tableRow = $("<tr/>");
            tableRow.append($("<td>").text(i + 1));
            tableRow.append($("<td>").text(polList[i][0]));
            tableRow.append($("<td>").text(polList[i][1] * rxNum));
            $("#table-body").append(tableRow);
        };
        if (polName === 'phusion') {
            $('#perRxn').text('Volume per reaction: 19 µL.');
        } else if (polName === 'toughmix') {
            $('#perRxn').text('Volume per reaction: 24 µL.');
        }
    });
};

btnClick('phusion', phusion);
btnClick('toughmix', toughmix);



