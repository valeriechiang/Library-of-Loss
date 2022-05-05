function search(){
    let keyword=$("#search").val()
    window.location="/search/"+keyword

}


$(document).ready(function(){
    //when the page loads, display all the names
    for (let i = 1; i < 30; i++) {
        $("#food"+i).click(function(){
            window.location="/view/"+i
        })
    }
    $("#submit_search").click(function(){
        search()
    })

    $("#search").keypress(function(e){     
        if(e.which == 13) {
            search()
        }
    })
    var custfilter = new RegExp(keyword, "ig")
    var repstr = "<span class='highlight'>" + keyword + "</span>"

    if (keyword != "") {
        console.log(keyword)
        //alert("hi")
        $(".listitem").each(function() {
            console.log($(this).html)
            $(this).html($(this).html().replace(custfilter, repstr));
        })
    }
    
    


})


