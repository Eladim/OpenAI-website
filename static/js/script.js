$(document).ready(function() {
    $(".about-click").click(function(){
        $(".about-content").slideToggle("slow");
    });

    $('#carouselExampleIndicators').carousel({
        interval: 3000
    });
});
