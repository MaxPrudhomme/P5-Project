window.onscroll = function() {scrollFunction()}

function scrollFunction()
{
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) 
    { 
        document.getElementById("projectLogo").style.width = "109px";
        document.getElementById("projectLogo").style.height = "82px";
        document.getElementById("mainMenu").style.marginTop = "20px";
    } 
    else 
    { 
        document.getElementById("projectLogo").style.width = "218px";
        document.getElementById("projectLogo").style.height = "164px";
        document.getElementById("mainMenu").style.marginTop = "60px";
    }
}

function displaySection(ele)
{
    ele = ele.getAttribute("section")
    var sections = ['projectSection','technicalOverviewSection','documentationSection','teamSection', 'roadmapSection', 'statsSection', 'telemetrySection']
    var cIndex = sections.indexOf(ele)
    var caller = document.getElementById(sections[cIndex])
    sections.splice(cIndex,1);
    for(i in sections) { document.getElementById(sections[i]).style.opacity = 0; document.getElementById(sections[i]).style.display = 'none'; }
    caller.style.display = 'block';
    setTimeout(function(){ caller.style.opacity = 1; }, 0.5)
}

function changeLanguage(id)
{
    body = document.body
    if (id == "en") {$(body).load("en.html")}
    else if (id == "fr") {$(body).load("fr.html")}
}