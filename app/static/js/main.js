
function deletePitch(pitchId) {
    fetch('/delete-pitch', {
        method: 'POST',
        body: JSON.stringify({
            pitchId: pitchId
        })
    }).then((_res) => {
        window.location.href = "/dashboard";
    })
}

$(function () {
    $(".like").click(function () {
        var input = $(this).find('.qty1');
        input.val(parseInt(input.val()) + 1);
    });

    $(".dislike").click(function () {
        var input = $(this).find('.qty2');
        input.val(input.val() - 1);
    });
});

$(document).ready(function () {

    // Hide the div
    $(".alert").hide();

    // Show the div in 5s
    $(".alert").delay(3000).fadeIn(1000);

});