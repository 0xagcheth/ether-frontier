const canvas=document.querySelector("#canvas"),ctx=canvas.getContext("2d");
const BG_URL="../assets/sprite-atlases/battlefield-background/runtime/backgroud.png";
const state={screen:"description-driven-restart-v3",status:"watchtower_generation_pending",background:null};
function loadImage(src){return new Promise((resolve,reject)=>{const image=new Image();image.onload=()=>resolve(image);image.onerror=reject;image.src=src;});}
function draw(){ctx.clearRect(0,0,720,720);if(state.background){const image=state.background,scale=Math.max(720/image.width,720/image.height),w=image.width*scale,h=image.height*scale;ctx.drawImage(image,(720-w)/2,(720-h)/2,w,h);}ctx.fillStyle="rgba(5,10,11,.76)";ctx.fillRect(0,0,720,720);ctx.textAlign="center";ctx.fillStyle="#d59b4e";ctx.font="12px system-ui";ctx.fillText("VISUAL PIPELINE RESET",360,325);ctx.fillStyle="#f1e7d2";ctx.font="34px Georgia";ctx.fillText("WATCHTOWER V3",360,372);ctx.fillStyle="#91a09b";ctx.font="12px system-ui";ctx.fillText("Description-driven layered master is being rebuilt",360,408);}
async function boot(){state.background=await loadImage(BG_URL);document.querySelector("#objectTitle").innerHTML="WATCH<br>TOWER";document.querySelector("#objectDescription").textContent="Старая crossbow-family ветка архивирована. Новый Warden's Post строится заново по исходному описанию объекта.";document.querySelector("#stateReadout").textContent="RESET";document.querySelector("#spriteCount").textContent="0";document.querySelector("#atlasReadout").textContent="PENDING";document.querySelector("#actions").innerHTML="";document.querySelector("#objectSwitch").innerHTML="";draw();}
window.advanceTime=()=>draw();
window.render_game_to_text=()=>JSON.stringify({...state,background:state.background?BG_URL:null,bakedCompositeFrames:false});
document.querySelector("#resetButton").onclick=draw;
boot().catch(error=>{console.error(error);document.querySelector("#stateReadout").textContent="LOAD ERROR";});
