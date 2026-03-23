let scene;
let camera;
let renderer;

function initAvatar(){

scene = new THREE.Scene();

camera = new THREE.PerspectiveCamera(
75,
window.innerWidth/window.innerHeight,
0.1,
1000
);

renderer = new THREE.WebGLRenderer({antialias:true});

renderer.setSize(window.innerWidth*0.65,window.innerHeight);

document.getElementById("avatar-container")
.appendChild(renderer.domElement);


/* LIGHT */

const light = new THREE.DirectionalLight(0xffffff,1)

light.position.set(0,5,5)

scene.add(light)


/* HEAD */

const head = new THREE.Mesh(

new THREE.SphereGeometry(1,32,32),

new THREE.MeshStandardMaterial({color:0xaaaaaa})

)

head.position.y=1.8

scene.add(head)


/* BODY */

const body = new THREE.Mesh(

new THREE.CylinderGeometry(0.8,0.8,2),

new THREE.MeshStandardMaterial({color:0x4facfe})

)

scene.add(body)


/* EYES */

const eye1 = new THREE.Mesh(

new THREE.SphereGeometry(0.1),

new THREE.MeshStandardMaterial({color:0x00ffff})

)

eye1.position.set(-0.3,2,0.9)

scene.add(eye1)

const eye2 = eye1.clone()

eye2.position.x=0.3

scene.add(eye2)


camera.position.z=5

animate()

}

function animate(){

requestAnimationFrame(animate)

renderer.render(scene,camera)

}