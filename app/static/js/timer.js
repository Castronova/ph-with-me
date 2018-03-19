
// set initial value for the minutes variable
var socket;
var Minutes = -1;
var timer_running = null;
var current_min = null;
var current_sec = null;
var display; 

$(document).ready(function() {

    // set the timer element for later
    display = $('#time');

    // connect to the chat socket
    socket = io.connect('http://' + document.domain + ':' + location.port + '/chat');
    
    // enable/disable the admin buttons, timer not running
    enablebuttons(false)

    // SocketIO handlers for sharing messages with the chatroom
    socket.on('timerupdate', function(data) {
	text = data.msg;
	$('#time').text(text);
    });

});

// timer function
function startTimer(minutes) {

    // enable/disable the admin buttons, timer not running
    enablebuttons(true)

    var timer = minutes, seconds;
    timer_running = 1;
    intervalID = null;
    var refresh = setInterval(function () {
        minutes = parseInt(timer / 60, 10)
        seconds = parseInt(timer % 60, 10);

        minutes = minutes < 10 ? "0" + minutes : minutes;
        seconds = seconds < 10 ? "0" + seconds : seconds;
        
        // exit if "stop" was pressed
        if (!timer_running){
    	console.log('clearing interval')
    	current_min = minutes
    	current_sec = seconds
    	clearInterval(intervalID);
        }

	// send the updated time to the chat room via server/events
        var output = minutes + " : " + seconds;
	socket.emit('timer', output);
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


	// decrement the timer
        if (--timer < 0) {
	    // DO SOMETHING WHEN THE TIMER RUNS OUT	
            display.text("Time's Up!");
            clearInterval(refresh);  // exit refresh loop
            var music = $("#over_music")[0];
                music.play();
             alert("Time's Up!");
         }
     }, 1000);
 }

function pause() {
    alert('paused')
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function enablebuttons(timer_running) {
    // utility function for enabling and disabling the admin controls
    // based on whether or not the timer is running.

    if (timer_running){
	$('#startph').attr("disabled",true);
	$('#pauseph').attr("disabled",false);
	$('#resetph').attr("disabled",false);
    } else {
	$('#startph').attr("disabled",false);
	$('#pauseph').attr("disabled",true);
	$('#resetph').attr("disabled",true);
    }
}
async function flash() {
    document.body.style.backgroundColor = '#f00';
    await sleep(200);
    document.body.style.backgroundColor = '#ffffff';
}

    
// stop timer
jQuery(function ($) {
    if (Minutes > 0) {
	timer_running = 0;
    }
});


