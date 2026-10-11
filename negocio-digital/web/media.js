(function(){
var box=document.getElementById("video-box");
if(box){
var v=box.querySelector("video"),src=v&&v.querySelector("source");
function fallo(){box.classList.add("fallo")}
if(src&&window.fetch){fetch(src.getAttribute("src"),{method:"HEAD"}).then(function(x){if(!x.ok)fallo()}).catch(fallo)}
if(src)src.addEventListener("error",fallo);
if(v)v.addEventListener("error",fallo);
}
var imgs=document.querySelectorAll(".ph img");
for(var i=0;i<imgs.length;i++)(function(im){
function mal(){im.hidden=true}
im.addEventListener("error",mal);
if(im.complete&&im.naturalWidth===0)mal();
})(imgs[i]);
})();
