let recorder;
let chunks=[];

async function startRecording(){

const stream = await navigator.mediaDevices.getUserMedia({audio:true});

recorder = new MediaRecorder(stream);

recorder.start();

recorder.ondataavailable=e=>chunks.push(e.data);

recorder.onstop=sendAudio;

setTimeout(()=>recorder.stop(),5000);
}

async function sendAudio(){

const blob = new Blob(chunks);

const form = new FormData();

form.append("audio",blob,"audio.wav");

const response = await fetch("/submit_audio",{

method:"POST",

body:form

});

document.write(await response.text());
}