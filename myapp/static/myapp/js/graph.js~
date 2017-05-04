$(document).ready(function() {
	//alert("loaded");

	//$( "#cssmenu ul li:first-child" ).addClass("active");






	$("#cssmenu ul li a").click(function(){
	//alert("entered");

	//alert($(this).text());

	$(this).siblings(".active").removeClass("active");

	$(this).addClass("active");
	//alert(this);

	
		
	});


$('#dropDownId :selected').text();

$("div.previousData-graphs div").css("display","none");
$("div.previousData-graphs div.m1-view").css("display","block");
$("div.previousData-graphs div.m12-view").css("display","block");
$("div.temp").css("display","block");

$("div.previousData-view input:button").click(function(){

	$("div.previousData-view input:button").removeClass("clicked");
	var my = $(this).attr("class");
	//alert(my);
	
	$(this).addClass("clicked");
	var o= "."+my+"-view";
	//alert(o);
	//alert(o);
	$("div.previousData-graphs div").css("display","none");
	//alert(o);
	$(o).css("display","block");

});



/*$("div.previousData-view input:button").hover(

   function(){
     
	if($(this).hasClass('m6-view'))
	{
		$("span.low").css("display","block");
	}
	if($(this).hasClass('m3-view'))
	{
		$("span.middle").css("display","block");
	}
	if($(this).hasClass('m1-view'))
	{
		$("span.high").css("display","block");
	}

  
   }, function() {


    $( this ).find( ".low, .middle, .high" ).hide();
  }
);





$(".multi-graphs div.graph_data").hide();


$("div.graph_data:first").show();


    $("#next").click(function(){
	alert($("div.graph_data:visible").next("div.graph_data").length);
        if ($("div.graph_data:visible").next("div.graph_data").length !=0){
            $("div.graph_data:visible").next("div.graph_data").show();
	    $(this).hide();}

        else {
            $("div.graph_data:visible").hide();
            $("div.graph_data:first").show();
        }
    });

    $("#prev").click(function(){
alert($("div.graph_data:visible").prev("div.graph_data").length);
        if ($("div.graph_data:visible").prev("div.graph_data").length !=0){
            $("div.graph_data:visible").prev("div.graph_data").show();
            $(this).hide();}
        else {
            $("div.graph_data:visible").hide();
            $("div.graph_data:last").show();
        }
    });*/



});
