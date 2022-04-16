window.onscroll = function() {scrollFunction()}

function scrollFunction()
{
    if (document.body.scrollTop > 80 || document.documentElement.scrollTop > 80) 
    { 
        document.getElementById("projectLogo").style.width = "200px";
        document.getElementById("projectLogo").style.height = "80px";
        document.getElementById("mainMenu").style.marginTop = "20px";
    } 
    else 
    { 
        document.getElementById("projectLogo").style.width = "400px";
        document.getElementById("projectLogo").style.height = "160px";
        document.getElementById("mainMenu").style.marginTop = "60px";
    }
}

function displaySection(ele)
{
    var buttons = ['projectSectionButton','technicalOverviewSectionButton','documentationSectionButton','teamSectionButton']
    var sections = ['projectSection','technicalOverviewSection','documentationSection','teamSection']
    var cIndex = buttons.indexOf(ele)
    var caller = document.getElementById(sections[cIndex])
    sections.splice(cIndex,1);
    for(i in sections) { document.getElementById(sections[i]).style.opacity = 0; document.getElementById(sections[i]).style.display = 'none'; }
    caller.style.display = 'block';
    setTimeout(function(){ caller.style.opacity = 1; }, 0.5)
}