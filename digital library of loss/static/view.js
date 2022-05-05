$(document).ready(function(){
    for (let i = 1; i < 30; i++) {
        $("#edit"+i).click(function(){
            window.location="/edit/"+i
        })
    }})