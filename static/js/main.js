const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// Function to fadeout Error Message - NOT working Though

setTimeout(function(){
    $('#message').fadeOut('slow');
}, 4000);