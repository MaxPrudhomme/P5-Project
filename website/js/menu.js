window.onscroll = function() {scrollFunction()}

function scrollFunction()
{
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) 
    { 
        document.getElementById("projectLogo").style.width = "200px";
        document.getElementById("projectLogo").style.height = "75px";
        document.getElementById("mainMenu").style.marginTop = "10px";
    } 
    else 
    { 
        document.getElementById("projectLogo").style.width = "400px";
        document.getElementById("projectLogo").style.height = "150px";
        document.getElementById("mainMenu").style.marginTop = "80px";
    }
}