const Images = [
    'dune1.jpg',
    'dune2.jpg',
    'dune3.png'
]


$(document).ready(changeImage);

function changeImage() {


    $('#review').each(function (index, element) {
        $(element).attr("src", "{% static 'images/"+Images[generateRanNum()]+"' %}", );
    })


}

function generateRanNum() {
    return Math.floor(Math.random() * Images.length);
}