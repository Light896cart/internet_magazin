$(document).ready(function(){

    $(".accordion .text_post").eq(0).addClass("active");
    $(".accordion .content_post").eq(0).show();

    $(".accordion .text_post").click(function(){
        $(this).next(".content_post").slideToggle("fast").siblings(".content_post:visible").slideUp("fast");
        $(this).toggleClass("active");
        $(this).siblings(".text_post").removeClass("active");
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
document.querySelector('button').addEventListener('click', () => {
  document.querySelector('.menu_mobile').classList.add('active');
  document.querySelector("*").style.overflow = 'hidden';
  document.querySelector(".two_sidebar_right_side").style.right = '0';
  document.querySelector(".two_sidebar_right_side").style.opacity = '0.8';

  document.querySelector('.close-menu').classList.add('close-menu-active');
})
// а тут мы вешаем на кнопку close-menu событие которое пр кликена кнопку
// удаляет menu_mobile  класс  active

document.querySelector('.close-menu').addEventListener('click', () => {
  document.querySelector('.menu_mobile').classList.remove('active');
  document.querySelector("*").style.overflow = 'auto';
  document.querySelector(".two_sidebar_right_side").style.right = '-100%';
  document.querySelector(".two_sidebar_right_side").style.opacity = '0';
  document.querySelector('.close-menu').classList.remove('close-menu-active')
})

$(document).ready(function(){

    $(".list_all_menu .product_category").eq(0).addClass("active");
    $(".accordion .product_category_if_item").eq(0).show();

    $(".list_all_menu .product_category").click(function(){
        $(this).next(".product_category_if_item").slideToggle("fast").siblings(".product_category_if_item:visible");
        $(this).toggleClass("active");
        $(this).siblings(".product_category").removeClass("active");
    });

});