(function(){
// El valor de la compra lo envia el servidor (Conversions API, via Make). Aqui solo se manda
// el evento Purchase con eventID = session_id de Stripe, para que Meta deduplique.
var id=new URLSearchParams(location.search).get("session_id");
if(!id||!/^cs_(test|live)_[A-Za-z0-9]{10,200}$/.test(id))return;
document.addEventListener("ceos:pixel",function(){
if(window.__ceosPurchase||!window.fbq)return;
window.__ceosPurchase=1;
fbq("track","Purchase",{},{eventID:id});
});
})();
