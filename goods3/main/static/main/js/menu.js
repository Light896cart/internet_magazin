    function SaveSelectValue(el) {
      localStorage.setItem(el.name, el.value);
    }
    function LoadSelectValue(el) {
      return localStorage.getItem(el.name);
    }

    let selectCheck = document.querySelector("[name='selectcheck']");
    selectCheck.value = LoadSelectValue(selectCheck);




var c = 0;
    function menut(){//для открывающего и закрывающего меню
    if(c==0){
        document.querySelector(".two_menu").style.display = 'block';
        document.querySelector(".button").style.transform = 'rotate(90deg)';
        c++;}
    else{
        document.querySelector(".two_menu").style.display = 'none';
        document.querySelector(".button").style.transform = 'rotate(0deg)';
        c--;}
}
function menut1(){//для открывающего и закрывающего меню
    if(c==0){
        document.querySelector(".two_menu1").style.display = 'block';
        document.querySelector(".button1").style.transform = 'rotate(90deg)';
        c++;}
    else{
        document.querySelector(".two_menu1").style.display = 'none';
        document.querySelector(".button1").style.transform = 'rotate(0deg)';
        c--;}
}
$('.two_products_each').click(function() {
    $('.products .photo_product').css({
        'width': '49%'
        });
    $('.content img').css({
        'height' : 'auto'
        });
    });
$('.three_products_each').click(function() {
    $('.products .photo_product').css({
        'width': '32.3%'
        });
    });



$(document).ready(function(){

    $(".img_photo").click(function(){

        var largePath = $(this).attr("src");

        $("#largeImg").attr({ src: largePath });
         return false;
    });

 });
$(document).ready(function(){

    $(".sidebar_acordion .sidebar_category_left").eq(0).addClass("active");
    $(".accordion .sidebar_subcategory_left").eq(0).show();

    $(".sidebar_acordion .sidebar_category_left").click(function(){
        $(this).next(".sidebar_subcategory_left").slideToggle("fast").siblings(".sidebar_subcategory_left:visible");
        $(this).toggleClass("active");
        $(this).siblings(".sidebar_category_left").removeClass("active");
    });

});
$(function() {
	var $menu_popup = $('.menu-popup');

	$(".menu-triger").click(function(){
		$('body').addClass('body_pointer');
		$menu_popup.show(0);
		$menu_popup.animate(
			{left: parseInt($menu_popup.css('left'),10) == 0 ? -$menu_popup.outerWidth() : 0},
			300
		);
		return false;
	});

	$(".menu-close").click(function(){
		$('body').removeClass('body_pointer');
		$menu_popup.animate(
			{left: parseInt($menu_popup.css('left'),10) == 0 ? -$menu_popup.outerWidth() : 0},
			300,
			function(){
				$menu_popup.hide(0);
			}
		);
		return false;
	});

	$(document).on('click', function(e){
		if (!$(e.target).closest('.menu-popup').length){
			$('body').removeClass('body_pointer');
			$menu_popup.animate(
				{left: parseInt($menu_popup.css('left'),10) == 0 ? -$menu_popup.outerWidth() : 0},
				300,
				function(){
					$menu_popup.hide(0);
				}
			);
		}
	});
});
/*function post(){
    if(c==0){
        document.querySelector(".post_content_on").style.display = 'none';
        c++;}
    else{
        document.querySelector(".post_content_on").style.display = 'block';
        c--;}
}
function post1(){
    if(c==0){
        document.querySelector(".post_structure_on").style.display = 'block';
        c++;}
    else{
        document.querySelector(".post_structure_on").style.display = 'none';
        c--;}
}
function post2(){
    if(c==0){
        document.querySelector(".post_care_on").style.display = 'block';
        c++;}
    else{
        document.querySelector(".post_care_on").style.display = 'none';
        c--;}
}*/
function menut2(){//для открывающего и закрывающего меню
    if(c==0){
        document.querySelector(".two_menu2").style.display = 'block';
        document.querySelector(".button2").style.transform = 'rotate(90deg)';
        c++;}
    else{
        document.querySelector(".two_menu2").style.display = 'none';
        document.querySelector(".button2").style.transform = 'rotate(0deg)';
        c--;}
}

const header = document.querySelector('.bottom_header');
const first  = document.querySelector('.bottom_header');//будем искать нашу высоту
const headerHeight = header.offsetHeight;
const firstHeight = first.offsetHeight;
window.addEventListener('scroll',()=>{//проверяем высоту
    let scrollDistance = window.scrollY;
    if(scrollDistance >= firstHeight + headerHeight){
        header.classList.add('header--fixed');
        first.style.marginTop = '${headerHeight}px';
    }else{
        header.classList.remove('header--fixed');
        first.style.marginTop = null;
    }
});
const header_bottom = document.querySelector('.filter');
const first_bottom  = document.querySelector('.filter');//будем искать нашу высоту
const headerHeight_bottom = header.offsetHeight;
const firstHeight_bottom = first.offsetHeight;
window.addEventListener('scroll',()=>{//проверяем высоту
    let scrollDistance = window.scrollY;
    if(scrollDistance >= firstHeight_bottom + headerHeight_bottom){
        header_bottom.classList.add('header_bottom--fixed');
        first_bottom.style.marginTop = '${headerHeight_bottom}px';
    }else{
        header_bottom.classList.remove('header_bottom--fixed');
        first_bottom.style.marginTop = null;
    }
});
//для фиксирование sidebar
const sidebar = document.querySelector('.sidebar');
const firsr  = document.querySelector('.men');//будем искать нашу высоту
const sidebarHeight = sidebar.offsetHeight;
const firsrHeight = firsr.offsetHeight;
window.addEventListener('scroll',()=>{//проверяем высоту
    let scrollDistance = window.scrollY;
    if(scrollDistance >= firsrHeight + 30){
        sidebar.classList.add('sidebar--fixed');
        firsr.style.marginTop = '${sidebarHeight}px';
    }else{
        sidebar.classList.remove('sidebar--fixed');
        firsr.style.marginTop = null;
    }
});