console.log("AI Proctoring Active");

let cheatingDetected = false;
let warningCount = 0;

function stopExam(){

    if(!cheatingDetected){

        cheatingDetected = true;

        alert("❌ Cheating detected. Interview terminated.");

        window.location.href="/";

    }

}


// TAB SWITCH

document.addEventListener("visibilitychange", function(){

    if(document.hidden){

        warningCount++;

        alert("⚠ Tab switching detected!");

        if(warningCount >= 1){

            stopExam();

        }

    }

});


// WINDOW SWITCH

window.addEventListener("blur", function(){

    warningCount++;

    alert("⚠ Window switch detected!");

    if(warningCount >= 1){

        stopExam();

    }

});


// Disable right click

document.addEventListener("contextmenu", function(e){

    e.preventDefault();

});


// Block DevTools

document.onkeydown = function(e){

    if(e.keyCode == 123){
        return false;
    }

    if(e.ctrlKey && e.shiftKey && e.keyCode == 73){
        return false;
    }

    if(e.ctrlKey && e.keyCode == 85){
        return false;
    }

};


// Reload detection

window.onbeforeunload = function(){

    return "Refreshing will restart the interview.";

};