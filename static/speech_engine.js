let questions=[]
let index=0

function speak(text){

let speech = new SpeechSynthesisUtterance(text)

speech.rate=1
speech.pitch=1

window.speechSynthesis.speak(speech)

}

function startAvatarInterview(q){

questions=q

document.getElementById("question-box").innerText=q[0]

initAvatar()

speak(q[0])

}

function nextQuestion(){

index++

if(index>=questions.length){

window.location="/hr_result"

return

}

document.getElementById("question-box").innerText=questions[index]

speak(questions[index])

}


function startListening(){

const recognition=new webkitSpeechRecognition()

recognition.lang="en-US"

recognition.onresult=function(event){

let answer = event.results[0][0].transcript

document.getElementById("answer-box").value=answer

}

recognition.start()

}