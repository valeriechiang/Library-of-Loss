$(document).ready(function(){
    //when the page loads, display all the names
    $("#addbutton").click(function(){
        window.location="/add"
    })

    $("#submit").click(function(){
        $(".warningdiv").empty()
        let title=$("#inputname").val()
        let image=$("#inputimg").val()
        let alt=$("#inputalt").val()
        let about=$("#inputabout").val()
        let rating=$("#inputrating").val()
        let dishes=$("#inputdishes").val()
        
        let noerror=true
        if (title==""){
            $("#namewarning").append('<button id="error">Empty Title</button>')
            $("#inputname").focus()
            noerror=false
        }
        if (image==""){
            $("#imagewarning").append('<button id="error">Empty Image</button>')
            $("#inputimg").focus()
            noerror=false
        }
        if (about==""){
            $("#aboutwarning").append('<button id="error">Empty Explanation</button>')
            $("#inputabout").focus()
            noerror=false
        }
        if (dishes==""){
            $("#disheswarning").append('<button id="error">Empty Quote</button>')
            $("#inputdishes").focus()
            noerror=false
        }


        if (noerror){
            let data_to_save = {"title": title, "image":image, "alt":alt,"about":about,"rating":rating,"Quote":dishes}         
            $.ajax({
                type: "POST",
                url: "add_entry",                
                dataType : "json",
                contentType: "application/json; charset=utf-8",
                data : JSON.stringify(data_to_save),
                success: function(result){
                    $(".warningdiv").empty()
                    let all_data = result["new_entry"]
                    //should be getting the new entry back
                    console.log(all_data)
                    currentid=all_data["id"]
                    $("#success").append('Item Added Successfully!<button id="view">View Now</button>')
                    $("#view").click(function(){
                        window.location="/view/"+currentid
                    })
                    $("#inputname").val("")
                    $("#inputimg").val("")
                    $("#inputalt").val("")
                    $("#inputabout").val("")
                    $("#inputrating").val("")
                    $("#inputdishes").val("")
                        
                },
                error: function(request, status, error){
                    console.log("Error");
                    console.log(request)
                    console.log(status)
                    console.log(error)
                }
            })

        }

    })
})