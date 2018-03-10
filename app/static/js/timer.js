
// set initial value for the minutes variable
var Minutes = -1;

$(document).ready(function() {

    // timer function
    function startTimer(duration, display) {
        var timer = duration, minutes, seconds;
        var refresh = setInterval(function () {
            minutes = parseInt(timer / 60, 10)
            seconds = parseInt(timer % 60, 10);

            minutes = minutes < 10 ? "0" + minutes : minutes;
            seconds = seconds < 10 ? "0" + seconds : seconds;

            var output = minutes + " : " + seconds;
            display.text(output);
            $("title").html(output + " - TimerTimer");

            // flash screen every minute
            if (minutes != '59') {
                var flash_ints = ['01', '00', '59'];
            } else {
                var flash_ints = ['01', '00'];
            }
            
            if (minutes.toString() != '60') {
                if(flash_ints.indexOf(seconds.toString()) != -1) {
                    console.log(seconds);
                    flash();
                }
            }


            if (--timer < 0) {
                display.text("Time's Up!");
                clearInterval(refresh);  // exit refresh loop
                var music = $("#over_music")[0];
                music.play();
                alert("Time's Up!");
            }
        }, 1000);

    }

    function sleep(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
    async function flash() {
        document.body.style.backgroundColor = '#f00';
        await sleep(200);
        document.body.style.backgroundColor = '#ffffff';
    }


    // start timer
    jQuery(function ($) {
        if (Minutes > 0) {
            var display = $('#time');
            startTimer(Minutes, display);
        }
    });

    // show help information
    $('#help-info').hide();
    $('#help-btn').hover( function() { $('#help-info').toggle(); } );
})
