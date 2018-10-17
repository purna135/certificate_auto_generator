function display(id) {
    // Get the modal
    var modal = document.getElementById('myModal');

    // Get the image and insert it inside the modal
    var img = document.getElementById(id);
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");

    modal.style.display = "block";
    modalImg.src = img.src;
    captionText.innerHTML = img.alt;

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
    modal.style.display = "none";
    }
}

function printImg(id) {
    var win = window.open('');
    var img_src = document.getElementById(id).getAttribute("src");
    win.document.write('<img src="' + img_src + '" width="700" height="940" />');
    win.print();
    win.focus();    //for IE
}

function printAll(img_list) {
    win = window.open('');
    img_list.forEach(function (id) {
        var img_src = document.getElementById(id).getAttribute("src");
        win.document.write('<img src="' + img_src + '" width="700" height="940" />');
    })
    win.print();
    win.focus(); //for IE
}
