navigator.mediaDevices.getUserMedia({video:true})

.then(stream=>{

let video=document.getElementById("camera-box")

video.srcObject=stream

})