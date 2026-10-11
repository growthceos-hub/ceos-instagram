(function(){
var PIXEL_ID="{{PIXEL_ID}}",K="ceos_cookies",MESES=12,b=document.getElementById("cookies"),r=document.getElementById("reabrir-cookies"),h=document.documentElement;
function pixel(){
if(window.fbq||PIXEL_ID.indexOf("{{")===0)return;
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");
fbq("init",PIXEL_ID);fbq("track","PageView");
document.dispatchEvent(new Event("ceos:pixel"));
}
function leer(){
try{var d=JSON.parse(localStorage.getItem(K));
if(d&&(d.v==="si"||d.v==="no")&&d.e>Date.now())return d.v;
localStorage.removeItem(K)}catch(e){}
return null}
function guardar(v){
var t=new Date(),e=new Date(t);e.setMonth(e.getMonth()+MESES);
try{localStorage.setItem(K,JSON.stringify({v:v,t:t.toISOString(),e:e.getTime()}))}catch(x){}}
function mostrar(){
if(!b)return;
b.hidden=false;h.classList.add("con-cookies");
document.body.style.setProperty("--alto-cookies",b.offsetHeight+"px");
b.focus()}
function ocultar(){
if(!b)return;
b.hidden=true;h.classList.remove("con-cookies");
if(r)r.focus()}
function decidir(v){guardar(v);ocultar();if(v==="si")pixel()}
var s=leer();
if(s==="si")pixel();else if(!s)mostrar();
if(b){
b.querySelector("[data-si]").addEventListener("click",function(){decidir("si")});
b.querySelector("[data-no]").addEventListener("click",function(){decidir("no")})}
if(r)r.addEventListener("click",mostrar);
})();
