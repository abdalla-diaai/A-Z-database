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
        };
    });
};



function otherClick() {
    $('#other').on('click', function () {
        $("#table-body").empty();
        const rxNum = $('#tentacles').val();    
        const other = $('#form-labels').val().split(',');
        let otherVol;
        for (let i = 0; i < other.length; i++) {
            let tableRow = $("<tr/>");
            tableRow.append($("<td>").text(i + 1));
            otherVol = other[i].split(' ');
            console.log(otherVol);
            tableRow.append($("<td>").text(otherVol[0]));
            tableRow.append($("<td>").text(parseInt(otherVol[1]) * rxNum));
            $("#table-body").append(tableRow);
        };
    });
};

const tooltipTriggerList = $('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

document.addEventListener('DOMContentLoaded', () => {
    const phusionList = [
        ['Forward Primer', 1],
        ['Reverse Primer', 1],
        ['2X Phusion Flash PCR Master Mix', 10],
        ['Template DNA', 1],
        ['Water', 7]
    ]
    
    const toughmixList = [
        ['Forward Primer', 0.75],
        ['Reverse Primer', 0.75],
        ['ToughMix PCR Master Mix', 12.5],
        ['Template DNA', 1],
        ['Water', 10]
    ]

btnClick('phusion', phusionList);
btnClick('toughmix', toughmixList);
otherClick();
});

$(document).ready(function() {
    $('#filter-table').bootstrapTable({
        filterControl: true
    });
});