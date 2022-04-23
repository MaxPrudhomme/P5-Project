function launcher()
{
    document.getElementById('submitArrow').style.marginLeft = '50px';
    setTimeout(function(){
        document.getElementById('submitArrow').style.display= "none"
        document.getElementById('submitArrow').style.opacity= "0"
        document.getElementById('checkmark').style.display= "block"
        document.getElementById('submitArrow').style.marginLeft = '-50px';
    },0500)
    var result = {};
    $.each($('#emailField').serializeArray(), function() {
        result[this.name] = this.value;
    });
    $.ajax({
        type: 'GET',
        url: 'https://project.maxprudhomme.com/launchPlatform',
        data: result,}).done(function(){
                document.getElementById('checkmark').style.animation="fill .4s ease-in-out .4s forwards, scale .3s ease-in-out .9s both";
                document.getElementById('checkmark__circle').style.animation="stroke 0.6s cubic-bezier(0.65, 0, 0.45, 1) forwards";
                document.getElementById('checkmark__check').style.animation="stroke 0.3s cubic-bezier(0.65, 0, 0.45, 1) 0.8s forwards";
            setTimeout(function(){
                document.getElementById('checkmark').style.opacity= "0"
            },2000)
            setTimeout(function(){
                document.getElementById('checkmark').style.display= "none"
                document.getElementById('submitArrow').style.display= "block"
                document.getElementById('submitArrow').style.opacity= "1"
            },3000)
            setTimeout(function(){
                document.getElementById('submitArrow').style.marginLeft = '0px';
            },3500)  
        })
}