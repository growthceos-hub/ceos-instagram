(function(){
var PIXEL_ID="{{PIXEL_ID}}",K="ceos_cookies",b=document.getElementById("cookies");
function pixel(){
if(document.body.getAttribute("data-pixel")==="manual"){document.dispatchEvent(new Event("ceos:consent"));return}
if(window.fbq||PIXEL_ID.indexOf("{{")===0)return;
!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version="2.0";n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(window,document,"script","https://connect.facebook.net/en_US/fbevents.js");
fbq("init",PIXEL_ID);fbq("track","PageView");
document.dispatchEvent(new Event("ceos:pixel"));
}
function set(v){try{localStorage.setItem(K,v)}catch(e){}if(b)b.hidden=true;if(v==="si")pixel()}
var s=null;try{s=localStorage.getItem(K)}catch(e){}
if(s==="si")pixel();else if(!s&&b)b.hidden=false;
if(b){b.querySelector("[data-si]").addEventListener("click",function(){set("si")});
b.querySelector("[data-no]").addEventListener("click",function(){set("no")})}
var r=document.getElementById("reabrir-cookies");
if(r)r.addEventListener("click",function(e){e.preventDefault();if(b)b.hidden=false});
})();
