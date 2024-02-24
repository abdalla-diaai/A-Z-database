var phusion = [
    ['Forward Primer', 1],
    ['Reverse Primer', 1],
    ['2X Phusion Flash PCR Master Mix', 10],
    ['Template DNA', 1],
    ['Water', 7]
]

$('#add-field').on('click', function () {
    const rxNum = $('#tentacles').val();
    console.log(rxNum);

    for (let i = 0; i < phusion.length; i++) {
        let tableRow = $("<tr/>");
        tableRow.append($("<td>").text(i + 1));
        tableRow.append($("<td>").text(phusion[i][0]));
        tableRow.append($("<td>").text(phusion[i][1] * rxNum));
        $("#table-body").append(tableRow);
    };
    $('#perRxn').text('Volume per reaction: 19 µL.');
});


