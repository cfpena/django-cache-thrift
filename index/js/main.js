var gifs = ['https://38.media.tumblr.com/9f6c25cc350f12aa74a7dc386a5c4985/tumblr_mevmyaKtDf1rgvhr8o1_500.gif',
'https://38.media.tumblr.com/9ead028ef62004ef6ac2b92e52edd210/tumblr_nok4eeONTv1s2yegdo1_400.gif',
'https://38.media.tumblr.com/9f43dc410be85b1159d1f42663d811d7/tumblr_mllh01J96X1s9npefo1_250.gif',
'https://38.media.tumblr.com/9f659499c8754e40cf3f7ac21d08dae6/tumblr_nqlr0rn8ox1r2r0koo1_400.gif',
'https://38.media.tumblr.com/9ed1c99afa7d71411884101cb054f35f/tumblr_mvtuwlhSkE1qbnleeo1_500.gif',
'https://38.media.tumblr.com/9e437d26769cb2ac4217df14dbb20034/tumblr_npw7v7W07C1tmj047o1_250.gif',
'https://38.media.tumblr.com/9e4ab65c0e7d4bb8aa6b5be854b83794/tumblr_mdlv9v6hE91qanrf2o1_r11_500.gif',
'https://38.media.tumblr.com/9ecd3483028290171dcb5e920ff4e3bb/tumblr_nkcmeflaVj1u26rdio1_500.gif',
'https://38.media.tumblr.com/9f83754d20ce882224ae3392a8372ee8/tumblr_mkwd0y8Poo1qlnbq8o1_400.gif',
'https://38.media.tumblr.com/9e6fcb37722bf01996209bdf76708559/tumblr_np9xo74UgD1ux4g5vo1_250.gif'];

console.log("hola");

function showTop(container){
	console.log("entro");
	for (var i=0; i < 10; i++) {
        etiqueta= "#gif" + i;
        //console.log(etiqueta);
        img = container.querySelector(etiqueta);
        //console.log(img)
        img.src = gifs[i];
      }

}

let contenedor = document.querySelector('.container');
showTop(contenedor);

