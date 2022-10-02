$(document).ready(function(){
    $(".joke").hover(function(){
        $(this).fadeOut(5000)
        $(this).text('Шутка :)');
    });
});

$(window).focus(function() {
  document.title = "CIA";
});

$(window).blur(function() {
  document.title = "Витя лошок";
});

$(document).ready(function(){
	$(".wiki_mini_wnd").hover(function(){
		$(this).color(red);
	});
});



