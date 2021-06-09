console.log('wohoo')
var modal = document.getElementById("myModal");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg");
var expandButton = document.getElementsByClassName('expand-button')[0];
var modalImg = document.getElementById("img01");
var captionText = document.getElementById("caption");

expandButton.onclick = function () {
    console.log('clicked')
    modal.style.display = "block";
    modalImg.src = img.src;
    captionText.innerHTML = img.alt;
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on <span> (x), close the modal
span.onclick = function () {
    modal.style.display = "none";
}